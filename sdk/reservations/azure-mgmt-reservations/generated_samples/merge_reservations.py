# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.reservations import AzureReservationAPI

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-reservations
# USAGE
    python merge_reservations.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AzureReservationAPI(
        credential=DefaultAzureCredential(),
    )

    response = client.reservation.begin_merge(
        reservation_order_id="276e7ae4-84d0-4da6-ab4b-d6b94f3557da",
        body={
            "properties": {
                "sources": [
                    "/providers/Microsoft.Capacity/reservationOrders/c0565a8a-4491-4e77-b07b-5e6d66718e1c/reservations/cea04232-932e-47db-acb5-e29a945ecc73",
                    "/providers/Microsoft.Capacity/reservationOrders/c0565a8a-4491-4e77-b07b-5e6d66718e1c/reservations/5bf54dc7-dacd-4f46-a16b-7b78f4a59799",
                ]
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/reservations/resource-manager/Microsoft.Capacity/stable/2022-03-01/examples/MergeReservations.json
if __name__ == "__main__":
    main()
