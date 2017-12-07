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

import pprint
import re  # noqa: F401

import six


class CreateDetails(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'desc': 'str',
        'lid_model_file': 'str',
        'load_from_store': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'desc': 'desc',
        'lid_model_file': 'lid_model_file',
        'load_from_store': 'load_from_store'
    }

    def __init__(self, name=None, desc=None, lid_model_file=None, load_from_store=None):  # noqa: E501
        """CreateDetails - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._desc = None
        self._lid_model_file = None
        self._load_from_store = None
        self.discriminator = None

        self.name = name
        if desc is not None:
            self.desc = desc
        if lid_model_file is not None:
            self.lid_model_file = lid_model_file
        self.load_from_store = load_from_store

    @property
    def name(self):
        """Gets the name of this CreateDetails.  # noqa: E501

        The sluggy-url-friendly-name of the instance.  # noqa: E501

        :return: The name of this CreateDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDetails.

        The sluggy-url-friendly-name of the instance.  # noqa: E501

        :param name: The name of this CreateDetails.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def desc(self):
        """Gets the desc of this CreateDetails.  # noqa: E501

        The longer existential description of this instance's purpose in life.  # noqa: E501

        :return: The desc of this CreateDetails.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this CreateDetails.

        The longer existential description of this instance's purpose in life.  # noqa: E501

        :param desc: The desc of this CreateDetails.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def lid_model_file(self):
        """Gets the lid_model_file of this CreateDetails.  # noqa: E501

        The pre-trained LID model to load.  # noqa: E501

        :return: The lid_model_file of this CreateDetails.  # noqa: E501
        :rtype: str
        """
        return self._lid_model_file

    @lid_model_file.setter
    def lid_model_file(self, lid_model_file):
        """Sets the lid_model_file of this CreateDetails.

        The pre-trained LID model to load.  # noqa: E501

        :param lid_model_file: The lid_model_file of this CreateDetails.  # noqa: E501
        :type: str
        """

        self._lid_model_file = lid_model_file

    @property
    def load_from_store(self):
        """Gets the load_from_store of this CreateDetails.  # noqa: E501

        Indicates if a pre-existing model with the specified name should be loaded from the model store. Usually set to False in which case a new model is created with details as specified.  # noqa: E501

        :return: The load_from_store of this CreateDetails.  # noqa: E501
        :rtype: bool
        """
        return self._load_from_store

    @load_from_store.setter
    def load_from_store(self, load_from_store):
        """Sets the load_from_store of this CreateDetails.

        Indicates if a pre-existing model with the specified name should be loaded from the model store. Usually set to False in which case a new model is created with details as specified.  # noqa: E501

        :param load_from_store: The load_from_store of this CreateDetails.  # noqa: E501
        :type: bool
        """
        if load_from_store is None:
            raise ValueError("Invalid value for `load_from_store`, must not be `None`")  # noqa: E501

        self._load_from_store = load_from_store

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
