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


class PatchCodeParams(object):
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
    swagger_types = {"extra_barcode_text": "str", "patch_format": "PatchFormat"}

    attribute_map = {"extra_barcode_text": "ExtraBarcodeText", "patch_format": "PatchFormat"}

    def __init__(self, extra_barcode_text=None, patch_format=None):  # noqa: E501
        """PatchCodeParams - a model defined in Swagger"""  # noqa: E501

        self._extra_barcode_text = None
        self._patch_format = None
        self.discriminator = None

        if extra_barcode_text is not None:
            self.extra_barcode_text = extra_barcode_text
        if patch_format is not None:
            self.patch_format = patch_format

    @property
    def extra_barcode_text(self):
        """Gets the extra_barcode_text of this PatchCodeParams.  # noqa: E501

        Specifies codetext for an extra QR barcode, when PatchCode is generated in page mode.  # noqa: E501

        :return: The extra_barcode_text of this PatchCodeParams.  # noqa: E501
        :rtype: str
        """
        return self._extra_barcode_text

    @extra_barcode_text.setter
    def extra_barcode_text(self, extra_barcode_text):
        """Sets the extra_barcode_text of this PatchCodeParams.

        Specifies codetext for an extra QR barcode, when PatchCode is generated in page mode.  # noqa: E501

        :param extra_barcode_text: The extra_barcode_text of this PatchCodeParams.  # noqa: E501
        :type: str
        """

        self._extra_barcode_text = extra_barcode_text

    @property
    def patch_format(self):
        """Gets the patch_format of this PatchCodeParams.  # noqa: E501

        PatchCode format. Choose PatchOnly to generate single PatchCode. Use page format to generate Patch page with PatchCodes as borders. Default value: PatchFormat.PatchOnly  # noqa: E501

        :return: The patch_format of this PatchCodeParams.  # noqa: E501
        :rtype: PatchFormat
        """
        return self._patch_format

    @patch_format.setter
    def patch_format(self, patch_format):
        """Sets the patch_format of this PatchCodeParams.

        PatchCode format. Choose PatchOnly to generate single PatchCode. Use page format to generate Patch page with PatchCodes as borders. Default value: PatchFormat.PatchOnly  # noqa: E501

        :param patch_format: The patch_format of this PatchCodeParams.  # noqa: E501
        :type: PatchFormat
        """

        self._patch_format = patch_format

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
        if issubclass(PatchCodeParams, dict):
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
        if not isinstance(other, PatchCodeParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
