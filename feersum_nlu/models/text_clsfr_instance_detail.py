# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.16
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


class TextClsfrInstanceDetail(object):
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
        'training_accuracy': 'float',
        'training_f1': 'float',
        'training_cm': 'object',
        'testing_accuracy': 'float',
        'testing_f1': 'float',
        'testing_cm': 'object',
        'cm_labels': 'object',
        'training_stamp': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'desc': 'desc',
        'training_accuracy': 'training_accuracy',
        'training_f1': 'training_f1',
        'training_cm': 'training_cm',
        'testing_accuracy': 'testing_accuracy',
        'testing_f1': 'testing_f1',
        'testing_cm': 'testing_cm',
        'cm_labels': 'cm_labels',
        'training_stamp': 'training_stamp'
    }

    def __init__(self, name=None, id=None, desc=None, training_accuracy=None, training_f1=None, training_cm=None, testing_accuracy=None, testing_f1=None, testing_cm=None, cm_labels=None, training_stamp=None):  # noqa: E501
        """TextClsfrInstanceDetail - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._id = None
        self._desc = None
        self._training_accuracy = None
        self._training_f1 = None
        self._training_cm = None
        self._testing_accuracy = None
        self._testing_f1 = None
        self._testing_cm = None
        self._cm_labels = None
        self._training_stamp = None
        self.discriminator = None

        self.name = name
        self.id = id
        if desc is not None:
            self.desc = desc
        if training_accuracy is not None:
            self.training_accuracy = training_accuracy
        if training_f1 is not None:
            self.training_f1 = training_f1
        if training_cm is not None:
            self.training_cm = training_cm
        if testing_accuracy is not None:
            self.testing_accuracy = testing_accuracy
        if testing_f1 is not None:
            self.testing_f1 = testing_f1
        if testing_cm is not None:
            self.testing_cm = testing_cm
        if cm_labels is not None:
            self.cm_labels = cm_labels
        if training_stamp is not None:
            self.training_stamp = training_stamp

    @property
    def name(self):
        """Gets the name of this TextClsfrInstanceDetail.  # noqa: E501

        The sluggy-url-friendly-name of the instance.  # noqa: E501

        :return: The name of this TextClsfrInstanceDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TextClsfrInstanceDetail.

        The sluggy-url-friendly-name of the instance.  # noqa: E501

        :param name: The name of this TextClsfrInstanceDetail.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this TextClsfrInstanceDetail.  # noqa: E501

        The unique id of a specific version of the model instance.  # noqa: E501

        :return: The id of this TextClsfrInstanceDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TextClsfrInstanceDetail.

        The unique id of a specific version of the model instance.  # noqa: E501

        :param id: The id of this TextClsfrInstanceDetail.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def desc(self):
        """Gets the desc of this TextClsfrInstanceDetail.  # noqa: E501

        The longer existential description of this instance's purpose in life.  # noqa: E501

        :return: The desc of this TextClsfrInstanceDetail.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this TextClsfrInstanceDetail.

        The longer existential description of this instance's purpose in life.  # noqa: E501

        :param desc: The desc of this TextClsfrInstanceDetail.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def training_accuracy(self):
        """Gets the training_accuracy of this TextClsfrInstanceDetail.  # noqa: E501

        The accuracy of the model as measured on the training set.  # noqa: E501

        :return: The training_accuracy of this TextClsfrInstanceDetail.  # noqa: E501
        :rtype: float
        """
        return self._training_accuracy

    @training_accuracy.setter
    def training_accuracy(self, training_accuracy):
        """Sets the training_accuracy of this TextClsfrInstanceDetail.

        The accuracy of the model as measured on the training set.  # noqa: E501

        :param training_accuracy: The training_accuracy of this TextClsfrInstanceDetail.  # noqa: E501
        :type: float
        """

        self._training_accuracy = training_accuracy

    @property
    def training_f1(self):
        """Gets the training_f1 of this TextClsfrInstanceDetail.  # noqa: E501

        The average F-score of the model as measured on the training set.  # noqa: E501

        :return: The training_f1 of this TextClsfrInstanceDetail.  # noqa: E501
        :rtype: float
        """
        return self._training_f1

    @training_f1.setter
    def training_f1(self, training_f1):
        """Sets the training_f1 of this TextClsfrInstanceDetail.

        The average F-score of the model as measured on the training set.  # noqa: E501

        :param training_f1: The training_f1 of this TextClsfrInstanceDetail.  # noqa: E501
        :type: float
        """

        self._training_f1 = training_f1

    @property
    def training_cm(self):
        """Gets the training_cm of this TextClsfrInstanceDetail.  # noqa: E501

        The confusion matrix as measured on the training set. The matrix is expected to be quite sparse so a compact dict of dicts representation is used.  # noqa: E501

        :return: The training_cm of this TextClsfrInstanceDetail.  # noqa: E501
        :rtype: object
        """
        return self._training_cm

    @training_cm.setter
    def training_cm(self, training_cm):
        """Sets the training_cm of this TextClsfrInstanceDetail.

        The confusion matrix as measured on the training set. The matrix is expected to be quite sparse so a compact dict of dicts representation is used.  # noqa: E501

        :param training_cm: The training_cm of this TextClsfrInstanceDetail.  # noqa: E501
        :type: object
        """

        self._training_cm = training_cm

    @property
    def testing_accuracy(self):
        """Gets the testing_accuracy of this TextClsfrInstanceDetail.  # noqa: E501

        The accuracy of the model as measured on the testing set.  # noqa: E501

        :return: The testing_accuracy of this TextClsfrInstanceDetail.  # noqa: E501
        :rtype: float
        """
        return self._testing_accuracy

    @testing_accuracy.setter
    def testing_accuracy(self, testing_accuracy):
        """Sets the testing_accuracy of this TextClsfrInstanceDetail.

        The accuracy of the model as measured on the testing set.  # noqa: E501

        :param testing_accuracy: The testing_accuracy of this TextClsfrInstanceDetail.  # noqa: E501
        :type: float
        """

        self._testing_accuracy = testing_accuracy

    @property
    def testing_f1(self):
        """Gets the testing_f1 of this TextClsfrInstanceDetail.  # noqa: E501

        The average F-score of the model as measured on the testing set.  # noqa: E501

        :return: The testing_f1 of this TextClsfrInstanceDetail.  # noqa: E501
        :rtype: float
        """
        return self._testing_f1

    @testing_f1.setter
    def testing_f1(self, testing_f1):
        """Sets the testing_f1 of this TextClsfrInstanceDetail.

        The average F-score of the model as measured on the testing set.  # noqa: E501

        :param testing_f1: The testing_f1 of this TextClsfrInstanceDetail.  # noqa: E501
        :type: float
        """

        self._testing_f1 = testing_f1

    @property
    def testing_cm(self):
        """Gets the testing_cm of this TextClsfrInstanceDetail.  # noqa: E501

        The confusion matrix as measured on the testing set. The matrix is expected to be quite sparse so a compact dict of dicts representation is used.  # noqa: E501

        :return: The testing_cm of this TextClsfrInstanceDetail.  # noqa: E501
        :rtype: object
        """
        return self._testing_cm

    @testing_cm.setter
    def testing_cm(self, testing_cm):
        """Sets the testing_cm of this TextClsfrInstanceDetail.

        The confusion matrix as measured on the testing set. The matrix is expected to be quite sparse so a compact dict of dicts representation is used.  # noqa: E501

        :param testing_cm: The testing_cm of this TextClsfrInstanceDetail.  # noqa: E501
        :type: object
        """

        self._testing_cm = testing_cm

    @property
    def cm_labels(self):
        """Gets the cm_labels of this TextClsfrInstanceDetail.  # noqa: E501

        A dict that, if present, maps from the confusion matrix row and column labels to longer more descriptive labels. For example, if present it maps an FAQ answer ID to the string answer which may be either a label or the full text answer.  # noqa: E501

        :return: The cm_labels of this TextClsfrInstanceDetail.  # noqa: E501
        :rtype: object
        """
        return self._cm_labels

    @cm_labels.setter
    def cm_labels(self, cm_labels):
        """Sets the cm_labels of this TextClsfrInstanceDetail.

        A dict that, if present, maps from the confusion matrix row and column labels to longer more descriptive labels. For example, if present it maps an FAQ answer ID to the string answer which may be either a label or the full text answer.  # noqa: E501

        :param cm_labels: The cm_labels of this TextClsfrInstanceDetail.  # noqa: E501
        :type: object
        """

        self._cm_labels = cm_labels

    @property
    def training_stamp(self):
        """Gets the training_stamp of this TextClsfrInstanceDetail.  # noqa: E501

        The time when the training operation concluded.  # noqa: E501

        :return: The training_stamp of this TextClsfrInstanceDetail.  # noqa: E501
        :rtype: str
        """
        return self._training_stamp

    @training_stamp.setter
    def training_stamp(self, training_stamp):
        """Sets the training_stamp of this TextClsfrInstanceDetail.

        The time when the training operation concluded.  # noqa: E501

        :param training_stamp: The training_stamp of this TextClsfrInstanceDetail.  # noqa: E501
        :type: str
        """

        self._training_stamp = training_stamp

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
        if not isinstance(other, TextClsfrInstanceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
