# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, overload
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
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    resource_group_name: str,
    integration_account_name: str,
    subscription_id: str,
    *,
    top: Optional[int] = None,
    filter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-05-01"))  # type: Literal["2019-05-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "integrationAccountName": _SERIALIZER.url("integration_account_name", integration_account_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if top is not None:
        _params["$top"] = _SERIALIZER.query("top", top, "int")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str, integration_account_name: str, map_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-05-01"))  # type: Literal["2019-05-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "integrationAccountName": _SERIALIZER.url("integration_account_name", integration_account_name, "str"),
        "mapName": _SERIALIZER.url("map_name", map_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_or_update_request(
    resource_group_name: str, integration_account_name: str, map_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-05-01"))  # type: Literal["2019-05-01"]
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "integrationAccountName": _SERIALIZER.url("integration_account_name", integration_account_name, "str"),
        "mapName": _SERIALIZER.url("map_name", map_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    resource_group_name: str, integration_account_name: str, map_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-05-01"))  # type: Literal["2019-05-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "integrationAccountName": _SERIALIZER.url("integration_account_name", integration_account_name, "str"),
        "mapName": _SERIALIZER.url("map_name", map_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_content_callback_url_request(
    resource_group_name: str, integration_account_name: str, map_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-05-01"))  # type: Literal["2019-05-01"]
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName}/listContentCallbackUrl",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "integrationAccountName": _SERIALIZER.url("integration_account_name", integration_account_name, "str"),
        "mapName": _SERIALIZER.url("map_name", map_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class IntegrationAccountMapsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.logic.LogicManagementClient`'s
        :attr:`integration_account_maps` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        integration_account_name: str,
        top: Optional[int] = None,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.IntegrationAccountMap"]:
        """Gets a list of integration account maps.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param integration_account_name: The integration account name. Required.
        :type integration_account_name: str
        :param top: The number of items to be included in the result. Default value is None.
        :type top: int
        :param filter: The filter to apply on the operation. Options for filters include: MapType.
         Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either IntegrationAccountMap or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.logic.models.IntegrationAccountMap]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2019-05-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.IntegrationAccountMapListResult]

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
                    integration_account_name=integration_account_name,
                    subscription_id=self._config.subscription_id,
                    top=top,
                    filter=filter,
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize("IntegrationAccountMapListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps"}  # type: ignore

    @distributed_trace
    def get(
        self, resource_group_name: str, integration_account_name: str, map_name: str, **kwargs: Any
    ) -> _models.IntegrationAccountMap:
        """Gets an integration account map.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param integration_account_name: The integration account name. Required.
        :type integration_account_name: str
        :param map_name: The integration account map name. Required.
        :type map_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IntegrationAccountMap or the result of cls(response)
        :rtype: ~azure.mgmt.logic.models.IntegrationAccountMap
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
        )  # type: Literal["2019-05-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.IntegrationAccountMap]

        request = build_get_request(
            resource_group_name=resource_group_name,
            integration_account_name=integration_account_name,
            map_name=map_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("IntegrationAccountMap", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName}"}  # type: ignore

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        integration_account_name: str,
        map_name: str,
        map: _models.IntegrationAccountMap,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.IntegrationAccountMap:
        """Creates or updates an integration account map. If the map is larger than 4 MB, you need to
        store the map in an Azure blob and use the blob's Shared Access Signature (SAS) URL as the
        'contentLink' property value.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param integration_account_name: The integration account name. Required.
        :type integration_account_name: str
        :param map_name: The integration account map name. Required.
        :type map_name: str
        :param map: The integration account map. Required.
        :type map: ~azure.mgmt.logic.models.IntegrationAccountMap
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IntegrationAccountMap or the result of cls(response)
        :rtype: ~azure.mgmt.logic.models.IntegrationAccountMap
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        integration_account_name: str,
        map_name: str,
        map: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.IntegrationAccountMap:
        """Creates or updates an integration account map. If the map is larger than 4 MB, you need to
        store the map in an Azure blob and use the blob's Shared Access Signature (SAS) URL as the
        'contentLink' property value.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param integration_account_name: The integration account name. Required.
        :type integration_account_name: str
        :param map_name: The integration account map name. Required.
        :type map_name: str
        :param map: The integration account map. Required.
        :type map: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IntegrationAccountMap or the result of cls(response)
        :rtype: ~azure.mgmt.logic.models.IntegrationAccountMap
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        resource_group_name: str,
        integration_account_name: str,
        map_name: str,
        map: Union[_models.IntegrationAccountMap, IO],
        **kwargs: Any
    ) -> _models.IntegrationAccountMap:
        """Creates or updates an integration account map. If the map is larger than 4 MB, you need to
        store the map in an Azure blob and use the blob's Shared Access Signature (SAS) URL as the
        'contentLink' property value.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param integration_account_name: The integration account name. Required.
        :type integration_account_name: str
        :param map_name: The integration account map name. Required.
        :type map_name: str
        :param map: The integration account map. Is either a model type or a IO type. Required.
        :type map: ~azure.mgmt.logic.models.IntegrationAccountMap or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IntegrationAccountMap or the result of cls(response)
        :rtype: ~azure.mgmt.logic.models.IntegrationAccountMap
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
        )  # type: Literal["2019-05-01"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.IntegrationAccountMap]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(map, (IO, bytes)):
            _content = map
        else:
            _json = self._serialize.body(map, "IntegrationAccountMap")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            integration_account_name=integration_account_name,
            map_name=map_name,
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

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("IntegrationAccountMap", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("IntegrationAccountMap", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName}"}  # type: ignore

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, integration_account_name: str, map_name: str, **kwargs: Any
    ) -> None:
        """Deletes an integration account map.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param integration_account_name: The integration account name. Required.
        :type integration_account_name: str
        :param map_name: The integration account map name. Required.
        :type map_name: str
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
        )  # type: Literal["2019-05-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            integration_account_name=integration_account_name,
            map_name=map_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName}"}  # type: ignore

    @overload
    def list_content_callback_url(
        self,
        resource_group_name: str,
        integration_account_name: str,
        map_name: str,
        list_content_callback_url: _models.GetCallbackUrlParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.WorkflowTriggerCallbackUrl:
        """Get the content callback url.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param integration_account_name: The integration account name. Required.
        :type integration_account_name: str
        :param map_name: The integration account map name. Required.
        :type map_name: str
        :param list_content_callback_url: Required.
        :type list_content_callback_url: ~azure.mgmt.logic.models.GetCallbackUrlParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkflowTriggerCallbackUrl or the result of cls(response)
        :rtype: ~azure.mgmt.logic.models.WorkflowTriggerCallbackUrl
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def list_content_callback_url(
        self,
        resource_group_name: str,
        integration_account_name: str,
        map_name: str,
        list_content_callback_url: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.WorkflowTriggerCallbackUrl:
        """Get the content callback url.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param integration_account_name: The integration account name. Required.
        :type integration_account_name: str
        :param map_name: The integration account map name. Required.
        :type map_name: str
        :param list_content_callback_url: Required.
        :type list_content_callback_url: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkflowTriggerCallbackUrl or the result of cls(response)
        :rtype: ~azure.mgmt.logic.models.WorkflowTriggerCallbackUrl
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def list_content_callback_url(
        self,
        resource_group_name: str,
        integration_account_name: str,
        map_name: str,
        list_content_callback_url: Union[_models.GetCallbackUrlParameters, IO],
        **kwargs: Any
    ) -> _models.WorkflowTriggerCallbackUrl:
        """Get the content callback url.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param integration_account_name: The integration account name. Required.
        :type integration_account_name: str
        :param map_name: The integration account map name. Required.
        :type map_name: str
        :param list_content_callback_url: Is either a model type or a IO type. Required.
        :type list_content_callback_url: ~azure.mgmt.logic.models.GetCallbackUrlParameters or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkflowTriggerCallbackUrl or the result of cls(response)
        :rtype: ~azure.mgmt.logic.models.WorkflowTriggerCallbackUrl
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
        )  # type: Literal["2019-05-01"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.WorkflowTriggerCallbackUrl]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(list_content_callback_url, (IO, bytes)):
            _content = list_content_callback_url
        else:
            _json = self._serialize.body(list_content_callback_url, "GetCallbackUrlParameters")

        request = build_list_content_callback_url_request(
            resource_group_name=resource_group_name,
            integration_account_name=integration_account_name,
            map_name=map_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.list_content_callback_url.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("WorkflowTriggerCallbackUrl", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_content_callback_url.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName}/listContentCallbackUrl"}  # type: ignore
