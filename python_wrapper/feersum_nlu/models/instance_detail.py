# coding: utf-8

"""
    Feersum NLU API

    This is an HTTP API for Feersum NLU

    OpenAPI spec version: 2.0.1
    
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

from pprint import pformat
from six import iteritems
import re


class InstanceDetail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, id=None, desc=None, training_accuracy=None, training_stamp=None, training_cm=None):
        """
        InstanceDetail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'id': 'str',
            'desc': 'str',
            'training_accuracy': 'float',
            'training_stamp': 'str',
            'training_cm': 'object'
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id',
            'desc': 'desc',
            'training_accuracy': 'training_accuracy',
            'training_stamp': 'training_stamp',
            'training_cm': 'training_cm'
        }

        self._name = name
        self._id = id
        self._desc = desc
        self._training_accuracy = training_accuracy
        self._training_stamp = training_stamp
        self._training_cm = training_cm


    @property
    def name(self):
        """
        Gets the name of this InstanceDetail.


        :return: The name of this InstanceDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InstanceDetail.


        :param name: The name of this InstanceDetail.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def id(self):
        """
        Gets the id of this InstanceDetail.


        :return: The id of this InstanceDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstanceDetail.


        :param id: The id of this InstanceDetail.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def desc(self):
        """
        Gets the desc of this InstanceDetail.


        :return: The desc of this InstanceDetail.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """
        Sets the desc of this InstanceDetail.


        :param desc: The desc of this InstanceDetail.
        :type: str
        """

        self._desc = desc

    @property
    def training_accuracy(self):
        """
        Gets the training_accuracy of this InstanceDetail.


        :return: The training_accuracy of this InstanceDetail.
        :rtype: float
        """
        return self._training_accuracy

    @training_accuracy.setter
    def training_accuracy(self, training_accuracy):
        """
        Sets the training_accuracy of this InstanceDetail.


        :param training_accuracy: The training_accuracy of this InstanceDetail.
        :type: float
        """

        self._training_accuracy = training_accuracy

    @property
    def training_stamp(self):
        """
        Gets the training_stamp of this InstanceDetail.


        :return: The training_stamp of this InstanceDetail.
        :rtype: str
        """
        return self._training_stamp

    @training_stamp.setter
    def training_stamp(self, training_stamp):
        """
        Sets the training_stamp of this InstanceDetail.


        :param training_stamp: The training_stamp of this InstanceDetail.
        :type: str
        """

        self._training_stamp = training_stamp

    @property
    def training_cm(self):
        """
        Gets the training_cm of this InstanceDetail.


        :return: The training_cm of this InstanceDetail.
        :rtype: object
        """
        return self._training_cm

    @training_cm.setter
    def training_cm(self, training_cm):
        """
        Sets the training_cm of this InstanceDetail.


        :param training_cm: The training_cm of this InstanceDetail.
        :type: object
        """

        self._training_cm = training_cm

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
