# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing import Optional

from pieces_os_client.models.created_external_provider_api_key import CreatedExternalProviderApiKey
from pieces_os_client.models.deleted_external_provider_api_key import DeletedExternalProviderApiKey
from pieces_os_client.models.precreated_external_provider_api_key import PrecreatedExternalProviderApiKey
from pieces_os_client.models.predeleted_external_provider_api_key import PredeletedExternalProviderApiKey
from pieces_os_client.models.preupdated_external_provider_api_key import PreupdatedExternalProviderApiKey
from pieces_os_client.models.updated_external_provider_api_key import UpdatedExternalProviderApiKey

from pieces_os_client.api_client import ApiClient
from pieces_os_client.api_response import ApiResponse
from pieces_os_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ExternalProviderApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def external_provider_api_key_create(self, precreated_external_provider_api_key : Optional[PrecreatedExternalProviderApiKey] = None, **kwargs) -> CreatedExternalProviderApiKey:  # noqa: E501
        """/external_provider/api_key/create [POST]  # noqa: E501

        This will create a specific external_provider api_key from a specific user Auth0UserMetadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.external_provider_api_key_create(precreated_external_provider_api_key, async_req=True)
        >>> result = thread.get()

        :param precreated_external_provider_api_key:
        :type precreated_external_provider_api_key: PrecreatedExternalProviderApiKey
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreatedExternalProviderApiKey
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the external_provider_api_key_create_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.external_provider_api_key_create_with_http_info(precreated_external_provider_api_key, **kwargs)  # noqa: E501

    @validate_arguments
    def external_provider_api_key_create_with_http_info(self, precreated_external_provider_api_key : Optional[PrecreatedExternalProviderApiKey] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/external_provider/api_key/create [POST]  # noqa: E501

        This will create a specific external_provider api_key from a specific user Auth0UserMetadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.external_provider_api_key_create_with_http_info(precreated_external_provider_api_key, async_req=True)
        >>> result = thread.get()

        :param precreated_external_provider_api_key:
        :type precreated_external_provider_api_key: PrecreatedExternalProviderApiKey
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CreatedExternalProviderApiKey, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'precreated_external_provider_api_key'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method external_provider_api_key_create" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['precreated_external_provider_api_key'] is not None:
            _body_params = _params['precreated_external_provider_api_key']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "CreatedExternalProviderApiKey",
            '401': "str",
            '500': "str",
        }

        return self.api_client.call_api(
            '/external_provider/api_key/create', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def external_provider_api_key_delete(self, predeleted_external_provider_api_key : Optional[PredeletedExternalProviderApiKey] = None, **kwargs) -> DeletedExternalProviderApiKey:  # noqa: E501
        """/external_provider/api_key/delete [POST]  # noqa: E501

        This will remove a specific external_provider api_key from a specific user Auth0UserMetadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.external_provider_api_key_delete(predeleted_external_provider_api_key, async_req=True)
        >>> result = thread.get()

        :param predeleted_external_provider_api_key:
        :type predeleted_external_provider_api_key: PredeletedExternalProviderApiKey
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DeletedExternalProviderApiKey
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the external_provider_api_key_delete_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.external_provider_api_key_delete_with_http_info(predeleted_external_provider_api_key, **kwargs)  # noqa: E501

    @validate_arguments
    def external_provider_api_key_delete_with_http_info(self, predeleted_external_provider_api_key : Optional[PredeletedExternalProviderApiKey] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/external_provider/api_key/delete [POST]  # noqa: E501

        This will remove a specific external_provider api_key from a specific user Auth0UserMetadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.external_provider_api_key_delete_with_http_info(predeleted_external_provider_api_key, async_req=True)
        >>> result = thread.get()

        :param predeleted_external_provider_api_key:
        :type predeleted_external_provider_api_key: PredeletedExternalProviderApiKey
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(DeletedExternalProviderApiKey, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'predeleted_external_provider_api_key'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method external_provider_api_key_delete" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['predeleted_external_provider_api_key'] is not None:
            _body_params = _params['predeleted_external_provider_api_key']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "DeletedExternalProviderApiKey",
            '401': "str",
            '500': "str",
        }

        return self.api_client.call_api(
            '/external_provider/api_key/delete', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def external_provider_api_key_update(self, preupdated_external_provider_api_key : Optional[PreupdatedExternalProviderApiKey] = None, **kwargs) -> UpdatedExternalProviderApiKey:  # noqa: E501
        """/external_provider/api_key/update [POST]  # noqa: E501

        This will update a specific external_provider api_key from a specific user Auth0UserMetadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.external_provider_api_key_update(preupdated_external_provider_api_key, async_req=True)
        >>> result = thread.get()

        :param preupdated_external_provider_api_key:
        :type preupdated_external_provider_api_key: PreupdatedExternalProviderApiKey
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UpdatedExternalProviderApiKey
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the external_provider_api_key_update_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.external_provider_api_key_update_with_http_info(preupdated_external_provider_api_key, **kwargs)  # noqa: E501

    @validate_arguments
    def external_provider_api_key_update_with_http_info(self, preupdated_external_provider_api_key : Optional[PreupdatedExternalProviderApiKey] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/external_provider/api_key/update [POST]  # noqa: E501

        This will update a specific external_provider api_key from a specific user Auth0UserMetadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.external_provider_api_key_update_with_http_info(preupdated_external_provider_api_key, async_req=True)
        >>> result = thread.get()

        :param preupdated_external_provider_api_key:
        :type preupdated_external_provider_api_key: PreupdatedExternalProviderApiKey
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(UpdatedExternalProviderApiKey, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'preupdated_external_provider_api_key'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method external_provider_api_key_update" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['preupdated_external_provider_api_key'] is not None:
            _body_params = _params['preupdated_external_provider_api_key']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "UpdatedExternalProviderApiKey",
            '401': "str",
            '500': "str",
        }

        return self.api_client.call_api(
            '/external_provider/api_key/update', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
