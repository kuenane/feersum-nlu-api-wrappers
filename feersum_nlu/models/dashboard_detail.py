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

from feersum_nlu.models.dashboard_model_detail import DashboardModelDetail  # noqa: F401,E501


class DashboardDetail(object):
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
        'api_version': 'str',
        'service_name': 'str',
        'peak_api_hit_rate': 'float',
        'model_list': 'list[DashboardModelDetail]'
    }

    attribute_map = {
        'api_version': 'api_version',
        'service_name': 'service_name',
        'peak_api_hit_rate': 'peak_api_hit_rate',
        'model_list': 'model_list'
    }

    def __init__(self, api_version=None, service_name=None, peak_api_hit_rate=None, model_list=None):  # noqa: E501
        """DashboardDetail - a model defined in Swagger"""  # noqa: E501

        self._api_version = None
        self._service_name = None
        self._peak_api_hit_rate = None
        self._model_list = None
        self.discriminator = None

        self.api_version = api_version
        self.service_name = service_name
        self.peak_api_hit_rate = peak_api_hit_rate
        self.model_list = model_list

    @property
    def api_version(self):
        """Gets the api_version of this DashboardDetail.  # noqa: E501

        The version of the http api.  # noqa: E501

        :return: The api_version of this DashboardDetail.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this DashboardDetail.

        The version of the http api.  # noqa: E501

        :param api_version: The api_version of this DashboardDetail.  # noqa: E501
        :type: str
        """
        if api_version is None:
            raise ValueError("Invalid value for `api_version`, must not be `None`")  # noqa: E501

        self._api_version = api_version

    @property
    def service_name(self):
        """Gets the service_name of this DashboardDetail.  # noqa: E501

        The details of this service.  # noqa: E501

        :return: The service_name of this DashboardDetail.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this DashboardDetail.

        The details of this service.  # noqa: E501

        :param service_name: The service_name of this DashboardDetail.  # noqa: E501
        :type: str
        """
        if service_name is None:
            raise ValueError("Invalid value for `service_name`, must not be `None`")  # noqa: E501

        self._service_name = service_name

    @property
    def peak_api_hit_rate(self):
        """Gets the peak_api_hit_rate of this DashboardDetail.  # noqa: E501

        The peak api hit rate (hits/s) over the last couple of window periods. A window period is in the order of 5 minutes.  # noqa: E501

        :return: The peak_api_hit_rate of this DashboardDetail.  # noqa: E501
        :rtype: float
        """
        return self._peak_api_hit_rate

    @peak_api_hit_rate.setter
    def peak_api_hit_rate(self, peak_api_hit_rate):
        """Sets the peak_api_hit_rate of this DashboardDetail.

        The peak api hit rate (hits/s) over the last couple of window periods. A window period is in the order of 5 minutes.  # noqa: E501

        :param peak_api_hit_rate: The peak_api_hit_rate of this DashboardDetail.  # noqa: E501
        :type: float
        """
        if peak_api_hit_rate is None:
            raise ValueError("Invalid value for `peak_api_hit_rate`, must not be `None`")  # noqa: E501

        self._peak_api_hit_rate = peak_api_hit_rate

    @property
    def model_list(self):
        """Gets the model_list of this DashboardDetail.  # noqa: E501

        A list of models' instance details.  # noqa: E501

        :return: The model_list of this DashboardDetail.  # noqa: E501
        :rtype: list[DashboardModelDetail]
        """
        return self._model_list

    @model_list.setter
    def model_list(self, model_list):
        """Sets the model_list of this DashboardDetail.

        A list of models' instance details.  # noqa: E501

        :param model_list: The model_list of this DashboardDetail.  # noqa: E501
        :type: list[DashboardModelDetail]
        """
        if model_list is None:
            raise ValueError("Invalid value for `model_list`, must not be `None`")  # noqa: E501

        self._model_list = model_list

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
        if not isinstance(other, DashboardDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
