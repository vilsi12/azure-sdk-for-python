# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.workloads import WorkloadsClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-workloads
# USAGE
    python sap_application_server_instances_delete.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = WorkloadsClient(
        credential=DefaultAzureCredential(),
        subscription_id="6d875e77-e412-4d7d-9af4-8895278b4443",
    )

    response = client.sap_application_server_instances.begin_delete(
        resource_group_name="test-rg",
        sap_virtual_instance_name="X00",
        application_instance_name="app01",
    ).result()
    print(response)


# x-ms-original-file: specification/workloads/resource-manager/Microsoft.Workloads/preview/2021-12-01-preview/examples/sapvirtualinstances/SAPApplicationServerInstances_Delete.json
if __name__ == "__main__":
    main()
