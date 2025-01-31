# coding: utf-8

"""

    Copyright (c) 2022 Aspose.BarCode for Cloud

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.

"""


import pprint
import re  # noqa: F401

import six


class GeneratorParamsList(object):
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
    swagger_types = {"barcode_builders": "list[GeneratorParams]", "x_step": "int", "y_step": "int"}

    attribute_map = {"barcode_builders": "BarcodeBuilders", "x_step": "XStep", "y_step": "YStep"}

    def __init__(self, barcode_builders=None, x_step=None, y_step=None):  # noqa: E501
        """GeneratorParamsList - a model defined in Swagger"""  # noqa: E501

        self._barcode_builders = None
        self._x_step = None
        self._y_step = None
        self.discriminator = None

        if barcode_builders is not None:
            self.barcode_builders = barcode_builders
        self.x_step = x_step
        self.y_step = y_step

    @property
    def barcode_builders(self):
        """Gets the barcode_builders of this GeneratorParamsList.  # noqa: E501

        List of barcode generators  # noqa: E501

        :return: The barcode_builders of this GeneratorParamsList.  # noqa: E501
        :rtype: list[GeneratorParams]
        """
        return self._barcode_builders

    @barcode_builders.setter
    def barcode_builders(self, barcode_builders):
        """Sets the barcode_builders of this GeneratorParamsList.

        List of barcode generators  # noqa: E501

        :param barcode_builders: The barcode_builders of this GeneratorParamsList.  # noqa: E501
        :type: list[GeneratorParams]
        """

        self._barcode_builders = barcode_builders

    @property
    def x_step(self):
        """Gets the x_step of this GeneratorParamsList.  # noqa: E501

        Shift step according to X axis  # noqa: E501

        :return: The x_step of this GeneratorParamsList.  # noqa: E501
        :rtype: int
        """
        return self._x_step

    @x_step.setter
    def x_step(self, x_step):
        """Sets the x_step of this GeneratorParamsList.

        Shift step according to X axis  # noqa: E501

        :param x_step: The x_step of this GeneratorParamsList.  # noqa: E501
        :type: int
        """
        if x_step is None:
            raise ValueError("Invalid value for `x_step`, must not be `None`")  # noqa: E501

        self._x_step = x_step

    @property
    def y_step(self):
        """Gets the y_step of this GeneratorParamsList.  # noqa: E501

        Shift step according to Y axis  # noqa: E501

        :return: The y_step of this GeneratorParamsList.  # noqa: E501
        :rtype: int
        """
        return self._y_step

    @y_step.setter
    def y_step(self, y_step):
        """Sets the y_step of this GeneratorParamsList.

        Shift step according to Y axis  # noqa: E501

        :param y_step: The y_step of this GeneratorParamsList.  # noqa: E501
        :type: int
        """
        if y_step is None:
            raise ValueError("Invalid value for `y_step`, must not be `None`")  # noqa: E501

        self._y_step = y_step

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(GeneratorParamsList, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GeneratorParamsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
