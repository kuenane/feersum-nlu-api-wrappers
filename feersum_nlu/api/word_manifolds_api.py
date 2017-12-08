# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.9
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from feersum_nlu.api_client import ApiClient


class WordManifoldsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def word_manifold_add_similar_words(self, instance_name, new_word_list, **kwargs):  # noqa: E501
        """Add new words.  # noqa: E501

        Add new words to the manifold that are similar to existing words and save the manifold. Warning! - Because this operation saves the updated word manifold to the store it could take a few seconds to complete. Returns the details of the updated instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_add_similar_words(instance_name, new_word_list, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param NewWordList new_word_list: List of new words. (required)
        :return: WmInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.word_manifold_add_similar_words_with_http_info(instance_name, new_word_list, **kwargs)  # noqa: E501
        else:
            (data) = self.word_manifold_add_similar_words_with_http_info(instance_name, new_word_list, **kwargs)  # noqa: E501
            return data

    def word_manifold_add_similar_words_with_http_info(self, instance_name, new_word_list, **kwargs):  # noqa: E501
        """Add new words.  # noqa: E501

        Add new words to the manifold that are similar to existing words and save the manifold. Warning! - Because this operation saves the updated word manifold to the store it could take a few seconds to complete. Returns the details of the updated instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_add_similar_words_with_http_info(instance_name, new_word_list, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param NewWordList new_word_list: List of new words. (required)
        :return: WmInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'new_word_list']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method word_manifold_add_similar_words" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `word_manifold_add_similar_words`")  # noqa: E501
        # verify the required parameter 'new_word_list' is set
        if ('new_word_list' not in params or
                params['new_word_list'] is None):
            raise ValueError("Missing the required parameter `new_word_list` when calling `word_manifold_add_similar_words`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instance_name' in params:
            path_params['instance_name'] = params['instance_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_word_list' in params:
            body_params = params['new_word_list']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/word_manifolds/{instance_name}/vocab', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WmInstanceDetail',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def word_manifold_create(self, wm_create_details, **kwargs):  # noqa: E501
        """Create a word manifold model.  # noqa: E501

        Create a new word manifold model using an input file or load a model from the store. Warning! - These models are quite big and each takes a few seconds to load/create. Returns the details of the new or loaded instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_create(wm_create_details, async=True)
        >>> result = thread.get()

        :param async bool
        :param WmCreateDetails wm_create_details: The details of the word manifold instance to create. (required)
        :return: WmInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.word_manifold_create_with_http_info(wm_create_details, **kwargs)  # noqa: E501
        else:
            (data) = self.word_manifold_create_with_http_info(wm_create_details, **kwargs)  # noqa: E501
            return data

    def word_manifold_create_with_http_info(self, wm_create_details, **kwargs):  # noqa: E501
        """Create a word manifold model.  # noqa: E501

        Create a new word manifold model using an input file or load a model from the store. Warning! - These models are quite big and each takes a few seconds to load/create. Returns the details of the new or loaded instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_create_with_http_info(wm_create_details, async=True)
        >>> result = thread.get()

        :param async bool
        :param WmCreateDetails wm_create_details: The details of the word manifold instance to create. (required)
        :return: WmInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wm_create_details']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method word_manifold_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wm_create_details' is set
        if ('wm_create_details' not in params or
                params['wm_create_details'] is None):
            raise ValueError("Missing the required parameter `wm_create_details` when calling `word_manifold_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'wm_create_details' in params:
            body_params = params['wm_create_details']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/word_manifolds', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WmInstanceDetail',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def word_manifold_get_similar_words(self, instance_name, word_and_threshold, **kwargs):  # noqa: E501
        """Find similar words.  # noqa: E501

        Returns words from the manifold that are similar to the parameter word.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_get_similar_words(instance_name, word_and_threshold, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param WordAndThreshold word_and_threshold: A word token and an accompanying threshold. (required)
        :return: WordAndDistanceList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.word_manifold_get_similar_words_with_http_info(instance_name, word_and_threshold, **kwargs)  # noqa: E501
        else:
            (data) = self.word_manifold_get_similar_words_with_http_info(instance_name, word_and_threshold, **kwargs)  # noqa: E501
            return data

    def word_manifold_get_similar_words_with_http_info(self, instance_name, word_and_threshold, **kwargs):  # noqa: E501
        """Find similar words.  # noqa: E501

        Returns words from the manifold that are similar to the parameter word.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_get_similar_words_with_http_info(instance_name, word_and_threshold, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param WordAndThreshold word_and_threshold: A word token and an accompanying threshold. (required)
        :return: WordAndDistanceList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'word_and_threshold']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method word_manifold_get_similar_words" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `word_manifold_get_similar_words`")  # noqa: E501
        # verify the required parameter 'word_and_threshold' is set
        if ('word_and_threshold' not in params or
                params['word_and_threshold'] is None):
            raise ValueError("Missing the required parameter `word_and_threshold` when calling `word_manifold_get_similar_words`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instance_name' in params:
            path_params['instance_name'] = params['instance_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'word_and_threshold' in params:
            body_params = params['word_and_threshold']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/word_manifolds/{instance_name}/similar_words', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WordAndDistanceList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def word_manifold_spell_correct(self, instance_name, text_input, **kwargs):  # noqa: E501
        """Spell correct a word.  # noqa: E501

        Spell correct a word replacing it with the most likely word from the manifold. Returns one or more scored candidate words.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_spell_correct(instance_name, text_input, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param TextInput text_input: The input text. (required)
        :return: WordAndDistanceList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.word_manifold_spell_correct_with_http_info(instance_name, text_input, **kwargs)  # noqa: E501
        else:
            (data) = self.word_manifold_spell_correct_with_http_info(instance_name, text_input, **kwargs)  # noqa: E501
            return data

    def word_manifold_spell_correct_with_http_info(self, instance_name, text_input, **kwargs):  # noqa: E501
        """Spell correct a word.  # noqa: E501

        Spell correct a word replacing it with the most likely word from the manifold. Returns one or more scored candidate words.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_spell_correct_with_http_info(instance_name, text_input, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param TextInput text_input: The input text. (required)
        :return: WordAndDistanceList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'text_input']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method word_manifold_spell_correct" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `word_manifold_spell_correct`")  # noqa: E501
        # verify the required parameter 'text_input' is set
        if ('text_input' not in params or
                params['text_input'] is None):
            raise ValueError("Missing the required parameter `text_input` when calling `word_manifold_spell_correct`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instance_name' in params:
            path_params['instance_name'] = params['instance_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'text_input' in params:
            body_params = params['text_input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/word_manifolds/{instance_name}/spell_correct', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WordAndDistanceList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
