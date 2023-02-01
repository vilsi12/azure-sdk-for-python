# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._endpoints_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_update_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class EndpointsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.trafficmanager.aio.TrafficManagerManagementClient`'s
        :attr:`endpoints` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def update(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_type: Union[str, _models.EndpointType],
        endpoint_name: str,
        parameters: _models.Endpoint,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Endpoint:
        """Update a Traffic Manager endpoint.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param profile_name: The name of the Traffic Manager profile. Required.
        :type profile_name: str
        :param endpoint_type: The type of the Traffic Manager endpoint to be updated. Known values are:
         "AzureEndpoints", "ExternalEndpoints", and "NestedEndpoints". Required.
        :type endpoint_type: str or ~azure.mgmt.trafficmanager.models.EndpointType
        :param endpoint_name: The name of the Traffic Manager endpoint to be updated. Required.
        :type endpoint_name: str
        :param parameters: The Traffic Manager endpoint parameters supplied to the Update operation.
         Required.
        :type parameters: ~azure.mgmt.trafficmanager.models.Endpoint
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Endpoint or the result of cls(response)
        :rtype: ~azure.mgmt.trafficmanager.models.Endpoint
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_type: Union[str, _models.EndpointType],
        endpoint_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Endpoint:
        """Update a Traffic Manager endpoint.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param profile_name: The name of the Traffic Manager profile. Required.
        :type profile_name: str
        :param endpoint_type: The type of the Traffic Manager endpoint to be updated. Known values are:
         "AzureEndpoints", "ExternalEndpoints", and "NestedEndpoints". Required.
        :type endpoint_type: str or ~azure.mgmt.trafficmanager.models.EndpointType
        :param endpoint_name: The name of the Traffic Manager endpoint to be updated. Required.
        :type endpoint_name: str
        :param parameters: The Traffic Manager endpoint parameters supplied to the Update operation.
         Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Endpoint or the result of cls(response)
        :rtype: ~azure.mgmt.trafficmanager.models.Endpoint
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_type: Union[str, _models.EndpointType],
        endpoint_name: str,
        parameters: Union[_models.Endpoint, IO],
        **kwargs: Any
    ) -> _models.Endpoint:
        """Update a Traffic Manager endpoint.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param profile_name: The name of the Traffic Manager profile. Required.
        :type profile_name: str
        :param endpoint_type: The type of the Traffic Manager endpoint to be updated. Known values are:
         "AzureEndpoints", "ExternalEndpoints", and "NestedEndpoints". Required.
        :type endpoint_type: str or ~azure.mgmt.trafficmanager.models.EndpointType
        :param endpoint_name: The name of the Traffic Manager endpoint to be updated. Required.
        :type endpoint_name: str
        :param parameters: The Traffic Manager endpoint parameters supplied to the Update operation. Is
         either a model type or a IO type. Required.
        :type parameters: ~azure.mgmt.trafficmanager.models.Endpoint or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Endpoint or the result of cls(response)
        :rtype: ~azure.mgmt.trafficmanager.models.Endpoint
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-04-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Endpoint] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "Endpoint")

        request = build_update_request(
            resource_group_name=resource_group_name,
            profile_name=profile_name,
            endpoint_type=endpoint_type,
            endpoint_name=endpoint_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Endpoint", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/{endpointType}/{endpointName}"
    }

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_type: Union[str, _models.EndpointType],
        endpoint_name: str,
        **kwargs: Any
    ) -> _models.Endpoint:
        """Gets a Traffic Manager endpoint.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param profile_name: The name of the Traffic Manager profile. Required.
        :type profile_name: str
        :param endpoint_type: The type of the Traffic Manager endpoint. Known values are:
         "AzureEndpoints", "ExternalEndpoints", and "NestedEndpoints". Required.
        :type endpoint_type: str or ~azure.mgmt.trafficmanager.models.EndpointType
        :param endpoint_name: The name of the Traffic Manager endpoint. Required.
        :type endpoint_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Endpoint or the result of cls(response)
        :rtype: ~azure.mgmt.trafficmanager.models.Endpoint
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-04-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.Endpoint] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            profile_name=profile_name,
            endpoint_type=endpoint_type,
            endpoint_name=endpoint_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Endpoint", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/{endpointType}/{endpointName}"
    }

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_type: Union[str, _models.EndpointType],
        endpoint_name: str,
        parameters: _models.Endpoint,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Endpoint:
        """Create or update a Traffic Manager endpoint.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param profile_name: The name of the Traffic Manager profile. Required.
        :type profile_name: str
        :param endpoint_type: The type of the Traffic Manager endpoint to be created or updated. Known
         values are: "AzureEndpoints", "ExternalEndpoints", and "NestedEndpoints". Required.
        :type endpoint_type: str or ~azure.mgmt.trafficmanager.models.EndpointType
        :param endpoint_name: The name of the Traffic Manager endpoint to be created or updated.
         Required.
        :type endpoint_name: str
        :param parameters: The Traffic Manager endpoint parameters supplied to the CreateOrUpdate
         operation. Required.
        :type parameters: ~azure.mgmt.trafficmanager.models.Endpoint
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Endpoint or the result of cls(response)
        :rtype: ~azure.mgmt.trafficmanager.models.Endpoint
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_type: Union[str, _models.EndpointType],
        endpoint_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Endpoint:
        """Create or update a Traffic Manager endpoint.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param profile_name: The name of the Traffic Manager profile. Required.
        :type profile_name: str
        :param endpoint_type: The type of the Traffic Manager endpoint to be created or updated. Known
         values are: "AzureEndpoints", "ExternalEndpoints", and "NestedEndpoints". Required.
        :type endpoint_type: str or ~azure.mgmt.trafficmanager.models.EndpointType
        :param endpoint_name: The name of the Traffic Manager endpoint to be created or updated.
         Required.
        :type endpoint_name: str
        :param parameters: The Traffic Manager endpoint parameters supplied to the CreateOrUpdate
         operation. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Endpoint or the result of cls(response)
        :rtype: ~azure.mgmt.trafficmanager.models.Endpoint
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_type: Union[str, _models.EndpointType],
        endpoint_name: str,
        parameters: Union[_models.Endpoint, IO],
        **kwargs: Any
    ) -> _models.Endpoint:
        """Create or update a Traffic Manager endpoint.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param profile_name: The name of the Traffic Manager profile. Required.
        :type profile_name: str
        :param endpoint_type: The type of the Traffic Manager endpoint to be created or updated. Known
         values are: "AzureEndpoints", "ExternalEndpoints", and "NestedEndpoints". Required.
        :type endpoint_type: str or ~azure.mgmt.trafficmanager.models.EndpointType
        :param endpoint_name: The name of the Traffic Manager endpoint to be created or updated.
         Required.
        :type endpoint_name: str
        :param parameters: The Traffic Manager endpoint parameters supplied to the CreateOrUpdate
         operation. Is either a model type or a IO type. Required.
        :type parameters: ~azure.mgmt.trafficmanager.models.Endpoint or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Endpoint or the result of cls(response)
        :rtype: ~azure.mgmt.trafficmanager.models.Endpoint
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-04-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Endpoint] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "Endpoint")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            profile_name=profile_name,
            endpoint_type=endpoint_type,
            endpoint_name=endpoint_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("Endpoint", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("Endpoint", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    create_or_update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/{endpointType}/{endpointName}"
    }

    @distributed_trace_async
    async def delete(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_type: Union[str, _models.EndpointType],
        endpoint_name: str,
        **kwargs: Any
    ) -> Optional[_models.DeleteOperationResult]:
        """Deletes a Traffic Manager endpoint.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param profile_name: The name of the Traffic Manager profile. Required.
        :type profile_name: str
        :param endpoint_type: The type of the Traffic Manager endpoint to be deleted. Known values are:
         "AzureEndpoints", "ExternalEndpoints", and "NestedEndpoints". Required.
        :type endpoint_type: str or ~azure.mgmt.trafficmanager.models.EndpointType
        :param endpoint_name: The name of the Traffic Manager endpoint to be deleted. Required.
        :type endpoint_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DeleteOperationResult or None or the result of cls(response)
        :rtype: ~azure.mgmt.trafficmanager.models.DeleteOperationResult or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-04-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[Optional[_models.DeleteOperationResult]] = kwargs.pop("cls", None)

        request = build_delete_request(
            resource_group_name=resource_group_name,
            profile_name=profile_name,
            endpoint_type=endpoint_type,
            endpoint_name=endpoint_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("DeleteOperationResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/{endpointType}/{endpointName}"
    }
