# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.timeseriesinsights import TimeSeriesInsightsClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-timeseriesinsights
# USAGE
    python environments_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = TimeSeriesInsightsClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.environments.begin_update(
        resource_group_name="rg1",
        environment_name="env1",
        environment_update_parameters={"tags": {"someTag": "someTagValue"}},
    ).result()
    print(response)


# x-ms-original-file: specification/timeseriesinsights/resource-manager/Microsoft.TimeSeriesInsights/preview/2021-03-31-preview/examples/EnvironmentsPatchTags.json
if __name__ == "__main__":
    main()
