# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Iterable, Iterator, Optional, TypeVar, cast
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from ..rest import schema as rest_schema, schema_groups as rest_schema_groups

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class SchemaGroupsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.schemaregistry._generated.AzureSchemaRegistry`'s
        :attr:`schema_groups` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    def list(self, **kwargs: Any) -> Iterable[str]:
        """Get list of schema groups.

        Gets the list of schema groups user is authorized to access.

        :return: An iterator like instance of str
        :rtype: ~azure.core.paging.ItemPaged[str]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == "str"  # Optional.
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = rest_schema_groups.build_list_request(
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

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
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

            return request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = deserialized["schemaGroups"]
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.get("nextLink", None), iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)


class SchemaOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.schemaregistry._generated.AzureSchemaRegistry`'s
        :attr:`schema` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    def get_by_id(self, id: str, **kwargs: Any) -> Iterator[bytes]:
        """Get a registered schema by its unique ID reference.

        Gets a registered schema by its unique ID.  Azure Schema Registry guarantees that ID is unique
        within a namespace. Operation response type is based on serialization of schema requested.

        :param id: References specific schema in registry namespace. Required.
        :type id: str
        :return: Iterator of the response bytes
        :rtype: Iterator[bytes]
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
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[Iterator[bytes]]

        request = rest_schema.build_get_by_id_request(
            id=id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=True, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        if response.status_code == 200:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Content-Type"] = self._deserialize("str", response.headers.get("Content-Type"))
            response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
            response_headers["Schema-Id-Location"] = self._deserialize(
                "str", response.headers.get("Schema-Id-Location")
            )
            response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
            response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
            response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

            deserialized = response.iter_bytes()

        if response.status_code == 200:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Content-Type"] = self._deserialize("str", response.headers.get("Content-Type"))
            response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
            response_headers["Schema-Id-Location"] = self._deserialize(
                "str", response.headers.get("Schema-Id-Location")
            )
            response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
            response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
            response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

            deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, cast(Iterator[bytes], deserialized), response_headers)

        return cast(Iterator[bytes], deserialized)

    def get_versions(self, group_name: str, schema_name: str, **kwargs: Any) -> Iterable[int]:
        """Get list schema versions.

        Gets the list of all versions of one schema.

        :param group_name: Schema group under which schema is registered.  Group's serialization type
         should match the serialization type specified in the request. Required.
        :type group_name: str
        :param schema_name: Name of schema. Required.
        :type schema_name: str
        :return: An iterator like instance of int
        :rtype: ~azure.core.paging.ItemPaged[int]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == 0  # Optional.
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = rest_schema.build_get_versions_request(
                    group_name=group_name,
                    schema_name=schema_name,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

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
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

            return request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = deserialized["schemaVersions"]
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.get("nextLink", None), iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    def get_schema_version(
        self, group_name: str, schema_name: str, schema_version: int, **kwargs: Any
    ) -> Iterator[bytes]:
        """Get specific schema versions.

        Gets one specific version of one schema.

        :param group_name: Schema group under which schema is registered.  Group's serialization type
         should match the serialization type specified in the request. Required.
        :type group_name: str
        :param schema_name: Name of schema. Required.
        :type schema_name: str
        :param schema_version: Version number of specific schema. Required.
        :type schema_version: int
        :return: Iterator of the response bytes
        :rtype: Iterator[bytes]
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
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[Iterator[bytes]]

        request = rest_schema.build_get_schema_version_request(
            group_name=group_name,
            schema_name=schema_name,
            schema_version=schema_version,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=True, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        if response.status_code == 200:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Content-Type"] = self._deserialize("str", response.headers.get("Content-Type"))
            response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
            response_headers["Schema-Id-Location"] = self._deserialize(
                "str", response.headers.get("Schema-Id-Location")
            )
            response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
            response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
            response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

            deserialized = response.iter_bytes()

        if response.status_code == 200:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Content-Type"] = self._deserialize("str", response.headers.get("Content-Type"))
            response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
            response_headers["Schema-Id-Location"] = self._deserialize(
                "str", response.headers.get("Schema-Id-Location")
            )
            response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
            response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
            response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

            deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, cast(Iterator[bytes], deserialized), response_headers)

        return cast(Iterator[bytes], deserialized)

    def query_id_by_content(  # pylint: disable=inconsistent-return-statements
        self, group_name: str, schema_name: str, schema_content: IO, **kwargs: Any
    ) -> None:
        """Get ID for existing schema.

        Gets the ID referencing an existing schema within the specified schema group, as matched by
        schema content comparison.

        :param group_name: Schema group under which schema is registered.  Group's serialization type
         should match the serialization type specified in the request. Required.
        :type group_name: str
        :param schema_name: Name of schema. Required.
        :type schema_name: str
        :param schema_content: String representation (UTF-8) of the registered schema. Required.
        :type schema_content: IO
        :return: None
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

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/json; serialization=Avro")
        )  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _content = schema_content

        request = rest_schema.build_query_id_by_content_request(
            group_name=group_name,
            schema_name=schema_name,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
        response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
        response_headers["Schema-Id-Location"] = self._deserialize("str", response.headers.get("Schema-Id-Location"))
        response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
        response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
        response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    def register(  # pylint: disable=inconsistent-return-statements
        self, group_name: str, schema_name: str, schema_content: IO, **kwargs: Any
    ) -> None:
        """Register new schema.

        Register new schema. If schema of specified name does not exist in specified group, schema is
        created at version 1. If schema of specified name exists already in specified group, schema is
        created at latest version + 1.

        :param group_name: Schema group under which schema should be registered.  Group's serialization
         type should match the serialization type specified in the request. Required.
        :type group_name: str
        :param schema_name: Name of schema. Required.
        :type schema_name: str
        :param schema_content: String representation (UTF-8) of the schema being registered. Required.
        :type schema_content: IO
        :return: None
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

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/json; serialization=Avro")
        )  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _content = schema_content

        request = rest_schema.build_register_request(
            group_name=group_name,
            schema_name=schema_name,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
        response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
        response_headers["Schema-Id-Location"] = self._deserialize("str", response.headers.get("Schema-Id-Location"))
        response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
        response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
        response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

        if cls:
            return cls(pipeline_response, None, response_headers)
