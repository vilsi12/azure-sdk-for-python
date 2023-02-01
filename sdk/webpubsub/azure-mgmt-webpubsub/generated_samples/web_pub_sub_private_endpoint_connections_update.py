# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.webpubsub import WebPubSubManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-webpubsub
# USAGE
    python web_pub_sub_private_endpoint_connections_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = WebPubSubManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.web_pub_sub_private_endpoint_connections.update(
        private_endpoint_connection_name="mywebpubsubservice.1fa229cd-bf3f-47f0-8c49-afb36723997e",
        resource_group_name="myResourceGroup",
        resource_name="myWebPubSubService",
        parameters={
            "properties": {
                "privateEndpoint": {
                    "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/myResourceGroup/providers/Microsoft.Network/privateEndpoints/myPrivateEndpoint"
                },
                "privateLinkServiceConnectionState": {"actionsRequired": "None", "status": "Approved"},
            }
        },
    )
    print(response)


# x-ms-original-file: specification/webpubsub/resource-manager/Microsoft.SignalRService/preview/2022-08-01-preview/examples/WebPubSubPrivateEndpointConnections_Update.json
if __name__ == "__main__":
    main()
