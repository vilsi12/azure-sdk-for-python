# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._service_operations import (
    build_get_properties_request,
    build_list_shares_segment_request,
    build_set_properties_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ServiceOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.fileshare.aio.AzureFileStorage`'s
        :attr:`service` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def set_properties(  # pylint: disable=inconsistent-return-statements
        self, storage_service_properties: _models.StorageServiceProperties, timeout: Optional[int] = None, **kwargs: Any
    ) -> None:
        """Sets properties for a storage account's File service endpoint, including properties for Storage
        Analytics metrics and CORS (Cross-Origin Resource Sharing) rules.

        :param storage_service_properties: The StorageService properties. Required.
        :type storage_service_properties: ~azure.storage.fileshare.models.StorageServiceProperties
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>`. Default value is None.
        :type timeout: int
        :keyword restype: restype. Default value is "service". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "properties". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        restype = kwargs.pop("restype", _params.pop("restype", "service"))  # type: str
        comp = kwargs.pop("comp", _params.pop("comp", "properties"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/xml"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _content = self._serialize.body(storage_service_properties, "StorageServiceProperties", is_xml=True)

        request = build_set_properties_request(
            url=self._config.url,
            timeout=timeout,
            restype=restype,
            comp=comp,
            content_type=content_type,
            version=self._config.version,
            content=_content,
            template_url=self.set_properties.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    set_properties.metadata = {"url": "{url}"}  # type: ignore

    @distributed_trace_async
    async def get_properties(self, timeout: Optional[int] = None, **kwargs: Any) -> _models.StorageServiceProperties:
        """Gets the properties of a storage account's File service, including properties for Storage
        Analytics metrics and CORS (Cross-Origin Resource Sharing) rules.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>`. Default value is None.
        :type timeout: int
        :keyword restype: restype. Default value is "service". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "properties". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageServiceProperties or the result of cls(response)
        :rtype: ~azure.storage.fileshare.models.StorageServiceProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        restype = kwargs.pop("restype", _params.pop("restype", "service"))  # type: str
        comp = kwargs.pop("comp", _params.pop("comp", "properties"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.StorageServiceProperties]

        request = build_get_properties_request(
            url=self._config.url,
            timeout=timeout,
            restype=restype,
            comp=comp,
            version=self._config.version,
            template_url=self.get_properties.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))

        deserialized = self._deserialize("StorageServiceProperties", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get_properties.metadata = {"url": "{url}"}  # type: ignore

    @distributed_trace_async
    async def list_shares_segment(
        self,
        prefix: Optional[str] = None,
        marker: Optional[str] = None,
        maxresults: Optional[int] = None,
        include: Optional[List[Union[str, "_models.ListSharesIncludeType"]]] = None,
        timeout: Optional[int] = None,
        **kwargs: Any
    ) -> _models.ListSharesResponse:
        """The List Shares Segment operation returns a list of the shares and share snapshots under the
        specified account.

        :param prefix: Filters the results to return only entries whose name begins with the specified
         prefix. Default value is None.
        :type prefix: str
        :param marker: A string value that identifies the portion of the list to be returned with the
         next list operation. The operation returns a marker value within the response body if the list
         returned was not complete. The marker value may then be used in a subsequent call to request
         the next set of list items. The marker value is opaque to the client. Default value is None.
        :type marker: str
        :param maxresults: Specifies the maximum number of entries to return. If the request does not
         specify maxresults, or specifies a value greater than 5,000, the server will return up to 5,000
         items. Default value is None.
        :type maxresults: int
        :param include: Include this parameter to specify one or more datasets to include in the
         response. Default value is None.
        :type include: list[str or ~azure.storage.fileshare.models.ListSharesIncludeType]
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>`. Default value is None.
        :type timeout: int
        :keyword comp: comp. Default value is "list". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListSharesResponse or the result of cls(response)
        :rtype: ~azure.storage.fileshare.models.ListSharesResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        comp = kwargs.pop("comp", _params.pop("comp", "list"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ListSharesResponse]

        request = build_list_shares_segment_request(
            url=self._config.url,
            prefix=prefix,
            marker=marker,
            maxresults=maxresults,
            include=include,
            timeout=timeout,
            comp=comp,
            version=self._config.version,
            template_url=self.list_shares_segment.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))

        deserialized = self._deserialize("ListSharesResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    list_shares_segment.metadata = {"url": "{url}"}  # type: ignore
