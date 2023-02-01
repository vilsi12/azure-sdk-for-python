# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Optional, TypeVar

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
from ...operations._queue_operations import (
    build_create_request,
    build_delete_request,
    build_get_access_policy_request,
    build_get_properties_request,
    build_set_access_policy_request,
    build_set_metadata_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class QueueOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.queue.aio.AzureQueueStorage`'s
        :attr:`queue` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def create(  # pylint: disable=inconsistent-return-statements
        self,
        timeout: Optional[int] = None,
        metadata: Optional[Dict[str, str]] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """creates a new queue under the given account.

        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>. Default value is None.
        :type timeout: int
        :param metadata: Optional. Include this parameter to specify that the queue's metadata be
         returned as part of the response body. Note that metadata requested with this parameter must be
         stored in accordance with the naming restrictions imposed by the 2009-09-19 version of the
         Queue service. Beginning with this version, all metadata names must adhere to the naming
         conventions for C# identifiers. Default value is None.
        :type metadata: dict[str, str]
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_create_request(
            url=self._config.url,
            timeout=timeout,
            metadata=metadata,
            request_id_parameter=request_id_parameter,
            version=self._config.version,
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

        if response.status_code not in [201, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 201:
            response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
            response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
            response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        if response.status_code == 204:
            response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
            response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
            response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    create.metadata = {"url": "{url}/{queueName}"}  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, timeout: Optional[int] = None, request_id_parameter: Optional[str] = None, **kwargs: Any
    ) -> None:
        """operation permanently deletes the specified queue.

        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            url=self._config.url,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            version=self._config.version,
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

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    delete.metadata = {"url": "{url}/{queueName}"}  # type: ignore

    @distributed_trace_async
    async def get_properties(  # pylint: disable=inconsistent-return-statements
        self, timeout: Optional[int] = None, request_id_parameter: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Retrieves user-defined metadata and queue properties on the specified queue. Metadata is
        associated with the queue as name-values pairs.

        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword comp: comp. Default value is "metadata". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        comp = kwargs.pop("comp", _params.pop("comp", "metadata"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_get_properties_request(
            url=self._config.url,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
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
        response_headers["x-ms-meta"] = self._deserialize("{str}", response.headers.get("x-ms-meta"))
        response_headers["x-ms-approximate-messages-count"] = self._deserialize(
            "int", response.headers.get("x-ms-approximate-messages-count")
        )
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    get_properties.metadata = {"url": "{url}/{queueName}"}  # type: ignore

    @distributed_trace_async
    async def set_metadata(  # pylint: disable=inconsistent-return-statements
        self,
        timeout: Optional[int] = None,
        metadata: Optional[Dict[str, str]] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """sets user-defined metadata on the specified queue. Metadata is associated with the queue as
        name-value pairs.

        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>. Default value is None.
        :type timeout: int
        :param metadata: Optional. Include this parameter to specify that the queue's metadata be
         returned as part of the response body. Note that metadata requested with this parameter must be
         stored in accordance with the naming restrictions imposed by the 2009-09-19 version of the
         Queue service. Beginning with this version, all metadata names must adhere to the naming
         conventions for C# identifiers. Default value is None.
        :type metadata: dict[str, str]
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword comp: comp. Default value is "metadata". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        comp = kwargs.pop("comp", _params.pop("comp", "metadata"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_set_metadata_request(
            url=self._config.url,
            timeout=timeout,
            metadata=metadata,
            request_id_parameter=request_id_parameter,
            comp=comp,
            version=self._config.version,
            template_url=self.set_metadata.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    set_metadata.metadata = {"url": "{url}/{queueName}"}  # type: ignore

    @distributed_trace_async
    async def get_access_policy(
        self, timeout: Optional[int] = None, request_id_parameter: Optional[str] = None, **kwargs: Any
    ) -> List[_models.SignedIdentifier]:
        """returns details about any stored access policies specified on the queue that may be used with
        Shared Access Signatures.

        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword comp: comp. Default value is "acl". Note that overriding this default value may result
         in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of SignedIdentifier or the result of cls(response)
        :rtype: list[~azure.storage.queue.models.SignedIdentifier]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        comp = kwargs.pop("comp", _params.pop("comp", "acl"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[List[_models.SignedIdentifier]]

        request = build_get_access_policy_request(
            url=self._config.url,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            comp=comp,
            version=self._config.version,
            template_url=self.get_access_policy.metadata["url"],
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
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        deserialized = self._deserialize("[SignedIdentifier]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get_access_policy.metadata = {"url": "{url}/{queueName}"}  # type: ignore

    @distributed_trace_async
    async def set_access_policy(  # pylint: disable=inconsistent-return-statements
        self,
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        queue_acl: Optional[List[_models.SignedIdentifier]] = None,
        **kwargs: Any
    ) -> None:
        """sets stored access policies for the queue that may be used with Shared Access Signatures.

        :param timeout: The The timeout parameter is expressed in seconds. For more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param queue_acl: the acls for the queue. Default value is None.
        :type queue_acl: list[~azure.storage.queue.models.SignedIdentifier]
        :keyword comp: comp. Default value is "acl". Note that overriding this default value may result
         in unsupported behavior.
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

        comp = kwargs.pop("comp", _params.pop("comp", "acl"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", "application/xml"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        serialization_ctxt = {"xml": {"name": "SignedIdentifiers", "wrapped": True}}
        if queue_acl is not None:
            _content = self._serialize.body(
                queue_acl, "[SignedIdentifier]", is_xml=True, serialization_ctxt=serialization_ctxt
            )
        else:
            _content = None

        request = build_set_access_policy_request(
            url=self._config.url,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            comp=comp,
            content_type=content_type,
            version=self._config.version,
            content=_content,
            template_url=self.set_access_policy.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    set_access_policy.metadata = {"url": "{url}/{queueName}"}  # type: ignore
