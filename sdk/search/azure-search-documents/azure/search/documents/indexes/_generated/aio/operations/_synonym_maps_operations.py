# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.3, generator: @autorest/python@6.2.3)
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

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._synonym_maps_operations import (
    build_create_or_update_request,
    build_create_request,
    build_delete_request,
    build_get_request,
    build_list_request,
)
from .._vendor import SearchServiceClientMixinABC

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SynonymMapsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~search_service_client.aio.SearchServiceClient`'s
        :attr:`synonym_maps` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create_or_update(
        self,
        synonym_map_name: str,
        prefer: Union[str, _models.Enum0],
        synonym_map: _models.SynonymMap,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SynonymMap:
        """Creates a new synonym map or updates a synonym map if it already exists.

        :param synonym_map_name: The name of the synonym map to create or update. Required.
        :type synonym_map_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~search_service_client.models.Enum0
        :param synonym_map: The definition of the synonym map to create or update. Required.
        :type synonym_map: ~search_service_client.models.SynonymMap
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynonymMap or the result of cls(response)
        :rtype: ~search_service_client.models.SynonymMap
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        synonym_map_name: str,
        prefer: Union[str, _models.Enum0],
        synonym_map: IO,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SynonymMap:
        """Creates a new synonym map or updates a synonym map if it already exists.

        :param synonym_map_name: The name of the synonym map to create or update. Required.
        :type synonym_map_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~search_service_client.models.Enum0
        :param synonym_map: The definition of the synonym map to create or update. Required.
        :type synonym_map: IO
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynonymMap or the result of cls(response)
        :rtype: ~search_service_client.models.SynonymMap
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        synonym_map_name: str,
        prefer: Union[str, _models.Enum0],
        synonym_map: Union[_models.SynonymMap, IO],
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> _models.SynonymMap:
        """Creates a new synonym map or updates a synonym map if it already exists.

        :param synonym_map_name: The name of the synonym map to create or update. Required.
        :type synonym_map_name: str
        :param prefer: For HTTP PUT requests, instructs the service to return the created/updated
         resource on success. "return=representation" Required.
        :type prefer: str or ~search_service_client.models.Enum0
        :param synonym_map: The definition of the synonym map to create or update. Is either a model
         type or a IO type. Required.
        :type synonym_map: ~search_service_client.models.SynonymMap or IO
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynonymMap or the result of cls(response)
        :rtype: ~search_service_client.models.SynonymMap
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
        )  # type: Literal["2021-04-30-Preview"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SynonymMap]

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(synonym_map, (IO, bytes)):
            _content = synonym_map
        else:
            _json = self._serialize.body(synonym_map, "SynonymMap")

        request = build_create_or_update_request(
            synonym_map_name=synonym_map_name,
            prefer=prefer,
            x_ms_client_request_id=_x_ms_client_request_id,
            if_match=if_match,
            if_none_match=if_none_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize("SynonymMap", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("SynonymMap", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {"url": "/synonymmaps('{synonymMapName}')"}  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        synonym_map_name: str,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a synonym map.

        :param synonym_map_name: The name of the synonym map to delete. Required.
        :type synonym_map_name: str
        :param if_match: Defines the If-Match condition. The operation will be performed only if the
         ETag on the server matches this value. Default value is None.
        :type if_match: str
        :param if_none_match: Defines the If-None-Match condition. The operation will be performed only
         if the ETag on the server does not match this value. Default value is None.
        :type if_none_match: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
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
        )  # type: Literal["2021-04-30-Preview"]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_delete_request(
            synonym_map_name=synonym_map_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            if_match=if_match,
            if_none_match=if_none_match,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/synonymmaps('{synonymMapName}')"}  # type: ignore

    @distributed_trace_async
    async def get(
        self, synonym_map_name: str, request_options: Optional[_models.RequestOptions] = None, **kwargs: Any
    ) -> _models.SynonymMap:
        """Retrieves a synonym map definition.

        :param synonym_map_name: The name of the synonym map to retrieve. Required.
        :type synonym_map_name: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynonymMap or the result of cls(response)
        :rtype: ~search_service_client.models.SynonymMap
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
        )  # type: Literal["2021-04-30-Preview"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SynonymMap]

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_get_request(
            synonym_map_name=synonym_map_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SynonymMap", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/synonymmaps('{synonymMapName}')"}  # type: ignore

    @distributed_trace_async
    async def list(
        self, select: Optional[str] = None, request_options: Optional[_models.RequestOptions] = None, **kwargs: Any
    ) -> _models.ListSynonymMapsResult:
        """Lists all synonym maps available for a search service.

        :param select: Selects which top-level properties of the synonym maps to retrieve. Specified as
         a comma-separated list of JSON property names, or '*' for all properties. The default is all
         properties. Default value is None.
        :type select: str
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListSynonymMapsResult or the result of cls(response)
        :rtype: ~search_service_client.models.ListSynonymMapsResult
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
        )  # type: Literal["2021-04-30-Preview"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ListSynonymMapsResult]

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_list_request(
            select=select,
            x_ms_client_request_id=_x_ms_client_request_id,
            api_version=api_version,
            template_url=self.list.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("ListSynonymMapsResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {"url": "/synonymmaps"}  # type: ignore

    @overload
    async def create(
        self,
        synonym_map: _models.SynonymMap,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SynonymMap:
        """Creates a new synonym map.

        :param synonym_map: The definition of the synonym map to create. Required.
        :type synonym_map: ~search_service_client.models.SynonymMap
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynonymMap or the result of cls(response)
        :rtype: ~search_service_client.models.SynonymMap
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self,
        synonym_map: IO,
        request_options: Optional[_models.RequestOptions] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SynonymMap:
        """Creates a new synonym map.

        :param synonym_map: The definition of the synonym map to create. Required.
        :type synonym_map: IO
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynonymMap or the result of cls(response)
        :rtype: ~search_service_client.models.SynonymMap
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create(
        self,
        synonym_map: Union[_models.SynonymMap, IO],
        request_options: Optional[_models.RequestOptions] = None,
        **kwargs: Any
    ) -> _models.SynonymMap:
        """Creates a new synonym map.

        :param synonym_map: The definition of the synonym map to create. Is either a model type or a IO
         type. Required.
        :type synonym_map: ~search_service_client.models.SynonymMap or IO
        :param request_options: Parameter group. Default value is None.
        :type request_options: ~search_service_client.models.RequestOptions
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SynonymMap or the result of cls(response)
        :rtype: ~search_service_client.models.SynonymMap
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
        )  # type: Literal["2021-04-30-Preview"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SynonymMap]

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(synonym_map, (IO, bytes)):
            _content = synonym_map
        else:
            _json = self._serialize.body(synonym_map, "SynonymMap")

        request = build_create_request(
            x_ms_client_request_id=_x_ms_client_request_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SynonymMap", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {"url": "/synonymmaps"}  # type: ignore
