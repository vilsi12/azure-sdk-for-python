# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, List, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._digital_twin_models_operations import build_add_request, build_delete_request, build_get_by_id_request, build_list_request, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class DigitalTwinModelsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.digitaltwins.core.aio.AzureDigitalTwinsAPI`'s
        :attr:`digital_twin_models` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")


    @distributed_trace_async
    async def add(
        self,
        models: Optional[List[Any]] = None,
        digital_twin_models_add_options: Optional["_models.DigitalTwinModelsAddOptions"] = None,
        **kwargs: Any
    ) -> List["_models.DigitalTwinsModelData"]:
        """Uploads one or more models. When any error occurs, no models are uploaded.
        Status codes:


        * 201 Created
        * 400 Bad Request

          * DTDLParserError - The models provided are not valid DTDL.
          * InvalidArgument - The model id is invalid.
          * LimitExceeded - The maximum number of model ids allowed in 'dependenciesFor' has been
        reached.
          * ModelVersionNotSupported - The version of DTDL used is not supported.

        * 409 Conflict

          * ModelAlreadyExists - The model provided already exists.

        :param models: An array of models to add. Default value is None.
        :type models: list[any]
        :param digital_twin_models_add_options: Parameter group. Default value is None.
        :type digital_twin_models_add_options:
         ~azure.digitaltwins.core.models.DigitalTwinModelsAddOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of DigitalTwinsModelData, or the result of cls(response)
        :rtype: list[~azure.digitaltwins.core.models.DigitalTwinsModelData]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.DigitalTwinsModelData"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-06-30-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _traceparent = None
        _tracestate = None
        if digital_twin_models_add_options is not None:
            _traceparent = digital_twin_models_add_options.traceparent
            _tracestate = digital_twin_models_add_options.tracestate
        if models is not None:
            _json = self._serialize.body(models, '[object]')
        else:
            _json = None

        request = build_add_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            traceparent=_traceparent,
            tracestate=_tracestate,
            template_url=self.add.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('[DigitalTwinsModelData]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    add.metadata = {'url': "/models"}  # type: ignore


    @distributed_trace
    def list(
        self,
        dependencies_for: Optional[List[str]] = None,
        include_model_definition: Optional[bool] = False,
        digital_twin_models_list_options: Optional["_models.DigitalTwinModelsListOptions"] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PagedDigitalTwinsModelDataCollection"]:
        """Retrieves model metadata and, optionally, model definitions.
        Status codes:


        * 200 OK
        * 400 Bad Request

          * InvalidArgument - The model id is invalid.
          * LimitExceeded - The maximum number of model ids allowed in 'dependenciesFor' has been
        reached.

        * 404 Not Found

          * ModelNotFound - The model was not found.

        :param dependencies_for: The set of the models which will have their dependencies retrieved. If
         omitted, all models are retrieved. Default value is None.
        :type dependencies_for: list[str]
        :param include_model_definition: When true the model definition will be returned as part of the
         result. Default value is False.
        :type include_model_definition: bool
        :param digital_twin_models_list_options: Parameter group. Default value is None.
        :type digital_twin_models_list_options:
         ~azure.digitaltwins.core.models.DigitalTwinModelsListOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PagedDigitalTwinsModelDataCollection or the result
         of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.digitaltwins.core.models.PagedDigitalTwinsModelDataCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2021-06-30-preview")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PagedDigitalTwinsModelDataCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                _traceparent = None
                _tracestate = None
                _max_items_per_page = None
                if digital_twin_models_list_options is not None:
                    _traceparent = digital_twin_models_list_options.traceparent
                    _tracestate = digital_twin_models_list_options.tracestate
                    _max_items_per_page = digital_twin_models_list_options.max_items_per_page
                
                request = build_list_request(
                    api_version=api_version,
                    traceparent=_traceparent,
                    tracestate=_tracestate,
                    dependencies_for=dependencies_for,
                    include_model_definition=include_model_definition,
                    max_items_per_page=_max_items_per_page,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                _traceparent = None
                _tracestate = None
                _max_items_per_page = None
                if digital_twin_models_list_options is not None:
                    _traceparent = digital_twin_models_list_options.traceparent
                    _tracestate = digital_twin_models_list_options.tracestate
                    _max_items_per_page = digital_twin_models_list_options.max_items_per_page
                
                request = build_list_request(
                    api_version=api_version,
                    traceparent=_traceparent,
                    tracestate=_tracestate,
                    dependencies_for=dependencies_for,
                    include_model_definition=include_model_definition,
                    max_items_per_page=_max_items_per_page,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PagedDigitalTwinsModelDataCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/models"}  # type: ignore

    @distributed_trace_async
    async def get_by_id(
        self,
        id: str,
        include_model_definition: Optional[bool] = False,
        digital_twin_models_get_by_id_options: Optional["_models.DigitalTwinModelsGetByIdOptions"] = None,
        **kwargs: Any
    ) -> "_models.DigitalTwinsModelData":
        """Retrieves model metadata and optionally the model definition.
        Status codes:


        * 200 OK
        * 400 Bad Request

          * InvalidArgument - The model id is invalid.
          * MissingArgument - The model id was not provided.

        * 404 Not Found

          * ModelNotFound - The model was not found.

        :param id: The id for the model. The id is globally unique and case sensitive.
        :type id: str
        :param include_model_definition: When true the model definition will be returned as part of the
         result. Default value is False.
        :type include_model_definition: bool
        :param digital_twin_models_get_by_id_options: Parameter group. Default value is None.
        :type digital_twin_models_get_by_id_options:
         ~azure.digitaltwins.core.models.DigitalTwinModelsGetByIdOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DigitalTwinsModelData, or the result of cls(response)
        :rtype: ~azure.digitaltwins.core.models.DigitalTwinsModelData
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DigitalTwinsModelData"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-06-30-preview")  # type: str

        _traceparent = None
        _tracestate = None
        if digital_twin_models_get_by_id_options is not None:
            _traceparent = digital_twin_models_get_by_id_options.traceparent
            _tracestate = digital_twin_models_get_by_id_options.tracestate

        request = build_get_by_id_request(
            id=id,
            api_version=api_version,
            traceparent=_traceparent,
            tracestate=_tracestate,
            include_model_definition=include_model_definition,
            template_url=self.get_by_id.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('DigitalTwinsModelData', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_id.metadata = {'url': "/models/{id}"}  # type: ignore


    @distributed_trace_async
    async def update(  # pylint: disable=inconsistent-return-statements
        self,
        id: str,
        update_model: List[Any],
        digital_twin_models_update_options: Optional["_models.DigitalTwinModelsUpdateOptions"] = None,
        **kwargs: Any
    ) -> None:
        """Updates the metadata for a model.
        Status codes:


        * 204 No Content
        * 400 Bad Request

          * InvalidArgument - The model id is invalid.
          * JsonPatchInvalid - The JSON Patch provided is invalid.
          * MissingArgument - The model id was not provided.

        * 404 Not Found

          * ModelNotFound - The model was not found.

        * 409 Conflict

          * ModelReferencesNotDecommissioned - The model refers to models that are not decommissioned.

        :param id: The id for the model. The id is globally unique and case sensitive.
        :type id: str
        :param update_model: An update specification described by JSON Patch. Only the decommissioned
         property can be replaced.
        :type update_model: list[any]
        :param digital_twin_models_update_options: Parameter group. Default value is None.
        :type digital_twin_models_update_options:
         ~azure.digitaltwins.core.models.DigitalTwinModelsUpdateOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-06-30-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json-patch+json")  # type: Optional[str]

        _traceparent = None
        _tracestate = None
        if digital_twin_models_update_options is not None:
            _traceparent = digital_twin_models_update_options.traceparent
            _tracestate = digital_twin_models_update_options.tracestate
        _json = self._serialize.body(update_model, '[object]')

        request = build_update_request(
            id=id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            traceparent=_traceparent,
            tracestate=_tracestate,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    update.metadata = {'url': "/models/{id}"}  # type: ignore


    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        id: str,
        digital_twin_models_delete_options: Optional["_models.DigitalTwinModelsDeleteOptions"] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a model. A model can only be deleted if no other models reference it.
        Status codes:


        * 204 No Content
        * 400 Bad Request

          * InvalidArgument - The model id is invalid.
          * MissingArgument - The model id was not provided.

        * 404 Not Found

          * ModelNotFound - The model was not found.

        * 409 Conflict

          * ModelReferencesNotDeleted - The model refers to models that are not deleted.

        :param id: The id for the model. The id is globally unique and case sensitive.
        :type id: str
        :param digital_twin_models_delete_options: Parameter group. Default value is None.
        :type digital_twin_models_delete_options:
         ~azure.digitaltwins.core.models.DigitalTwinModelsDeleteOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-06-30-preview")  # type: str

        _traceparent = None
        _tracestate = None
        if digital_twin_models_delete_options is not None:
            _traceparent = digital_twin_models_delete_options.traceparent
            _tracestate = digital_twin_models_delete_options.tracestate

        request = build_delete_request(
            id=id,
            api_version=api_version,
            traceparent=_traceparent,
            tracestate=_tracestate,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': "/models/{id}"}  # type: ignore

