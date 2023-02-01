# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""
FILE: sample_satellite_download_async.py

DESCRIPTION:
    This sample demonstrates:
    - Creating a Farmer and a Boundary
    - Queuing a satellite data ingestion job, and waiting for its completion
    - Dowloading the data parallelly with a set max degree of concurrency

USAGE:
    ```python sample_satellite_download_async.py```

    Set the environment variables with your own values before running the sample:
    - `AZURE_TENANT_ID`: The tenant ID of your active directory application.
    - `AZURE_CLIENT_ID`: The client ID of your active directory application.
    - `AZURE_CLIENT_SECRET`: The client secret of your active directory application.
    - `FARMBEATS_ENDPOINT`: The FarmBeats endpoint that you want to run these samples on.
"""

from azure.core.exceptions import ResourceNotFoundError
from azure.identity.aio import DefaultAzureCredential
from azure.agrifood.farming.aio import FarmBeatsClient
from azure.agrifood.farming.models import Farmer, Boundary, Polygon, SatelliteDataIngestionJob, SatelliteData
import asyncio
from datetime import datetime
from urllib.parse import urlparse, parse_qs
from random import randint
from pathlib import Path
import os
from isodate import UTC
from dotenv import load_dotenv

# Helper to retrive the file path param from FarmBeats data store path.
def parse_file_path_from_file_link(file_link):
    return parse_qs(urlparse(file_link).query)['filePath'][0]

# Helper to download a given scene file path and store it to
# the specified out path. Waits on the given semaphore to limit
# max concurrency.
async def download_image(client, file_link, out_path, semaphore):
    file_path = parse_file_path_from_file_link(file_link)
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    async with semaphore:
        print(f"Async downloading image to {out_path.resolve()}")
        with open(out_path, 'wb') as tif_file:
            file_stream = await client.scenes.download(file_path)
            async for bits in file_stream:
                tif_file.write(bits)
        return str(out_path.resolve())
        
async def sample_satellite_download_async():

    farmbeats_endpoint = os.environ['FARMBEATS_ENDPOINT']

    credential = DefaultAzureCredential()

    client = FarmBeatsClient(
        endpoint=farmbeats_endpoint,
        credential=credential
    )

    farmer_id = "contoso-farmer"
    boundary_id = "contoso-boundary"
    job_id_prefix = "contoso-job"
    start_date_time = datetime(2020, 1, 1, tzinfo=UTC)
    end_date_time = datetime(2020, 1, 31, tzinfo=UTC)
    data_root_dir = os.path.join(os.path.dirname(__file__), "..", "data", "satellite")

    # Create or update a farmer within FarmBeats.
    print(
        f"Ensure farmer with id {farmer_id} exists... ", end="", flush=True)
    farmer = await client.farmers.create_or_update(
        farmer_id=farmer_id,
        farmer=Farmer()
    )
    print("Done")

    # Create a boundary if the boundary does not exist.
    try:
        print(
            f"Checking if boundary with id {boundary_id} exists... ", end="", flush=True)
        boundary = await client.boundaries.get(
            farmer_id=farmer_id,
            boundary_id=boundary_id
        )
        print("Exists")
        
    except ResourceNotFoundError as e:
        print("Boundary doesn't exist. Creating... ", end="", flush=True)
        # Creating a boundary.
        boundary = await client.boundaries.create_or_update(
            farmer_id=farmer_id,
            boundary_id=boundary_id,
            boundary=Boundary(
                geometry=Polygon(
                    coordinates=[
                        [
                            [79.27057921886444, 18.042507660177698],
                            [79.26899135112762, 18.040135849620704],
                            [79.27113711833954, 18.03927382882835],
                            [79.27248358726501, 18.041069275656195],
                            [79.27057921886444, 18.042507660177698]
                        ]
                    ]
                )
            )
        )
        print("Created")

    # Queue a satellite job and wait for completion.
    job_id = f"{job_id_prefix}-{randint(0, 1000)}"
    print(f"Queuing satellite job {job_id}... ", end="", flush=True)
    satellite_job_poller = await client.scenes.begin_create_satellite_data_ingestion_job(
        job_id=job_id,
        job=SatelliteDataIngestionJob(
            farmer_id=farmer_id,
            boundary_id=boundary_id,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            data=SatelliteData(
                image_names=[
                    "LAI"
                ]
            )
        )
    )
    print("Queued. Waiting for completion... ", end="", flush=True)
    await satellite_job_poller.result()
    print(f"Job completed with status {satellite_job_poller.status()}")

    # Get scenes which are available in FarmBeats for our farmer and boundary of intrest.
    print("Getting scenes list... ", end="", flush=True)
    scenes = client.scenes.list(
        boundary.farmer_id,
        boundary.id,
        start_date_time=start_date_time,
        end_date_time=end_date_time,
    )
    print("Done")

    # Setting up async function to parallely download images.
    files_to_download = list()
    async for scene in scenes:
        safe_datetime_str = scene.scene_date_time.strftime("%Y-%m-%d %H-%M-%S")
        scene_out_path = Path(
            data_root_dir,
            scene.provider,
            scene.source,
            safe_datetime_str
        )
        for image_file in scene.image_files:
            band_out_path = Path(
                scene_out_path,
                f"{image_file.name}-{int(image_file.resolution)}.tif"
            )
            files_to_download.append((image_file.file_link, band_out_path))

    download_semaphore = asyncio.Semaphore(2)
    
    # Download images asynchronously and await completion.
    await asyncio.gather(
        *[download_image(client, file_link, out_path, download_semaphore) for file_link, out_path in files_to_download])

    print("Downloads done")

    await client.close()
    await credential.close()


if __name__ == "__main__":

    load_dotenv()

    asyncio.run(sample_satellite_download_async())
