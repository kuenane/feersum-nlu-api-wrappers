# coding: utf-8

"""
    Feersum NLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.

    OpenAPI spec version: 2.0.1
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

import os
import sys
import unittest

import feersum_nlu
from feersum_nlu.rest import ApiException
from feersum_nlu.apis.duckling_entity_extractors_api import DucklingEntityExtractorsApi


class TestDucklingEntityExtractorsApi(unittest.TestCase):
    """ DucklingEntityExtractorsApi unit test stubs """

    def setUp(self):
        self.api = feersum_nlu.apis.duckling_entity_extractors_api.DucklingEntityExtractorsApi()

    def tearDown(self):
        pass

    def test_duckling_entity_extractor_create(self):
        """
        Test case for duckling_entity_extractor_create

        Create a duckling entity extractor.
        """
        pass

    def test_duckling_entity_extractor_get_details(self):
        """
        Test case for duckling_entity_extractor_get_details

        Get details of named instance.
        """
        pass

    def test_duckling_entity_extractor_get_details_all(self):
        """
        Test case for duckling_entity_extractor_get_details_all

        Get list of loaded regular expression entity extractors.
        """
        pass

    def test_duckling_entity_extractor_retrieve(self):
        """
        Test case for duckling_entity_extractor_retrieve

        Extract information based on the regular expression.
        """
        pass


if __name__ == '__main__':
    unittest.main()
