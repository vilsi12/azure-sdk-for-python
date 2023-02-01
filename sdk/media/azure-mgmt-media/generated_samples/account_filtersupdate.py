# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.media import AzureMediaServices

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-media
# USAGE
    python account_filtersupdate.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AzureMediaServices(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.account_filters.update(
        resource_group_name="contoso",
        account_name="contosomedia",
        filter_name="accountFilterWithTimeWindowAndTrack",
        parameters={
            "properties": {
                "firstQuality": {"bitrate": 128000},
                "presentationTimeRange": {
                    "endTimestamp": 170000000,
                    "forceEndTimestamp": False,
                    "liveBackoffDuration": 0,
                    "presentationWindowDuration": 9223372036854775000,
                    "startTimestamp": 10,
                    "timescale": 10000000,
                },
            }
        },
    )
    print(response)


# x-ms-original-file: specification/mediaservices/resource-manager/Microsoft.Media/Metadata/stable/2022-08-01/examples/accountFilters-update.json
if __name__ == "__main__":
    main()
