# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.billing import BillingManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-billing
# USAGE
    python billing_profile_role_definition.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = BillingManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.billing_role_definitions.get_by_billing_profile(
        billing_account_name="{billingAccountName}",
        billing_profile_name="{billingProfileName}",
        billing_role_definition_name="{billingRoleDefinitionName}",
    )
    print(response)


# x-ms-original-file: specification/billing/resource-manager/Microsoft.Billing/stable/2020-05-01/examples/BillingProfileRoleDefinition.json
if __name__ == "__main__":
    main()
