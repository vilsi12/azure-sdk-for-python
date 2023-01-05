# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, List, Optional, TypeVar

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
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._cognitive_services_management_client_operations import (
    build_check_domain_availability_request,
    build_check_sku_availability_request,
)
from .._vendor import CognitiveServicesManagementClientMixinABC

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class CognitiveServicesManagementClientOperationsMixin(CognitiveServicesManagementClientMixinABC):
    @distributed_trace_async
    async def check_sku_availability(
        self, location: str, skus: List[str], kind: str, type: str, **kwargs: Any
    ) -> _models.SkuAvailabilityListResult:
        """Check available SKUs.

        :param location: Resource location. Required.
        :type location: str
        :param skus: The SKU of the resource. Required.
        :type skus: list[str]
        :param kind: The Kind of the resource. Required.
        :type kind: str
        :param type: The Type of the resource. Required.
        :type type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SkuAvailabilityListResult or the result of cls(response)
        :rtype: ~azure.mgmt.cognitiveservices.models.SkuAvailabilityListResult
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

        api_version: Literal["2022-12-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[_models.SkuAvailabilityListResult] = kwargs.pop("cls", None)

        _parameters = _models.CheckSkuAvailabilityParameter(kind=kind, skus=skus, type=type)
        _json = self._serialize.body(_parameters, "CheckSkuAvailabilityParameter")

        request = build_check_sku_availability_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.check_sku_availability.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SkuAvailabilityListResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_sku_availability.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.CognitiveServices/locations/{location}/checkSkuAvailability"
    }

    @distributed_trace_async
    async def check_domain_availability(
        self, subdomain_name: str, type: str, kind: Optional[str] = None, **kwargs: Any
    ) -> _models.DomainAvailability:
        """Check whether a domain is available.

        :param subdomain_name: The subdomain name to use. Required.
        :type subdomain_name: str
        :param type: The Type of the resource. Required.
        :type type: str
        :param kind: The Kind of the resource. Default value is None.
        :type kind: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DomainAvailability or the result of cls(response)
        :rtype: ~azure.mgmt.cognitiveservices.models.DomainAvailability
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

        api_version: Literal["2022-12-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[_models.DomainAvailability] = kwargs.pop("cls", None)

        _parameters = _models.CheckDomainAvailabilityParameter(kind=kind, subdomain_name=subdomain_name, type=type)
        _json = self._serialize.body(_parameters, "CheckDomainAvailabilityParameter")

        request = build_check_domain_availability_request(
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.check_domain_availability.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("DomainAvailability", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_domain_availability.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.CognitiveServices/checkDomainAvailability"
    }
