# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import DataLakeAnalyticsAccountManagementClientConfiguration
from .operations import (
    AccountsOperations,
    ComputePoliciesOperations,
    DataLakeStoreAccountsOperations,
    FirewallRulesOperations,
    LocationsOperations,
    Operations,
    StorageAccountsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class DataLakeAnalyticsAccountManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Creates an Azure Data Lake Analytics account management client.

    :ivar accounts: AccountsOperations operations
    :vartype accounts: azure.mgmt.datalake.analytics.account.aio.operations.AccountsOperations
    :ivar data_lake_store_accounts: DataLakeStoreAccountsOperations operations
    :vartype data_lake_store_accounts:
     azure.mgmt.datalake.analytics.account.aio.operations.DataLakeStoreAccountsOperations
    :ivar storage_accounts: StorageAccountsOperations operations
    :vartype storage_accounts:
     azure.mgmt.datalake.analytics.account.aio.operations.StorageAccountsOperations
    :ivar compute_policies: ComputePoliciesOperations operations
    :vartype compute_policies:
     azure.mgmt.datalake.analytics.account.aio.operations.ComputePoliciesOperations
    :ivar firewall_rules: FirewallRulesOperations operations
    :vartype firewall_rules:
     azure.mgmt.datalake.analytics.account.aio.operations.FirewallRulesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.datalake.analytics.account.aio.operations.Operations
    :ivar locations: LocationsOperations operations
    :vartype locations: azure.mgmt.datalake.analytics.account.aio.operations.LocationsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Get subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2019-11-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = DataLakeAnalyticsAccountManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.accounts = AccountsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.data_lake_store_accounts = DataLakeStoreAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.storage_accounts = StorageAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.compute_policies = ComputePoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.firewall_rules = FirewallRulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.locations = LocationsOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DataLakeAnalyticsAccountManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
