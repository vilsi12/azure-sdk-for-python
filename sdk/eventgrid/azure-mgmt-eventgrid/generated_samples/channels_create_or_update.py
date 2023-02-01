# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.eventgrid import EventGridManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-eventgrid
# USAGE
    python channels_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = EventGridManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="5b4b650e-28b9-4790-b3ab-ddbd88d727c4",
    )

    response = client.channels.create_or_update(
        resource_group_name="examplerg",
        partner_namespace_name="examplePartnerNamespaceName1",
        channel_name="exampleChannelName1",
        channel_info={
            "properties": {
                "channelType": "PartnerTopic",
                "expirationTimeIfNotActivatedUtc": "2021-10-21T22:50:25.410433Z",
                "messageForActivation": "Example message to approver",
                "partnerTopicInfo": {
                    "azureSubscriptionId": "5b4b650e-28b9-4790-b3ab-ddbd88d727c4",
                    "name": "examplePartnerTopic1",
                    "resourceGroupName": "examplerg2",
                    "source": "ContosoCorp.Accounts.User1",
                },
            }
        },
    )
    print(response)


# x-ms-original-file: specification/eventgrid/resource-manager/Microsoft.EventGrid/stable/2022-06-15/examples/Channels_CreateOrUpdate.json
if __name__ == "__main__":
    main()
