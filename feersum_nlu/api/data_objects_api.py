# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.27
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from feersum_nlu.api_client import ApiClient


class DataObjectsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def data_object_del(self, instance_name, **kwargs):  # noqa: E501
        """Trash a data_object.  # noqa: E501

        Trash a data_object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_object_del(instance_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the data_object. (required)
        :return: DataObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.data_object_del_with_http_info(instance_name, **kwargs)  # noqa: E501
        else:
            (data) = self.data_object_del_with_http_info(instance_name, **kwargs)  # noqa: E501
            return data

    def data_object_del_with_http_info(self, instance_name, **kwargs):  # noqa: E501
        """Trash a data_object.  # noqa: E501

        Trash a data_object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_object_del_with_http_info(instance_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the data_object. (required)
        :return: DataObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_object_del" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `data_object_del`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instance_name' in params:
            path_params['instance_name'] = params['instance_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyHeader_old']  # noqa: E501

        return self.api_client.call_api(
            '/data_objects/{instance_name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataObject',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_object_get_details(self, instance_name, **kwargs):  # noqa: E501
        """Get a data_object.  # noqa: E501

        Get a data_object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_object_get_details(instance_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the data_object. (required)
        :return: DataObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.data_object_get_details_with_http_info(instance_name, **kwargs)  # noqa: E501
        else:
            (data) = self.data_object_get_details_with_http_info(instance_name, **kwargs)  # noqa: E501
            return data

    def data_object_get_details_with_http_info(self, instance_name, **kwargs):  # noqa: E501
        """Get a data_object.  # noqa: E501

        Get a data_object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_object_get_details_with_http_info(instance_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the data_object. (required)
        :return: DataObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_object_get_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `data_object_get_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instance_name' in params:
            path_params['instance_name'] = params['instance_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyHeader_old']  # noqa: E501

        return self.api_client.call_api(
            '/data_objects/{instance_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataObject',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_object_get_names_all(self, **kwargs):  # noqa: E501
        """Get list of names of loaded data_objects.  # noqa: E501

        Get the list of names of loaded data_objects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_object_get_names_all(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[DataObjectName]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.data_object_get_names_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.data_object_get_names_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def data_object_get_names_all_with_http_info(self, **kwargs):  # noqa: E501
        """Get list of names of loaded data_objects.  # noqa: E501

        Get the list of names of loaded data_objects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_object_get_names_all_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[DataObjectName]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_object_get_names_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyHeader_old']  # noqa: E501

        return self.api_client.call_api(
            '/data_objects', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DataObjectName]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_object_post(self, instance_name, data, **kwargs):  # noqa: E501
        """Update/create a data_object.  # noqa: E501

        Update/create a data_object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_object_post(instance_name, data, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the data_object. (required)
        :param DataObject data: The data_object. (required)
        :return: DataObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.data_object_post_with_http_info(instance_name, data, **kwargs)  # noqa: E501
        else:
            (data) = self.data_object_post_with_http_info(instance_name, data, **kwargs)  # noqa: E501
            return data

    def data_object_post_with_http_info(self, instance_name, data, **kwargs):  # noqa: E501
        """Update/create a data_object.  # noqa: E501

        Update/create a data_object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_object_post_with_http_info(instance_name, data, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the data_object. (required)
        :param DataObject data: The data_object. (required)
        :return: DataObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'data']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_object_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `data_object_post`")  # noqa: E501
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `data_object_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instance_name' in params:
            path_params['instance_name'] = params['instance_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyHeader_old']  # noqa: E501

        return self.api_client.call_api(
            '/data_objects/{instance_name}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataObject',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_object_vaporise(self, instance_name, **kwargs):  # noqa: E501
        """Vaporise the named data_object.  # noqa: E501

        Permanently vaporise the named data_object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_object_vaporise(instance_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the data_object. (required)
        :return: DataObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.data_object_vaporise_with_http_info(instance_name, **kwargs)  # noqa: E501
        else:
            (data) = self.data_object_vaporise_with_http_info(instance_name, **kwargs)  # noqa: E501
            return data

    def data_object_vaporise_with_http_info(self, instance_name, **kwargs):  # noqa: E501
        """Vaporise the named data_object.  # noqa: E501

        Permanently vaporise the named data_object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_object_vaporise_with_http_info(instance_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the data_object. (required)
        :return: DataObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_object_vaporise" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `data_object_vaporise`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instance_name' in params:
            path_params['instance_name'] = params['instance_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyHeader_old']  # noqa: E501

        return self.api_client.call_api(
            '/data_objects/{instance_name}/vaporise', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataObject',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
