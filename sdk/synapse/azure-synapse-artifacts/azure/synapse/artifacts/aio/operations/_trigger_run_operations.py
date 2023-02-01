# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
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
from ...operations._trigger_run_operations import (
    build_cancel_trigger_instance_request,
    build_query_trigger_runs_by_workspace_request,
    build_rerun_trigger_instance_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class TriggerRunOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.synapse.artifacts.aio.ArtifactsClient`'s
        :attr:`trigger_run` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def rerun_trigger_instance(  # pylint: disable=inconsistent-return-statements
        self, trigger_name: str, run_id: str, **kwargs: Any
    ) -> None:
        """Rerun single trigger instance by runId.

        :param trigger_name: The trigger name. Required.
        :type trigger_name: str
        :param run_id: The pipeline run identifier. Required.
        :type run_id: str
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

        api_version: Literal["2020-12-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_rerun_trigger_instance_request(
            trigger_name=trigger_name,
            run_id=run_id,
            api_version=api_version,
            template_url=self.rerun_trigger_instance.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    rerun_trigger_instance.metadata = {"url": "/triggers/{triggerName}/triggerRuns/{runId}/rerun"}

    @distributed_trace_async
    async def cancel_trigger_instance(  # pylint: disable=inconsistent-return-statements
        self, trigger_name: str, run_id: str, **kwargs: Any
    ) -> None:
        """Cancel single trigger instance by runId.

        :param trigger_name: The trigger name. Required.
        :type trigger_name: str
        :param run_id: The pipeline run identifier. Required.
        :type run_id: str
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

        api_version: Literal["2020-12-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_cancel_trigger_instance_request(
            trigger_name=trigger_name,
            run_id=run_id,
            api_version=api_version,
            template_url=self.cancel_trigger_instance.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    cancel_trigger_instance.metadata = {"url": "/triggers/{triggerName}/triggerRuns/{runId}/cancel"}

    @overload
    async def query_trigger_runs_by_workspace(
        self, filter_parameters: _models.RunFilterParameters, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.TriggerRunsQueryResponse:
        """Query trigger runs.

        :param filter_parameters: Parameters to filter the pipeline run. Required.
        :type filter_parameters: ~azure.synapse.artifacts.models.RunFilterParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TriggerRunsQueryResponse or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.TriggerRunsQueryResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def query_trigger_runs_by_workspace(
        self, filter_parameters: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.TriggerRunsQueryResponse:
        """Query trigger runs.

        :param filter_parameters: Parameters to filter the pipeline run. Required.
        :type filter_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TriggerRunsQueryResponse or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.TriggerRunsQueryResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def query_trigger_runs_by_workspace(
        self, filter_parameters: Union[_models.RunFilterParameters, IO], **kwargs: Any
    ) -> _models.TriggerRunsQueryResponse:
        """Query trigger runs.

        :param filter_parameters: Parameters to filter the pipeline run. Is either a model type or a IO
         type. Required.
        :type filter_parameters: ~azure.synapse.artifacts.models.RunFilterParameters or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TriggerRunsQueryResponse or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.TriggerRunsQueryResponse
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

        api_version: Literal["2020-12-01"] = kwargs.pop("api_version", _params.pop("api-version", "2020-12-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.TriggerRunsQueryResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(filter_parameters, (IO, bytes)):
            _content = filter_parameters
        else:
            _json = self._serialize.body(filter_parameters, "RunFilterParameters")

        request = build_query_trigger_runs_by_workspace_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.query_trigger_runs_by_workspace.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("TriggerRunsQueryResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    query_trigger_runs_by_workspace.metadata = {"url": "/queryTriggerRuns"}
