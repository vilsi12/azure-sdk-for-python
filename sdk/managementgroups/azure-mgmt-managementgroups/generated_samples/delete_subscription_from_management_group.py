# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.managementgroups import ManagementGroupsAPI

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-managementgroups
# USAGE
    python delete_subscription_from_management_group.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ManagementGroupsAPI(
        credential=DefaultAzureCredential(),
    )

    response = client.management_group_subscriptions.delete(
        group_id="Group",
        subscription_id="728bcbe4-8d56-4510-86c2-4921b8beefbc",
    )
    print(response)


# x-ms-original-file: specification/managementgroups/resource-manager/Microsoft.Management/stable/2021-04-01/examples/RemoveManagementGroupSubscription.json
if __name__ == "__main__":
    main()
