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


class DashboardModelDetail(object):
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
        'peak_api_hit_rate': 'float',
        'model_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'desc': 'desc',
        'peak_api_hit_rate': 'peak_api_hit_rate',
        'model_type': 'model_type'
    }

    def __init__(self, name=None, desc=None, peak_api_hit_rate=None, model_type=None):  # noqa: E501
        """DashboardModelDetail - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._desc = None
        self._peak_api_hit_rate = None
        self._model_type = None
        self.discriminator = None

        self.name = name
        if desc is not None:
            self.desc = desc
        if peak_api_hit_rate is not None:
            self.peak_api_hit_rate = peak_api_hit_rate
        self.model_type = model_type

    @property
    def name(self):
        """Gets the name of this DashboardModelDetail.  # noqa: E501

        The sluggy-url-friendly-name of the instance.  # noqa: E501

        :return: The name of this DashboardModelDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DashboardModelDetail.

        The sluggy-url-friendly-name of the instance.  # noqa: E501

        :param name: The name of this DashboardModelDetail.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def desc(self):
        """Gets the desc of this DashboardModelDetail.  # noqa: E501

        The longer existential description of this instance's purpose in life.  # noqa: E501

        :return: The desc of this DashboardModelDetail.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this DashboardModelDetail.

        The longer existential description of this instance's purpose in life.  # noqa: E501

        :param desc: The desc of this DashboardModelDetail.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def peak_api_hit_rate(self):
        """Gets the peak_api_hit_rate of this DashboardModelDetail.  # noqa: E501

        The peak api hit rate (hits/s) over the last couple of window periods. A window period is in the order of 5 minutes.  # noqa: E501

        :return: The peak_api_hit_rate of this DashboardModelDetail.  # noqa: E501
        :rtype: float
        """
        return self._peak_api_hit_rate

    @peak_api_hit_rate.setter
    def peak_api_hit_rate(self, peak_api_hit_rate):
        """Sets the peak_api_hit_rate of this DashboardModelDetail.

        The peak api hit rate (hits/s) over the last couple of window periods. A window period is in the order of 5 minutes.  # noqa: E501

        :param peak_api_hit_rate: The peak_api_hit_rate of this DashboardModelDetail.  # noqa: E501
        :type: float
        """

        self._peak_api_hit_rate = peak_api_hit_rate

    @property
    def model_type(self):
        """Gets the model_type of this DashboardModelDetail.  # noqa: E501

        The type of this model.  # noqa: E501

        :return: The model_type of this DashboardModelDetail.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this DashboardModelDetail.

        The type of this model.  # noqa: E501

        :param model_type: The model_type of this DashboardModelDetail.  # noqa: E501
        :type: str
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501

        self._model_type = model_type

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
        if not isinstance(other, DashboardModelDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
