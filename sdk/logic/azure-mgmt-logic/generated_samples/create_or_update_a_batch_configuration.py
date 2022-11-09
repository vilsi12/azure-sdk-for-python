# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.logic import LogicManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-logic
# USAGE
    python create_or_update_a_batch_configuration.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = LogicManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="34adfa4f-cedf-4dc0-ba29-b6d1a69ab345",
    )

    response = client.integration_account_batch_configurations.create_or_update(
        resource_group_name="testResourceGroup",
        integration_account_name="testIntegrationAccount",
        batch_configuration_name="testBatchConfiguration",
        batch_configuration={
            "location": "westus",
            "properties": {
                "batchGroupName": "DEFAULT",
                "releaseCriteria": {
                    "batchSize": 234567,
                    "messageCount": 10,
                    "recurrence": {
                        "frequency": "Minute",
                        "interval": 1,
                        "startTime": "2017-03-24T11:43:00",
                        "timeZone": "India Standard Time",
                    },
                },
            },
        },
    )
    print(response)


# x-ms-original-file: specification/logic/resource-manager/Microsoft.Logic/stable/2019-05-01/examples/IntegrationAccountBatchConfigurations_CreateOrUpdate.json
if __name__ == "__main__":
    main()
