# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload

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
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._scope_access_review_instances_operations import (
    build_create_request,
    build_get_by_id_request,
    build_list_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ScopeAccessReviewInstancesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.authorization.v2021_12_01_preview.aio.AuthorizationManagementClient`'s
        :attr:`scope_access_review_instances` attribute.
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
        self, scope: str, schedule_definition_id: str, filter: Optional[str] = None, **kwargs: Any
    ) -> AsyncIterable["_models.AccessReviewInstance"]:
        """Get access review instances.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param filter: The filter to apply on the operation. Other than standard filters, one custom
         filter option is supported : 'assignedToMeToReview()'. When one specified
         $filter=assignedToMeToReview(), only items that are assigned to the calling user to review are
         returned. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AccessReviewInstance or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewInstance]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-12-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AccessReviewInstanceListResult]

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
                    scope=scope,
                    schedule_definition_id=schedule_definition_id,
                    filter=filter,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("AccessReviewInstanceListResult", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/instances"}  # type: ignore

    @distributed_trace_async
    async def get_by_id(
        self, scope: str, schedule_definition_id: str, id: str, **kwargs: Any
    ) -> _models.AccessReviewInstance:
        """Get access review instances.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewInstance or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewInstance
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-12-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AccessReviewInstance]

        request = build_get_by_id_request(
            scope=scope,
            schedule_definition_id=schedule_definition_id,
            id=id,
            api_version=api_version,
            template_url=self.get_by_id.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AccessReviewInstance", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_id.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/instances/{id}"}  # type: ignore

    @overload
    async def create(
        self,
        scope: str,
        schedule_definition_id: str,
        id: str,
        properties: _models.AccessReviewInstanceProperties,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AccessReviewInstance:
        """Update access review instance.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :param properties: Access review instance properties. Required.
        :type properties:
         ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewInstanceProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewInstance or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewInstance
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self,
        scope: str,
        schedule_definition_id: str,
        id: str,
        properties: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AccessReviewInstance:
        """Update access review instance.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :param properties: Access review instance properties. Required.
        :type properties: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewInstance or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewInstance
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create(
        self,
        scope: str,
        schedule_definition_id: str,
        id: str,
        properties: Union[_models.AccessReviewInstanceProperties, IO],
        **kwargs: Any
    ) -> _models.AccessReviewInstance:
        """Update access review instance.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :param properties: Access review instance properties. Is either a model type or a IO type.
         Required.
        :type properties:
         ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewInstanceProperties or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessReviewInstance or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2021_12_01_preview.models.AccessReviewInstance
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-12-01-preview"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AccessReviewInstance]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(properties, (IO, bytes)):
            _content = properties
        else:
            _json = self._serialize.body(properties, "AccessReviewInstanceProperties")

        request = build_create_request(
            scope=scope,
            schedule_definition_id=schedule_definition_id,
            id=id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AccessReviewInstance", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/instances/{id}"}  # type: ignore
