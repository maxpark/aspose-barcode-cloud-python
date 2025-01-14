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


class Pdf417Params(object):
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
        "aspect_ratio": "float",
        "text_encoding": "str",
        "columns": "int",
        "compaction_mode": "Pdf417CompactionMode",
        "error_level": "Pdf417ErrorLevel",
        "macro_file_id": "int",
        "macro_segment_id": "int",
        "macro_segments_count": "int",
        "rows": "int",
        "truncate": "bool",
        "pdf417_eci_encoding": "ECIEncodings",
        "is_reader_initialization": "bool",
        "macro_time_stamp": "datetime",
        "macro_sender": "str",
        "macro_file_size": "int",
        "macro_checksum": "int",
        "macro_file_name": "str",
        "macro_addressee": "str",
        "macro_eci_encoding": "ECIEncodings",
        "code128_emulation": "Code128Emulation",
    }

    attribute_map = {
        "aspect_ratio": "AspectRatio",
        "text_encoding": "TextEncoding",
        "columns": "Columns",
        "compaction_mode": "CompactionMode",
        "error_level": "ErrorLevel",
        "macro_file_id": "MacroFileID",
        "macro_segment_id": "MacroSegmentID",
        "macro_segments_count": "MacroSegmentsCount",
        "rows": "Rows",
        "truncate": "Truncate",
        "pdf417_eci_encoding": "Pdf417ECIEncoding",
        "is_reader_initialization": "IsReaderInitialization",
        "macro_time_stamp": "MacroTimeStamp",
        "macro_sender": "MacroSender",
        "macro_file_size": "MacroFileSize",
        "macro_checksum": "MacroChecksum",
        "macro_file_name": "MacroFileName",
        "macro_addressee": "MacroAddressee",
        "macro_eci_encoding": "MacroECIEncoding",
        "code128_emulation": "Code128Emulation",
    }

    def __init__(
        self,
        aspect_ratio=None,
        text_encoding=None,
        columns=None,
        compaction_mode=None,
        error_level=None,
        macro_file_id=None,
        macro_segment_id=None,
        macro_segments_count=None,
        rows=None,
        truncate=None,
        pdf417_eci_encoding=None,
        is_reader_initialization=None,
        macro_time_stamp=None,
        macro_sender=None,
        macro_file_size=None,
        macro_checksum=None,
        macro_file_name=None,
        macro_addressee=None,
        macro_eci_encoding=None,
        code128_emulation=None,
    ):  # noqa: E501
        """Pdf417Params - a model defined in Swagger"""  # noqa: E501

        self._aspect_ratio = None
        self._text_encoding = None
        self._columns = None
        self._compaction_mode = None
        self._error_level = None
        self._macro_file_id = None
        self._macro_segment_id = None
        self._macro_segments_count = None
        self._rows = None
        self._truncate = None
        self._pdf417_eci_encoding = None
        self._is_reader_initialization = None
        self._macro_time_stamp = None
        self._macro_sender = None
        self._macro_file_size = None
        self._macro_checksum = None
        self._macro_file_name = None
        self._macro_addressee = None
        self._macro_eci_encoding = None
        self._code128_emulation = None
        self.discriminator = None

        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if text_encoding is not None:
            self.text_encoding = text_encoding
        if columns is not None:
            self.columns = columns
        if compaction_mode is not None:
            self.compaction_mode = compaction_mode
        if error_level is not None:
            self.error_level = error_level
        if macro_file_id is not None:
            self.macro_file_id = macro_file_id
        if macro_segment_id is not None:
            self.macro_segment_id = macro_segment_id
        if macro_segments_count is not None:
            self.macro_segments_count = macro_segments_count
        if rows is not None:
            self.rows = rows
        if truncate is not None:
            self.truncate = truncate
        if pdf417_eci_encoding is not None:
            self.pdf417_eci_encoding = pdf417_eci_encoding
        if is_reader_initialization is not None:
            self.is_reader_initialization = is_reader_initialization
        if macro_time_stamp is not None:
            self.macro_time_stamp = macro_time_stamp
        if macro_sender is not None:
            self.macro_sender = macro_sender
        if macro_file_size is not None:
            self.macro_file_size = macro_file_size
        if macro_checksum is not None:
            self.macro_checksum = macro_checksum
        if macro_file_name is not None:
            self.macro_file_name = macro_file_name
        if macro_addressee is not None:
            self.macro_addressee = macro_addressee
        if macro_eci_encoding is not None:
            self.macro_eci_encoding = macro_eci_encoding
        if code128_emulation is not None:
            self.code128_emulation = code128_emulation

    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this Pdf417Params.  # noqa: E501

        Height/Width ratio of 2D BarCode module.  # noqa: E501

        :return: The aspect_ratio of this Pdf417Params.  # noqa: E501
        :rtype: float
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this Pdf417Params.

        Height/Width ratio of 2D BarCode module.  # noqa: E501

        :param aspect_ratio: The aspect_ratio of this Pdf417Params.  # noqa: E501
        :type: float
        """

        self._aspect_ratio = aspect_ratio

    @property
    def text_encoding(self):
        """Gets the text_encoding of this Pdf417Params.  # noqa: E501

        Encoding of codetext.  # noqa: E501

        :return: The text_encoding of this Pdf417Params.  # noqa: E501
        :rtype: str
        """
        return self._text_encoding

    @text_encoding.setter
    def text_encoding(self, text_encoding):
        """Sets the text_encoding of this Pdf417Params.

        Encoding of codetext.  # noqa: E501

        :param text_encoding: The text_encoding of this Pdf417Params.  # noqa: E501
        :type: str
        """

        self._text_encoding = text_encoding

    @property
    def columns(self):
        """Gets the columns of this Pdf417Params.  # noqa: E501

        Columns count.  # noqa: E501

        :return: The columns of this Pdf417Params.  # noqa: E501
        :rtype: int
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this Pdf417Params.

        Columns count.  # noqa: E501

        :param columns: The columns of this Pdf417Params.  # noqa: E501
        :type: int
        """

        self._columns = columns

    @property
    def compaction_mode(self):
        """Gets the compaction_mode of this Pdf417Params.  # noqa: E501

        Pdf417 symbology type of BarCode's compaction mode. Default value: Pdf417CompactionMode.Auto.  # noqa: E501

        :return: The compaction_mode of this Pdf417Params.  # noqa: E501
        :rtype: Pdf417CompactionMode
        """
        return self._compaction_mode

    @compaction_mode.setter
    def compaction_mode(self, compaction_mode):
        """Sets the compaction_mode of this Pdf417Params.

        Pdf417 symbology type of BarCode's compaction mode. Default value: Pdf417CompactionMode.Auto.  # noqa: E501

        :param compaction_mode: The compaction_mode of this Pdf417Params.  # noqa: E501
        :type: Pdf417CompactionMode
        """

        self._compaction_mode = compaction_mode

    @property
    def error_level(self):
        """Gets the error_level of this Pdf417Params.  # noqa: E501

        Pdf417 symbology type of BarCode's error correction level ranging from level0 to level8, level0 means no error correction info, level8 means best error correction which means a larger picture.  # noqa: E501

        :return: The error_level of this Pdf417Params.  # noqa: E501
        :rtype: Pdf417ErrorLevel
        """
        return self._error_level

    @error_level.setter
    def error_level(self, error_level):
        """Sets the error_level of this Pdf417Params.

        Pdf417 symbology type of BarCode's error correction level ranging from level0 to level8, level0 means no error correction info, level8 means best error correction which means a larger picture.  # noqa: E501

        :param error_level: The error_level of this Pdf417Params.  # noqa: E501
        :type: Pdf417ErrorLevel
        """

        self._error_level = error_level

    @property
    def macro_file_id(self):
        """Gets the macro_file_id of this Pdf417Params.  # noqa: E501

        Macro Pdf417 barcode's file ID. Used for MacroPdf417.  # noqa: E501

        :return: The macro_file_id of this Pdf417Params.  # noqa: E501
        :rtype: int
        """
        return self._macro_file_id

    @macro_file_id.setter
    def macro_file_id(self, macro_file_id):
        """Sets the macro_file_id of this Pdf417Params.

        Macro Pdf417 barcode's file ID. Used for MacroPdf417.  # noqa: E501

        :param macro_file_id: The macro_file_id of this Pdf417Params.  # noqa: E501
        :type: int
        """

        self._macro_file_id = macro_file_id

    @property
    def macro_segment_id(self):
        """Gets the macro_segment_id of this Pdf417Params.  # noqa: E501

        Macro Pdf417 barcode's segment ID, which starts from 0, to MacroSegmentsCount - 1.  # noqa: E501

        :return: The macro_segment_id of this Pdf417Params.  # noqa: E501
        :rtype: int
        """
        return self._macro_segment_id

    @macro_segment_id.setter
    def macro_segment_id(self, macro_segment_id):
        """Sets the macro_segment_id of this Pdf417Params.

        Macro Pdf417 barcode's segment ID, which starts from 0, to MacroSegmentsCount - 1.  # noqa: E501

        :param macro_segment_id: The macro_segment_id of this Pdf417Params.  # noqa: E501
        :type: int
        """

        self._macro_segment_id = macro_segment_id

    @property
    def macro_segments_count(self):
        """Gets the macro_segments_count of this Pdf417Params.  # noqa: E501

        Macro Pdf417 barcode segments count.  # noqa: E501

        :return: The macro_segments_count of this Pdf417Params.  # noqa: E501
        :rtype: int
        """
        return self._macro_segments_count

    @macro_segments_count.setter
    def macro_segments_count(self, macro_segments_count):
        """Sets the macro_segments_count of this Pdf417Params.

        Macro Pdf417 barcode segments count.  # noqa: E501

        :param macro_segments_count: The macro_segments_count of this Pdf417Params.  # noqa: E501
        :type: int
        """

        self._macro_segments_count = macro_segments_count

    @property
    def rows(self):
        """Gets the rows of this Pdf417Params.  # noqa: E501

        Rows count.  # noqa: E501

        :return: The rows of this Pdf417Params.  # noqa: E501
        :rtype: int
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this Pdf417Params.

        Rows count.  # noqa: E501

        :param rows: The rows of this Pdf417Params.  # noqa: E501
        :type: int
        """

        self._rows = rows

    @property
    def truncate(self):
        """Gets the truncate of this Pdf417Params.  # noqa: E501

        Whether Pdf417 symbology type of BarCode is truncated (to reduce space).  # noqa: E501

        :return: The truncate of this Pdf417Params.  # noqa: E501
        :rtype: bool
        """
        return self._truncate

    @truncate.setter
    def truncate(self, truncate):
        """Sets the truncate of this Pdf417Params.

        Whether Pdf417 symbology type of BarCode is truncated (to reduce space).  # noqa: E501

        :param truncate: The truncate of this Pdf417Params.  # noqa: E501
        :type: bool
        """

        self._truncate = truncate

    @property
    def pdf417_eci_encoding(self):
        """Gets the pdf417_eci_encoding of this Pdf417Params.  # noqa: E501

        Extended Channel Interpretation Identifiers. It is used to tell the barcode reader details about the used references for encoding the data in the symbol. Current implementation consists all well known charset encodings.  # noqa: E501

        :return: The pdf417_eci_encoding of this Pdf417Params.  # noqa: E501
        :rtype: ECIEncodings
        """
        return self._pdf417_eci_encoding

    @pdf417_eci_encoding.setter
    def pdf417_eci_encoding(self, pdf417_eci_encoding):
        """Sets the pdf417_eci_encoding of this Pdf417Params.

        Extended Channel Interpretation Identifiers. It is used to tell the barcode reader details about the used references for encoding the data in the symbol. Current implementation consists all well known charset encodings.  # noqa: E501

        :param pdf417_eci_encoding: The pdf417_eci_encoding of this Pdf417Params.  # noqa: E501
        :type: ECIEncodings
        """

        self._pdf417_eci_encoding = pdf417_eci_encoding

    @property
    def is_reader_initialization(self):
        """Gets the is_reader_initialization of this Pdf417Params.  # noqa: E501

        Used to instruct the reader to interpret the data contained within the symbol as programming for reader initialization  # noqa: E501

        :return: The is_reader_initialization of this Pdf417Params.  # noqa: E501
        :rtype: bool
        """
        return self._is_reader_initialization

    @is_reader_initialization.setter
    def is_reader_initialization(self, is_reader_initialization):
        """Sets the is_reader_initialization of this Pdf417Params.

        Used to instruct the reader to interpret the data contained within the symbol as programming for reader initialization  # noqa: E501

        :param is_reader_initialization: The is_reader_initialization of this Pdf417Params.  # noqa: E501
        :type: bool
        """

        self._is_reader_initialization = is_reader_initialization

    @property
    def macro_time_stamp(self):
        """Gets the macro_time_stamp of this Pdf417Params.  # noqa: E501

        Macro Pdf417 barcode time stamp  # noqa: E501

        :return: The macro_time_stamp of this Pdf417Params.  # noqa: E501
        :rtype: datetime
        """
        return self._macro_time_stamp

    @macro_time_stamp.setter
    def macro_time_stamp(self, macro_time_stamp):
        """Sets the macro_time_stamp of this Pdf417Params.

        Macro Pdf417 barcode time stamp  # noqa: E501

        :param macro_time_stamp: The macro_time_stamp of this Pdf417Params.  # noqa: E501
        :type: datetime
        """

        self._macro_time_stamp = macro_time_stamp

    @property
    def macro_sender(self):
        """Gets the macro_sender of this Pdf417Params.  # noqa: E501

        Macro Pdf417 barcode sender name  # noqa: E501

        :return: The macro_sender of this Pdf417Params.  # noqa: E501
        :rtype: str
        """
        return self._macro_sender

    @macro_sender.setter
    def macro_sender(self, macro_sender):
        """Sets the macro_sender of this Pdf417Params.

        Macro Pdf417 barcode sender name  # noqa: E501

        :param macro_sender: The macro_sender of this Pdf417Params.  # noqa: E501
        :type: str
        """

        self._macro_sender = macro_sender

    @property
    def macro_file_size(self):
        """Gets the macro_file_size of this Pdf417Params.  # noqa: E501

        Macro Pdf417 file size. The file size field contains the size in bytes of the entire source file  # noqa: E501

        :return: The macro_file_size of this Pdf417Params.  # noqa: E501
        :rtype: int
        """
        return self._macro_file_size

    @macro_file_size.setter
    def macro_file_size(self, macro_file_size):
        """Sets the macro_file_size of this Pdf417Params.

        Macro Pdf417 file size. The file size field contains the size in bytes of the entire source file  # noqa: E501

        :param macro_file_size: The macro_file_size of this Pdf417Params.  # noqa: E501
        :type: int
        """

        self._macro_file_size = macro_file_size

    @property
    def macro_checksum(self):
        """Gets the macro_checksum of this Pdf417Params.  # noqa: E501

        Macro Pdf417 barcode checksum. The checksum field contains the value of the 16-bit (2 bytes) CRC checksum using the CCITT-16 polynomial  # noqa: E501

        :return: The macro_checksum of this Pdf417Params.  # noqa: E501
        :rtype: int
        """
        return self._macro_checksum

    @macro_checksum.setter
    def macro_checksum(self, macro_checksum):
        """Sets the macro_checksum of this Pdf417Params.

        Macro Pdf417 barcode checksum. The checksum field contains the value of the 16-bit (2 bytes) CRC checksum using the CCITT-16 polynomial  # noqa: E501

        :param macro_checksum: The macro_checksum of this Pdf417Params.  # noqa: E501
        :type: int
        """

        self._macro_checksum = macro_checksum

    @property
    def macro_file_name(self):
        """Gets the macro_file_name of this Pdf417Params.  # noqa: E501

        Macro Pdf417 barcode file name  # noqa: E501

        :return: The macro_file_name of this Pdf417Params.  # noqa: E501
        :rtype: str
        """
        return self._macro_file_name

    @macro_file_name.setter
    def macro_file_name(self, macro_file_name):
        """Sets the macro_file_name of this Pdf417Params.

        Macro Pdf417 barcode file name  # noqa: E501

        :param macro_file_name: The macro_file_name of this Pdf417Params.  # noqa: E501
        :type: str
        """

        self._macro_file_name = macro_file_name

    @property
    def macro_addressee(self):
        """Gets the macro_addressee of this Pdf417Params.  # noqa: E501

        Macro Pdf417 barcode addressee name  # noqa: E501

        :return: The macro_addressee of this Pdf417Params.  # noqa: E501
        :rtype: str
        """
        return self._macro_addressee

    @macro_addressee.setter
    def macro_addressee(self, macro_addressee):
        """Sets the macro_addressee of this Pdf417Params.

        Macro Pdf417 barcode addressee name  # noqa: E501

        :param macro_addressee: The macro_addressee of this Pdf417Params.  # noqa: E501
        :type: str
        """

        self._macro_addressee = macro_addressee

    @property
    def macro_eci_encoding(self):
        """Gets the macro_eci_encoding of this Pdf417Params.  # noqa: E501

        Extended Channel Interpretation Identifiers. Applies for Macro PDF417 text fields.  # noqa: E501

        :return: The macro_eci_encoding of this Pdf417Params.  # noqa: E501
        :rtype: ECIEncodings
        """
        return self._macro_eci_encoding

    @macro_eci_encoding.setter
    def macro_eci_encoding(self, macro_eci_encoding):
        """Sets the macro_eci_encoding of this Pdf417Params.

        Extended Channel Interpretation Identifiers. Applies for Macro PDF417 text fields.  # noqa: E501

        :param macro_eci_encoding: The macro_eci_encoding of this Pdf417Params.  # noqa: E501
        :type: ECIEncodings
        """

        self._macro_eci_encoding = macro_eci_encoding

    @property
    def code128_emulation(self):
        """Gets the code128_emulation of this Pdf417Params.  # noqa: E501

        Function codeword for Code 128 emulation. Applied for MicroPDF417 only. Ignored for PDF417 and MacroPDF417 barcodes.  # noqa: E501

        :return: The code128_emulation of this Pdf417Params.  # noqa: E501
        :rtype: Code128Emulation
        """
        return self._code128_emulation

    @code128_emulation.setter
    def code128_emulation(self, code128_emulation):
        """Sets the code128_emulation of this Pdf417Params.

        Function codeword for Code 128 emulation. Applied for MicroPDF417 only. Ignored for PDF417 and MacroPDF417 barcodes.  # noqa: E501

        :param code128_emulation: The code128_emulation of this Pdf417Params.  # noqa: E501
        :type: Code128Emulation
        """

        self._code128_emulation = code128_emulation

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
        if issubclass(Pdf417Params, dict):
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
        if not isinstance(other, Pdf417Params):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
