# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.26
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from feersum_nlu.models.labeled_word_manifold import LabeledWordManifold  # noqa: F401,E501


class TrainDetails(object):
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
        'threshold': 'float',
        'immediate_mode': 'bool',
        'word_manifold': 'str',
        'word_manifold_list': 'list[LabeledWordManifold]'
    }

    attribute_map = {
        'threshold': 'threshold',
        'immediate_mode': 'immediate_mode',
        'word_manifold': 'word_manifold',
        'word_manifold_list': 'word_manifold_list'
    }

    def __init__(self, threshold=None, immediate_mode=None, word_manifold=None, word_manifold_list=None):  # noqa: E501
        """TrainDetails - a model defined in Swagger"""  # noqa: E501

        self._threshold = None
        self._immediate_mode = None
        self._word_manifold = None
        self._word_manifold_list = None
        self.discriminator = None

        if threshold is not None:
            self.threshold = threshold
        if immediate_mode is not None:
            self.immediate_mode = immediate_mode
        if word_manifold is not None:
            self.word_manifold = word_manifold
        if word_manifold_list is not None:
            self.word_manifold_list = word_manifold_list

    @property
    def threshold(self):
        """Gets the threshold of this TrainDetails.  # noqa: E501

        There is typically some model dependent threshold to be set upon training which is possibly mutable post training. This is that threshold.  # noqa: E501

        :return: The threshold of this TrainDetails.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this TrainDetails.

        There is typically some model dependent threshold to be set upon training which is possibly mutable post training. This is that threshold.  # noqa: E501

        :param threshold: The threshold of this TrainDetails.  # noqa: E501
        :type: float
        """

        self._threshold = threshold

    @property
    def immediate_mode(self):
        """Gets the immediate_mode of this TrainDetails.  # noqa: E501

        Set immediate_mode to True to do synchronous/blocking training. Might be forced to False in production.  # noqa: E501

        :return: The immediate_mode of this TrainDetails.  # noqa: E501
        :rtype: bool
        """
        return self._immediate_mode

    @immediate_mode.setter
    def immediate_mode(self, immediate_mode):
        """Sets the immediate_mode of this TrainDetails.

        Set immediate_mode to True to do synchronous/blocking training. Might be forced to False in production.  # noqa: E501

        :param immediate_mode: The immediate_mode of this TrainDetails.  # noqa: E501
        :type: bool
        """

        self._immediate_mode = immediate_mode

    @property
    def word_manifold(self):
        """Gets the word_manifold of this TrainDetails.  # noqa: E501

        The word manifold instance to use for training and later inference.  Rather use the word_manifold_list for supplying a language labelled list of word manifold instances to use in a multi-language system.   # noqa: E501

        :return: The word_manifold of this TrainDetails.  # noqa: E501
        :rtype: str
        """
        return self._word_manifold

    @word_manifold.setter
    def word_manifold(self, word_manifold):
        """Sets the word_manifold of this TrainDetails.

        The word manifold instance to use for training and later inference.  Rather use the word_manifold_list for supplying a language labelled list of word manifold instances to use in a multi-language system.   # noqa: E501

        :param word_manifold: The word_manifold of this TrainDetails.  # noqa: E501
        :type: str
        """

        self._word_manifold = word_manifold

    @property
    def word_manifold_list(self):
        """Gets the word_manifold_list of this TrainDetails.  # noqa: E501

        The list of labelled word manifolds to use for training.  # noqa: E501

        :return: The word_manifold_list of this TrainDetails.  # noqa: E501
        :rtype: list[LabeledWordManifold]
        """
        return self._word_manifold_list

    @word_manifold_list.setter
    def word_manifold_list(self, word_manifold_list):
        """Sets the word_manifold_list of this TrainDetails.

        The list of labelled word manifolds to use for training.  # noqa: E501

        :param word_manifold_list: The word_manifold_list of this TrainDetails.  # noqa: E501
        :type: list[LabeledWordManifold]
        """

        self._word_manifold_list = word_manifold_list

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
        if not isinstance(other, TrainDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
