# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.polling.base_polling import LROBasePolling

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class DocumentTranslationOperations(object):
    """DocumentTranslationOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.ai.documenttranslation.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def _submit_batch_request_initial(
        self,
        inputs,  # type: List["_models.BatchRequest"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            400: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            429: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            503: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))

        _body = _models.BatchSubmissionRequest(inputs=inputs)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._submit_batch_request_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if _body is not None:
            body_content = self._serialize.body(_body, 'BatchSubmissionRequest')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['Operation-Location']=self._deserialize('str', response.headers.get('Operation-Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    _submit_batch_request_initial.metadata = {'url': '/batches'}  # type: ignore

    def begin_submit_batch_request(
        self,
        inputs,  # type: List["_models.BatchRequest"]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """Submit a document translation request to the Document Translation service.

        Use this API to submit a bulk (batch) translation request to the Document Translation service.
        Each request can contain multiple documents and must contain a source and destination container
        for each document.

        The prefix and suffix filter (if supplied) are used to filter folders. The prefix is applied to
        the subpath after the container name.

        Glossaries / Translation memory can be included in the request and are applied by the service
        when the document is translated.

        If the glossary is invalid or unreachable during translation, an error is indicated in the
        document status.
        If a file with the same name already exists at the destination, it will be overwritten. The
        targetUrl for each target language must be unique.

        :param inputs: The input list of documents or folders containing documents.
        :type inputs: list[~azure.ai.documenttranslation.models.BatchRequest]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the LROBasePolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', False)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._submit_batch_request_initial(
                inputs=inputs,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        if polling is True: polling_method = LROBasePolling(lro_delay, lro_options={'final-state-via': 'location'}, path_format_arguments=path_format_arguments,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_submit_batch_request.metadata = {'url': '/batches'}  # type: ignore

    def get_operations(
        self,
        top=50,  # type: Optional[int]
        skip=0,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.BatchStatusResponse"]
        """Returns a list of batch requests submitted and the status for each request.

        Returns a list of batch requests submitted and the status for each request.
        This list only contains batch requests submitted by the user (based on the subscription). The
        status for each request is sorted by id.

        If the number of requests exceeds our paging limit, server-side paging is used. Paginated
        responses indicate a partial result and include a continuation token in the response.
        The absence of a continuation token means that no additional pages are available.

        $top and $skip query parameters can be used to specify a number of results to return and an
        offset for the collection.

        The server honors the values specified by the client. However, clients must be prepared to
        handle responses that contain a different page size or contain a continuation token.

        When both $top and $skip are included, the server should first apply $skip and then $top on the
        collection.
        Note: If the server can't honor $top and/or $skip, the server must return an error to the
        client informing about it instead of just ignoring the query options.
        This reduces the risk of the client making assumptions about the data returned.

        :param top: Take the $top entries in the collection
         When both $top and $skip are supplied, $skip is applied first.
        :type top: int
        :param skip: Skip the $skip entries in the collection
         When both $top and $skip are supplied, $skip is applied first.
        :type skip: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BatchStatusResponse or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.ai.documenttranslation.models.BatchStatusResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BatchStatusResponse"]
        error_map = {
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            400: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            429: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            503: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.get_operations.metadata['url']  # type: ignore
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int', maximum=100, minimum=1)
                if skip is not None:
                    query_parameters['$skip'] = self._serialize.query("skip", skip, 'int', maximum=2147483647, minimum=0)

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('BatchStatusResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_operations.metadata = {'url': '/batches'}  # type: ignore

    def get_document_status(
        self,
        id,  # type: str
        document_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DocumentStatusDetail"
        """Returns the status for a specific document.

        Returns the translation status for a specific document based on the request Id and document Id.

        :param id: Format - uuid.  The batch id.
        :type id: str
        :param document_id: Format - uuid.  The document id.
        :type document_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DocumentStatusDetail, or the result of cls(response)
        :rtype: ~azure.ai.documenttranslation.models.DocumentStatusDetail
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DocumentStatusDetail"]
        error_map = {
            409: ResourceExistsError,
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            404: lambda response: ResourceNotFoundError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            429: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            503: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_document_status.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'id': self._serialize.url("id", id, 'str'),
            'documentId': self._serialize.url("document_id", document_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
        response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))
        deserialized = self._deserialize('DocumentStatusDetail', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_document_status.metadata = {'url': '/batches/{id}/documents/{documentId}'}  # type: ignore

    def get_operation_status(
        self,
        id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.BatchStatusDetail"
        """Returns the status for a document translation request.

        Returns the status for a document translation request.
        The status includes the overall request status, as well as the status for documents that are
        being translated as part of that request.

        :param id: Format - uuid.  The operation id.
        :type id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BatchStatusDetail, or the result of cls(response)
        :rtype: ~azure.ai.documenttranslation.models.BatchStatusDetail
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BatchStatusDetail"]
        error_map = {
            409: ResourceExistsError,
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            404: lambda response: ResourceNotFoundError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            429: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            503: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_operation_status.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'id': self._serialize.url("id", id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
        response_headers['ETag']=self._deserialize('str', response.headers.get('ETag'))
        deserialized = self._deserialize('BatchStatusDetail', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_operation_status.metadata = {'url': '/batches/{id}'}  # type: ignore

    def cancel_operation(
        self,
        id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.BatchStatusDetail"
        """Cancel a currently processing or queued operation.

        Cancel a currently processing or queued operation.
        Cancel a currently processing or queued operation.
        An operation will not be cancelled if it is already completed or failed or cancelling. A bad
        request will be returned.
        All documents that have completed translation will not be cancelled and will be charged.
        All pending documents will be cancelled if possible.

        :param id: Format - uuid.  The operation-id.
        :type id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BatchStatusDetail, or the result of cls(response)
        :rtype: ~azure.ai.documenttranslation.models.BatchStatusDetail
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BatchStatusDetail"]
        error_map = {
            409: ResourceExistsError,
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            404: lambda response: ResourceNotFoundError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            429: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            503: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.cancel_operation.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'id': self._serialize.url("id", id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('BatchStatusDetail', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    cancel_operation.metadata = {'url': '/batches/{id}'}  # type: ignore

    def get_operation_documents_status(
        self,
        id,  # type: str
        top=50,  # type: Optional[int]
        skip=0,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.DocumentStatusResponse"]
        """Returns the status for all documents in a batch document translation request.

        Returns the status for all documents in a batch document translation request.

        The documents included in the response are sorted by document Id in descending order. If the
        number of documents in the response exceeds our paging limit, server-side paging is used.
        Paginated responses indicate a partial result and include a continuation token in the response.
        The absence of a continuation token means that no additional pages are available.

        $top and $skip query parameters can be used to specify a number of results to return and an
        offset for the collection.
        The server honors the values specified by the client. However, clients must be prepared to
        handle responses that contain a different page size or contain a continuation token.

        When both $top and $skip are included, the server should first apply $skip and then $top on the
        collection.
        Note: If the server can't honor $top and/or $skip, the server must return an error to the
        client informing about it instead of just ignoring the query options.
        This reduces the risk of the client making assumptions about the data returned.

        :param id: Format - uuid.  The operation id.
        :type id: str
        :param top: Take the $top entries in the collection
         When both $top and $skip are supplied, $skip is applied first.
        :type top: int
        :param skip: Skip the $skip entries in the collection
         When both $top and $skip are supplied, $skip is applied first.
        :type skip: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DocumentStatusResponse or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.ai.documenttranslation.models.DocumentStatusResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DocumentStatusResponse"]
        error_map = {
            409: ResourceExistsError,
            400: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            401: lambda response: ClientAuthenticationError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            404: lambda response: ResourceNotFoundError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            429: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            503: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.get_operation_documents_status.metadata['url']  # type: ignore
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'id': self._serialize.url("id", id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int', maximum=100, minimum=1)
                if skip is not None:
                    query_parameters['$skip'] = self._serialize.query("skip", skip, 'int', maximum=2147483647, minimum=0)

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'id': self._serialize.url("id", id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('DocumentStatusResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_operation_documents_status.metadata = {'url': '/batches/{id}/documents'}  # type: ignore

    def get_document_formats(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.FileFormatListResult"
        """Returns a list of supported document formats.

        The list of supported document formats supported by the Document Translation service.
        The list includes the common file extension, as well as the content-type if using the upload
        API.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileFormatListResult, or the result of cls(response)
        :rtype: ~azure.ai.documenttranslation.models.FileFormatListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FileFormatListResult"]
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            429: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            503: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_document_formats.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('FileFormatListResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_document_formats.metadata = {'url': '/documents/formats'}  # type: ignore

    def get_glossary_formats(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.FileFormatListResult"
        """Returns the list of supported glossary formats.

        The list of supported glossary formats supported by the Document Translation service.
        The list includes the common file extension used.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileFormatListResult, or the result of cls(response)
        :rtype: ~azure.ai.documenttranslation.models.FileFormatListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FileFormatListResult"]
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            429: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            503: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_glossary_formats.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('FileFormatListResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_glossary_formats.metadata = {'url': '/glossaries/formats'}  # type: ignore

    def get_document_storage_source(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.StorageSourceListResult"
        """Returns a list of supported storage sources.

        Returns a list of storage sources/options supported by the Document Translation service.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageSourceListResult, or the result of cls(response)
        :rtype: ~azure.ai.documenttranslation.models.StorageSourceListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.StorageSourceListResult"]
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            429: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            500: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
            503: lambda response: HttpResponseError(response=response, model=self._deserialize(_models.ErrorResponseV2, response)),
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_document_storage_source.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('StorageSourceListResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_document_storage_source.metadata = {'url': '/storagesources'}  # type: ignore
