# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.14
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


class Lr4InstanceDetail(object):
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
        'id': 'str',
        'desc': 'str',
        'lid_model_file': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'desc': 'desc',
        'lid_model_file': 'lid_model_file'
    }

    def __init__(self, name=None, id=None, desc=None, lid_model_file=None):  # noqa: E501
        """Lr4InstanceDetail - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._id = None
        self._desc = None
        self._lid_model_file = None
        self.discriminator = None

        self.name = name
        self.id = id
        if desc is not None:
            self.desc = desc
        self.lid_model_file = lid_model_file

    @property
    def name(self):
        """Gets the name of this Lr4InstanceDetail.  # noqa: E501

        The sluggy-url-friendly-name of the instance.  # noqa: E501

        :return: The name of this Lr4InstanceDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Lr4InstanceDetail.

        The sluggy-url-friendly-name of the instance.  # noqa: E501

        :param name: The name of this Lr4InstanceDetail.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this Lr4InstanceDetail.  # noqa: E501

        The unique id of a specific version of the model instance.  # noqa: E501

        :return: The id of this Lr4InstanceDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Lr4InstanceDetail.

        The unique id of a specific version of the model instance.  # noqa: E501

        :param id: The id of this Lr4InstanceDetail.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def desc(self):
        """Gets the desc of this Lr4InstanceDetail.  # noqa: E501

        The longer existential description of this instance's purpose in life.  # noqa: E501

        :return: The desc of this Lr4InstanceDetail.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this Lr4InstanceDetail.

        The longer existential description of this instance's purpose in life.  # noqa: E501

        :param desc: The desc of this Lr4InstanceDetail.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def lid_model_file(self):
        """Gets the lid_model_file of this Lr4InstanceDetail.  # noqa: E501

        The pre-trained model this instance was created from.  # noqa: E501

        :return: The lid_model_file of this Lr4InstanceDetail.  # noqa: E501
        :rtype: str
        """
        return self._lid_model_file

    @lid_model_file.setter
    def lid_model_file(self, lid_model_file):
        """Sets the lid_model_file of this Lr4InstanceDetail.

        The pre-trained model this instance was created from.  # noqa: E501

        :param lid_model_file: The lid_model_file of this Lr4InstanceDetail.  # noqa: E501
        :type: str
        """
        if lid_model_file is None:
            raise ValueError("Invalid value for `lid_model_file`, must not be `None`")  # noqa: E501

        self._lid_model_file = lid_model_file

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
        if not isinstance(other, Lr4InstanceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
