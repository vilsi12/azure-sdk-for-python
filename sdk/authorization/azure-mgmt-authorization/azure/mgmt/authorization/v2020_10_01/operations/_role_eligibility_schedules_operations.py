# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar
from urllib.parse import parse_qs, urljoin, urlparse

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
from ..._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(scope: str, role_eligibility_schedule_name: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-10-01"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/{scope}/providers/Microsoft.Authorization/roleEligibilitySchedules/{roleEligibilityScheduleName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str", skip_quote=True),
        "roleEligibilityScheduleName": _SERIALIZER.url(
            "role_eligibility_schedule_name", role_eligibility_schedule_name, "str"
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_for_scope_request(scope: str, *, filter: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-10-01"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Authorization/roleEligibilitySchedules")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str", skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class RoleEligibilitySchedulesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.authorization.v2020_10_01.AuthorizationManagementClient`'s
        :attr:`role_eligibility_schedules` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get(self, scope: str, role_eligibility_schedule_name: str, **kwargs: Any) -> _models.RoleEligibilitySchedule:
        """Get the specified role eligibility schedule for a resource scope.

        :param scope: The scope of the role eligibility schedule. Required.
        :type scope: str
        :param role_eligibility_schedule_name: The name (guid) of the role eligibility schedule to get.
         Required.
        :type role_eligibility_schedule_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleEligibilitySchedule or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2020_10_01.models.RoleEligibilitySchedule
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-10-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.RoleEligibilitySchedule]

        request = build_get_request(
            scope=scope,
            role_eligibility_schedule_name=role_eligibility_schedule_name,
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("RoleEligibilitySchedule", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/roleEligibilitySchedules/{roleEligibilityScheduleName}"}  # type: ignore

    @distributed_trace
    def list_for_scope(
        self, scope: str, filter: Optional[str] = None, **kwargs: Any
    ) -> Iterable["_models.RoleEligibilitySchedule"]:
        """Gets role eligibility schedules for a resource scope.

        :param scope: The scope of the role eligibility schedules. Required.
        :type scope: str
        :param filter: The filter to apply on the operation. Use $filter=atScope() to return all role
         eligibility schedules at or above the scope. Use $filter=principalId eq {id} to return all role
         eligibility schedules at, above or below the scope for the specified principal. Use
         $filter=assignedTo('{userId}') to return all role eligibility schedules for the user. Use
         $filter=asTarget() to return all role eligibility schedules created for the current user.
         Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either RoleEligibilitySchedule or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.authorization.v2020_10_01.models.RoleEligibilitySchedule]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-10-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.RoleEligibilityScheduleListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_for_scope_request(
                    scope=scope,
                    filter=filter,
                    api_version=api_version,
                    template_url=self.list_for_scope.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urlparse(next_link)
                _next_request_params = case_insensitive_dict(parse_qs(_parsed_next_link.query))
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest("GET", urljoin(next_link, _parsed_next_link.path), params=_next_request_params)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("RoleEligibilityScheduleListResult", pipeline_response)
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
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_for_scope.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/roleEligibilitySchedules"}  # type: ignore
