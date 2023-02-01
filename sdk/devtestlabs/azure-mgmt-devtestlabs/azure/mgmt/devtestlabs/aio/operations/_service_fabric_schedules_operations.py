# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
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
from ...operations._service_fabric_schedules_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_execute_request,
    build_get_request,
    build_list_request,
    build_update_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ServiceFabricSchedulesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.devtestlabs.aio.DevTestLabsClient`'s
        :attr:`service_fabric_schedules` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        lab_name: str,
        user_name: str,
        service_fabric_name: str,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        top: Optional[int] = None,
        orderby: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.Schedule"]:
        """List schedules in a given service fabric.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param lab_name: The name of the lab. Required.
        :type lab_name: str
        :param user_name: The name of the user profile. Required.
        :type user_name: str
        :param service_fabric_name: The name of the service fabric. Required.
        :type service_fabric_name: str
        :param expand: Specify the $expand query. Example: 'properties($select=status)'. Default value
         is None.
        :type expand: str
        :param filter: The filter to apply to the operation. Example: '$filter=contains(name,'myName').
         Default value is None.
        :type filter: str
        :param top: The maximum number of resources to return from the operation. Example: '$top=10'.
         Default value is None.
        :type top: int
        :param orderby: The ordering expression for the results, using OData notation. Example:
         '$orderby=name desc'. Default value is None.
        :type orderby: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Schedule or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.devtestlabs.models.Schedule]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2018-09-15"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ScheduleList]

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
                    lab_name=lab_name,
                    user_name=user_name,
                    service_fabric_name=service_fabric_name,
                    subscription_id=self._config.subscription_id,
                    expand=expand,
                    filter=filter,
                    top=top,
                    orderby=orderby,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

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
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ScheduleList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        lab_name: str,
        user_name: str,
        service_fabric_name: str,
        name: str,
        expand: Optional[str] = None,
        **kwargs: Any
    ) -> _models.Schedule:
        """Get schedule.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param lab_name: The name of the lab. Required.
        :type lab_name: str
        :param user_name: The name of the user profile. Required.
        :type user_name: str
        :param service_fabric_name: The name of the service fabric. Required.
        :type service_fabric_name: str
        :param name: The name of the schedule. Required.
        :type name: str
        :param expand: Specify the $expand query. Example: 'properties($select=status)'. Default value
         is None.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Schedule or the result of cls(response)
        :rtype: ~azure.mgmt.devtestlabs.models.Schedule
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

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2018-09-15"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Schedule]

        request = build_get_request(
            resource_group_name=resource_group_name,
            lab_name=lab_name,
            user_name=user_name,
            service_fabric_name=service_fabric_name,
            name=name,
            subscription_id=self._config.subscription_id,
            expand=expand,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Schedule", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name}"}  # type: ignore

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        lab_name: str,
        user_name: str,
        service_fabric_name: str,
        name: str,
        schedule: _models.Schedule,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Schedule:
        """Create or replace an existing schedule.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param lab_name: The name of the lab. Required.
        :type lab_name: str
        :param user_name: The name of the user profile. Required.
        :type user_name: str
        :param service_fabric_name: The name of the service fabric. Required.
        :type service_fabric_name: str
        :param name: The name of the schedule. Required.
        :type name: str
        :param schedule: A schedule. Required.
        :type schedule: ~azure.mgmt.devtestlabs.models.Schedule
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Schedule or the result of cls(response)
        :rtype: ~azure.mgmt.devtestlabs.models.Schedule
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        lab_name: str,
        user_name: str,
        service_fabric_name: str,
        name: str,
        schedule: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Schedule:
        """Create or replace an existing schedule.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param lab_name: The name of the lab. Required.
        :type lab_name: str
        :param user_name: The name of the user profile. Required.
        :type user_name: str
        :param service_fabric_name: The name of the service fabric. Required.
        :type service_fabric_name: str
        :param name: The name of the schedule. Required.
        :type name: str
        :param schedule: A schedule. Required.
        :type schedule: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Schedule or the result of cls(response)
        :rtype: ~azure.mgmt.devtestlabs.models.Schedule
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        lab_name: str,
        user_name: str,
        service_fabric_name: str,
        name: str,
        schedule: Union[_models.Schedule, IO],
        **kwargs: Any
    ) -> _models.Schedule:
        """Create or replace an existing schedule.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param lab_name: The name of the lab. Required.
        :type lab_name: str
        :param user_name: The name of the user profile. Required.
        :type user_name: str
        :param service_fabric_name: The name of the service fabric. Required.
        :type service_fabric_name: str
        :param name: The name of the schedule. Required.
        :type name: str
        :param schedule: A schedule. Is either a model type or a IO type. Required.
        :type schedule: ~azure.mgmt.devtestlabs.models.Schedule or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Schedule or the result of cls(response)
        :rtype: ~azure.mgmt.devtestlabs.models.Schedule
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

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2018-09-15"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Schedule]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(schedule, (IO, bytes)):
            _content = schedule
        else:
            _json = self._serialize.body(schedule, "Schedule")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            lab_name=lab_name,
            user_name=user_name,
            service_fabric_name=service_fabric_name,
            name=name,
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
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("Schedule", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("Schedule", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name}"}  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        lab_name: str,
        user_name: str,
        service_fabric_name: str,
        name: str,
        **kwargs: Any
    ) -> None:
        """Delete schedule.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param lab_name: The name of the lab. Required.
        :type lab_name: str
        :param user_name: The name of the user profile. Required.
        :type user_name: str
        :param service_fabric_name: The name of the service fabric. Required.
        :type service_fabric_name: str
        :param name: The name of the schedule. Required.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
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

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2018-09-15"]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            lab_name=lab_name,
            user_name=user_name,
            service_fabric_name=service_fabric_name,
            name=name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name}"}  # type: ignore

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        lab_name: str,
        user_name: str,
        service_fabric_name: str,
        name: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs: Any
    ) -> _models.Schedule:
        """Allows modifying tags of schedules. All other properties will be ignored.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param lab_name: The name of the lab. Required.
        :type lab_name: str
        :param user_name: The name of the user profile. Required.
        :type user_name: str
        :param service_fabric_name: The name of the service fabric. Required.
        :type service_fabric_name: str
        :param name: The name of the schedule. Required.
        :type name: str
        :param tags: The tags of the resource. Default value is None.
        :type tags: dict[str, str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Schedule or the result of cls(response)
        :rtype: ~azure.mgmt.devtestlabs.models.Schedule
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

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2018-09-15"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Schedule]

        _schedule = _models.ScheduleFragment(tags=tags)
        _json = self._serialize.body(_schedule, "ScheduleFragment")

        request = build_update_request(
            resource_group_name=resource_group_name,
            lab_name=lab_name,
            user_name=user_name,
            service_fabric_name=service_fabric_name,
            name=name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Schedule", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name}"}  # type: ignore

    async def _execute_initial(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        lab_name: str,
        user_name: str,
        service_fabric_name: str,
        name: str,
        **kwargs: Any
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

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2018-09-15"]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_execute_request(
            resource_group_name=resource_group_name,
            lab_name=lab_name,
            user_name=user_name,
            service_fabric_name=service_fabric_name,
            name=name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._execute_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _execute_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name}/execute"}  # type: ignore

    @distributed_trace_async
    async def begin_execute(
        self,
        resource_group_name: str,
        lab_name: str,
        user_name: str,
        service_fabric_name: str,
        name: str,
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Execute a schedule. This operation can take a while to complete.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param lab_name: The name of the lab. Required.
        :type lab_name: str
        :param user_name: The name of the user profile. Required.
        :type user_name: str
        :param service_fabric_name: The name of the service fabric. Required.
        :type service_fabric_name: str
        :param name: The name of the schedule. Required.
        :type name: str
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

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2018-09-15"]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._execute_initial(  # type: ignore
                resource_group_name=resource_group_name,
                lab_name=lab_name,
                user_name=user_name,
                service_fabric_name=service_fabric_name,
                name=name,
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
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))  # type: AsyncPollingMethod
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
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_execute.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name}/execute"}  # type: ignore
