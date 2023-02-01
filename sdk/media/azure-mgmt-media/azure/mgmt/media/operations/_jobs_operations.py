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
    account_name: str,
    transform_name: str,
    subscription_id: str,
    *,
    filter: Optional[str] = None,
    orderby: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-07-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "transformName": _SERIALIZER.url("transform_name", transform_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if orderby is not None:
        _params["$orderby"] = _SERIALIZER.query("orderby", orderby, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str, account_name: str, transform_name: str, job_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-07-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "transformName": _SERIALIZER.url("transform_name", transform_name, "str"),
        "jobName": _SERIALIZER.url("job_name", job_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_request(
    resource_group_name: str, account_name: str, transform_name: str, job_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-07-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "transformName": _SERIALIZER.url("transform_name", transform_name, "str"),
        "jobName": _SERIALIZER.url("job_name", job_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    resource_group_name: str, account_name: str, transform_name: str, job_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-07-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "transformName": _SERIALIZER.url("transform_name", transform_name, "str"),
        "jobName": _SERIALIZER.url("job_name", job_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_update_request(
    resource_group_name: str, account_name: str, transform_name: str, job_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-07-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "transformName": _SERIALIZER.url("transform_name", transform_name, "str"),
        "jobName": _SERIALIZER.url("job_name", job_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, params=_params, headers=_headers, **kwargs)


def build_cancel_job_request(
    resource_group_name: str, account_name: str, transform_name: str, job_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-07-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName}/cancelJob",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "accountName": _SERIALIZER.url("account_name", account_name, "str"),
        "transformName": _SERIALIZER.url("transform_name", transform_name, "str"),
        "jobName": _SERIALIZER.url("job_name", job_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class JobsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.media.AzureMediaServices`'s
        :attr:`jobs` attribute.
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
        account_name: str,
        transform_name: str,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.Job"]:
        """List Jobs.

        Lists all of the Jobs for the Transform.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param transform_name: The Transform name. Required.
        :type transform_name: str
        :param filter: Restricts the set of items returned. Default value is None.
        :type filter: str
        :param orderby: Specifies the key by which the result collection should be ordered. Default
         value is None.
        :type orderby: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Job or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.media.models.Job]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-07-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
        cls: ClsType[_models.JobCollection] = kwargs.pop("cls", None)

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
                    account_name=account_name,
                    transform_name=transform_name,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    orderby=orderby,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("JobCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.odata_next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs"
    }

    @distributed_trace
    def get(
        self, resource_group_name: str, account_name: str, transform_name: str, job_name: str, **kwargs: Any
    ) -> _models.Job:
        """Get Job.

        Gets a Job.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param transform_name: The Transform name. Required.
        :type transform_name: str
        :param job_name: The Job name. Required.
        :type job_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Job or the result of cls(response)
        :rtype: ~azure.mgmt.media.models.Job
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

        api_version: Literal["2022-07-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
        cls: ClsType[_models.Job] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            transform_name=transform_name,
            job_name=job_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Job", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName}"
    }

    @overload
    def create(
        self,
        resource_group_name: str,
        account_name: str,
        transform_name: str,
        job_name: str,
        parameters: _models.Job,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Job:
        """Create Job.

        Creates a Job.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param transform_name: The Transform name. Required.
        :type transform_name: str
        :param job_name: The Job name. Required.
        :type job_name: str
        :param parameters: The request parameters. Required.
        :type parameters: ~azure.mgmt.media.models.Job
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Job or the result of cls(response)
        :rtype: ~azure.mgmt.media.models.Job
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self,
        resource_group_name: str,
        account_name: str,
        transform_name: str,
        job_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Job:
        """Create Job.

        Creates a Job.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param transform_name: The Transform name. Required.
        :type transform_name: str
        :param job_name: The Job name. Required.
        :type job_name: str
        :param parameters: The request parameters. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Job or the result of cls(response)
        :rtype: ~azure.mgmt.media.models.Job
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create(
        self,
        resource_group_name: str,
        account_name: str,
        transform_name: str,
        job_name: str,
        parameters: Union[_models.Job, IO],
        **kwargs: Any
    ) -> _models.Job:
        """Create Job.

        Creates a Job.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param transform_name: The Transform name. Required.
        :type transform_name: str
        :param job_name: The Job name. Required.
        :type job_name: str
        :param parameters: The request parameters. Is either a model type or a IO type. Required.
        :type parameters: ~azure.mgmt.media.models.Job or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Job or the result of cls(response)
        :rtype: ~azure.mgmt.media.models.Job
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

        api_version: Literal["2022-07-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Job] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "Job")

        request = build_create_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            transform_name=transform_name,
            job_name=job_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Job", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName}"
    }

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, account_name: str, transform_name: str, job_name: str, **kwargs: Any
    ) -> None:
        """Delete Job.

        Deletes a Job.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param transform_name: The Transform name. Required.
        :type transform_name: str
        :param job_name: The Job name. Required.
        :type job_name: str
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

        api_version: Literal["2022-07-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            transform_name=transform_name,
            job_name=job_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName}"
    }

    @overload
    def update(
        self,
        resource_group_name: str,
        account_name: str,
        transform_name: str,
        job_name: str,
        parameters: _models.Job,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Job:
        """Update Job.

        Update is only supported for description and priority. Updating Priority will take effect when
        the Job state is Queued or Scheduled and depending on the timing the priority update may be
        ignored.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param transform_name: The Transform name. Required.
        :type transform_name: str
        :param job_name: The Job name. Required.
        :type job_name: str
        :param parameters: The request parameters. Required.
        :type parameters: ~azure.mgmt.media.models.Job
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Job or the result of cls(response)
        :rtype: ~azure.mgmt.media.models.Job
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self,
        resource_group_name: str,
        account_name: str,
        transform_name: str,
        job_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Job:
        """Update Job.

        Update is only supported for description and priority. Updating Priority will take effect when
        the Job state is Queued or Scheduled and depending on the timing the priority update may be
        ignored.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param transform_name: The Transform name. Required.
        :type transform_name: str
        :param job_name: The Job name. Required.
        :type job_name: str
        :param parameters: The request parameters. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Job or the result of cls(response)
        :rtype: ~azure.mgmt.media.models.Job
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def update(
        self,
        resource_group_name: str,
        account_name: str,
        transform_name: str,
        job_name: str,
        parameters: Union[_models.Job, IO],
        **kwargs: Any
    ) -> _models.Job:
        """Update Job.

        Update is only supported for description and priority. Updating Priority will take effect when
        the Job state is Queued or Scheduled and depending on the timing the priority update may be
        ignored.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param transform_name: The Transform name. Required.
        :type transform_name: str
        :param job_name: The Job name. Required.
        :type job_name: str
        :param parameters: The request parameters. Is either a model type or a IO type. Required.
        :type parameters: ~azure.mgmt.media.models.Job or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Job or the result of cls(response)
        :rtype: ~azure.mgmt.media.models.Job
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

        api_version: Literal["2022-07-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Job] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "Job")

        request = build_update_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            transform_name=transform_name,
            job_name=job_name,
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

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Job", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName}"
    }

    @distributed_trace
    def cancel_job(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, account_name: str, transform_name: str, job_name: str, **kwargs: Any
    ) -> None:
        """Cancel Job.

        Cancel a Job.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param transform_name: The Transform name. Required.
        :type transform_name: str
        :param job_name: The Job name. Required.
        :type job_name: str
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

        api_version: Literal["2022-07-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-07-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_cancel_job_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            transform_name=transform_name,
            job_name=job_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.cancel_job.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    cancel_job.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName}/cancelJob"
    }
