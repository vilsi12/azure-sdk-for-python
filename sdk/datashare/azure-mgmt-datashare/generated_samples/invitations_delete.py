# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.datashare import DataShareManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-datashare
# USAGE
    python invitations_delete.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DataShareManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="433a8dfd-e5d5-4e77-ad86-90acdc75eb1a",
    )

    response = client.invitations.delete(
        resource_group_name="SampleResourceGroup",
        account_name="Account1",
        share_name="Share1",
        invitation_name="Invitation1",
    )
    print(response)


# x-ms-original-file: specification/datashare/resource-manager/Microsoft.DataShare/stable/2020-09-01/examples/Invitations_Delete.json
if __name__ == "__main__":
    main()
