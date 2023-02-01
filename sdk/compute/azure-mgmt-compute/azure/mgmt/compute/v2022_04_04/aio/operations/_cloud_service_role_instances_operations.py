# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, AsyncIterator, Callable, Dict, Optional, TypeVar, Union, cast
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
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
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._cloud_service_role_instances_operations import (
    build_delete_request,
    build_get_instance_view_request,
    build_get_remote_desktop_file_request,
    build_get_request,
    build_list_request,
    build_rebuild_request,
    build_reimage_request,
    build_restart_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class CloudServiceRoleInstancesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.compute.v2022_04_04.aio.ComputeManagementClient`'s
        :attr:`cloud_service_role_instances` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self, role_instance_name: str, resource_group_name: str, cloud_service_name: str, **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-04-04"] = kwargs.pop("api_version", _params.pop("api-version", "2022-04-04"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            role_instance_name=role_instance_name,
            resource_group_name=resource_group_name,
            cloud_service_name=cloud_service_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._delete_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/cloudServices/{cloudServiceName}/roleInstances/{roleInstanceName}"
    }

    @distributed_trace_async
    async def begin_delete(
        self, role_instance_name: str, resource_group_name: str, cloud_service_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Deletes a role instance from a cloud service.

        :param role_instance_name: Name of the role instance. Required.
        :type role_instance_name: str
        :param resource_group_name: Name of the resource group. Required.
        :type resource_group_name: str
        :param cloud_service_name: Name of the cloud service. Required.
        :type cloud_service_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-04-04"] = kwargs.pop("api_version", _params.pop("api-version", "2022-04-04"))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_initial(  # type: ignore
                role_instance_name=role_instance_name,
                resource_group_name=resource_group_name,
                cloud_service_name=cloud_service_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/cloudServices/{cloudServiceName}/roleInstances/{roleInstanceName}"
    }

    @distributed_trace_async
    async def get(
        self,
        role_instance_name: str,
        resource_group_name: str,
        cloud_service_name: str,
        expand: Optional[Union[str, _models.InstanceViewTypes]] = None,
        **kwargs: Any
    ) -> _models.RoleInstance:
        """Gets a role instance from a cloud service.

        :param role_instance_name: Name of the role instance. Required.
        :type role_instance_name: str
        :param resource_group_name: Name of the resource group. Required.
        :type resource_group_name: str
        :param cloud_service_name: Name of the cloud service. Required.
        :type cloud_service_name: str
        :param expand: The expand expression to apply to the operation. 'UserData' is not supported for
         cloud services. Known values are: "instanceView" and "userData". Default value is None.
        :type expand: str or ~azure.mgmt.compute.v2022_04_04.models.InstanceViewTypes
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleInstance or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2022_04_04.models.RoleInstance
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

        api_version: Literal["2022-04-04"] = kwargs.pop("api_version", _params.pop("api-version", "2022-04-04"))
        cls: ClsType[_models.RoleInstance] = kwargs.pop("cls", None)

        request = build_get_request(
            role_instance_name=role_instance_name,
            resource_group_name=resource_group_name,
            cloud_service_name=cloud_service_name,
            subscription_id=self._config.subscription_id,
            expand=expand,
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

        deserialized = self._deserialize("RoleInstance", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/cloudServices/{cloudServiceName}/roleInstances/{roleInstanceName}"
    }

    @distributed_trace_async
    async def get_instance_view(
        self, role_instance_name: str, resource_group_name: str, cloud_service_name: str, **kwargs: Any
    ) -> _models.RoleInstanceView:
        """Retrieves information about the run-time state of a role instance in a cloud service.

        :param role_instance_name: Name of the role instance. Required.
        :type role_instance_name: str
        :param resource_group_name: Name of the resource group. Required.
        :type resource_group_name: str
        :param cloud_service_name: Name of the cloud service. Required.
        :type cloud_service_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleInstanceView or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2022_04_04.models.RoleInstanceView
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

        api_version: Literal["2022-04-04"] = kwargs.pop("api_version", _params.pop("api-version", "2022-04-04"))
        cls: ClsType[_models.RoleInstanceView] = kwargs.pop("cls", None)

        request = build_get_instance_view_request(
            role_instance_name=role_instance_name,
            resource_group_name=resource_group_name,
            cloud_service_name=cloud_service_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_instance_view.metadata["url"],
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

        deserialized = self._deserialize("RoleInstanceView", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_instance_view.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/cloudServices/{cloudServiceName}/roleInstances/{roleInstanceName}/instanceView"
    }

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        cloud_service_name: str,
        expand: Optional[Union[str, _models.InstanceViewTypes]] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.RoleInstance"]:
        """Gets the list of all role instances in a cloud service. Use nextLink property in the response
        to get the next page of role instances. Do this till nextLink is null to fetch all the role
        instances.

        :param resource_group_name: Name of the resource group. Required.
        :type resource_group_name: str
        :param cloud_service_name: Name of the cloud service. Required.
        :type cloud_service_name: str
        :param expand: The expand expression to apply to the operation. 'UserData' is not supported for
         cloud services. Known values are: "instanceView" and "userData". Default value is None.
        :type expand: str or ~azure.mgmt.compute.v2022_04_04.models.InstanceViewTypes
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either RoleInstance or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.compute.v2022_04_04.models.RoleInstance]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-04-04"] = kwargs.pop("api_version", _params.pop("api-version", "2022-04-04"))
        cls: ClsType[_models.RoleInstanceListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    resource_group_name=resource_group_name,
                    cloud_service_name=cloud_service_name,
                    subscription_id=self._config.subscription_id,
                    expand=expand,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("RoleInstanceListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/cloudServices/{cloudServiceName}/roleInstances"
    }

    async def _restart_initial(  # pylint: disable=inconsistent-return-statements
        self, role_instance_name: str, resource_group_name: str, cloud_service_name: str, **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-04-04"] = kwargs.pop("api_version", _params.pop("api-version", "2022-04-04"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_restart_request(
            role_instance_name=role_instance_name,
            resource_group_name=resource_group_name,
            cloud_service_name=cloud_service_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._restart_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _restart_initial.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/cloudServices/{cloudServiceName}/roleInstances/{roleInstanceName}/restart"
    }

    @distributed_trace_async
    async def begin_restart(
        self, role_instance_name: str, resource_group_name: str, cloud_service_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """The Reboot Role Instance asynchronous operation requests a reboot of a role instance in the
        cloud service.

        :param role_instance_name: Name of the role instance. Required.
        :type role_instance_name: str
        :param resource_group_name: Name of the resource group. Required.
        :type resource_group_name: str
        :param cloud_service_name: Name of the cloud service. Required.
        :type cloud_service_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-04-04"] = kwargs.pop("api_version", _params.pop("api-version", "2022-04-04"))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._restart_initial(  # type: ignore
                role_instance_name=role_instance_name,
                resource_group_name=resource_group_name,
                cloud_service_name=cloud_service_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_restart.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/cloudServices/{cloudServiceName}/roleInstances/{roleInstanceName}/restart"
    }

    async def _reimage_initial(  # pylint: disable=inconsistent-return-statements
        self, role_instance_name: str, resource_group_name: str, cloud_service_name: str, **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-04-04"] = kwargs.pop("api_version", _params.pop("api-version", "2022-04-04"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_reimage_request(
            role_instance_name=role_instance_name,
            resource_group_name=resource_group_name,
            cloud_service_name=cloud_service_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._reimage_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _reimage_initial.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/cloudServices/{cloudServiceName}/roleInstances/{roleInstanceName}/reimage"
    }

    @distributed_trace_async
    async def begin_reimage(
        self, role_instance_name: str, resource_group_name: str, cloud_service_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """The Reimage Role Instance asynchronous operation reinstalls the operating system on instances
        of web roles or worker roles.

        :param role_instance_name: Name of the role instance. Required.
        :type role_instance_name: str
        :param resource_group_name: Name of the resource group. Required.
        :type resource_group_name: str
        :param cloud_service_name: Name of the cloud service. Required.
        :type cloud_service_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-04-04"] = kwargs.pop("api_version", _params.pop("api-version", "2022-04-04"))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._reimage_initial(  # type: ignore
                role_instance_name=role_instance_name,
                resource_group_name=resource_group_name,
                cloud_service_name=cloud_service_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_reimage.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/cloudServices/{cloudServiceName}/roleInstances/{roleInstanceName}/reimage"
    }

    async def _rebuild_initial(  # pylint: disable=inconsistent-return-statements
        self, role_instance_name: str, resource_group_name: str, cloud_service_name: str, **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-04-04"] = kwargs.pop("api_version", _params.pop("api-version", "2022-04-04"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_rebuild_request(
            role_instance_name=role_instance_name,
            resource_group_name=resource_group_name,
            cloud_service_name=cloud_service_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._rebuild_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _rebuild_initial.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/cloudServices/{cloudServiceName}/roleInstances/{roleInstanceName}/rebuild"
    }

    @distributed_trace_async
    async def begin_rebuild(
        self, role_instance_name: str, resource_group_name: str, cloud_service_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """The Rebuild Role Instance asynchronous operation reinstalls the operating system on instances
        of web roles or worker roles and initializes the storage resources that are used by them. If
        you do not want to initialize storage resources, you can use Reimage Role Instance.

        :param role_instance_name: Name of the role instance. Required.
        :type role_instance_name: str
        :param resource_group_name: Name of the resource group. Required.
        :type resource_group_name: str
        :param cloud_service_name: Name of the cloud service. Required.
        :type cloud_service_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-04-04"] = kwargs.pop("api_version", _params.pop("api-version", "2022-04-04"))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._rebuild_initial(  # type: ignore
                role_instance_name=role_instance_name,
                resource_group_name=resource_group_name,
                cloud_service_name=cloud_service_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_rebuild.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/cloudServices/{cloudServiceName}/roleInstances/{roleInstanceName}/rebuild"
    }

    @distributed_trace_async
    async def get_remote_desktop_file(
        self, role_instance_name: str, resource_group_name: str, cloud_service_name: str, **kwargs: Any
    ) -> AsyncIterator[bytes]:
        """Gets a remote desktop file for a role instance in a cloud service.

        :param role_instance_name: Name of the role instance. Required.
        :type role_instance_name: str
        :param resource_group_name: Name of the resource group. Required.
        :type resource_group_name: str
        :param cloud_service_name: Name of the cloud service. Required.
        :type cloud_service_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Async iterator of the response bytes or the result of cls(response)
        :rtype: AsyncIterator[bytes]
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

        api_version: Literal["2022-04-04"] = kwargs.pop("api_version", _params.pop("api-version", "2022-04-04"))
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        request = build_get_remote_desktop_file_request(
            role_instance_name=role_instance_name,
            resource_group_name=resource_group_name,
            cloud_service_name=cloud_service_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_remote_desktop_file.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=True, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    get_remote_desktop_file.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/cloudServices/{cloudServiceName}/roleInstances/{roleInstanceName}/remoteDesktopFile"
    }
