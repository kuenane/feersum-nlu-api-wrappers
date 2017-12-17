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


class Date(object):
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
        'date': 'str',
        'granularity': 'str'
    }

    attribute_map = {
        'date': 'date',
        'granularity': 'granularity'
    }

    def __init__(self, date=None, granularity=None):  # noqa: E501
        """Date - a model defined in Swagger"""  # noqa: E501

        self._date = None
        self._granularity = None
        self.discriminator = None

        self.date = date
        self.granularity = granularity

    @property
    def date(self):
        """Gets the date of this Date.  # noqa: E501


        :return: The date of this Date.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Date.


        :param date: The date of this Date.  # noqa: E501
        :type: str
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def granularity(self):
        """Gets the granularity of this Date.  # noqa: E501


        :return: The granularity of this Date.  # noqa: E501
        :rtype: str
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """Sets the granularity of this Date.


        :param granularity: The granularity of this Date.  # noqa: E501
        :type: str
        """
        if granularity is None:
            raise ValueError("Invalid value for `granularity`, must not be `None`")  # noqa: E501
        allowed_values = ["second", "minute", "hour", "day", "week", "month", "year"]  # noqa: E501
        if granularity not in allowed_values:
            raise ValueError(
                "Invalid value for `granularity` ({0}), must be one of {1}"  # noqa: E501
                .format(granularity, allowed_values)
            )

        self._granularity = granularity

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
        if not isinstance(other, Date):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
