"""
reserializer.api
~~~~~~~~~~~~

This module implements the Reserializer API.
"""

from .exceptions import (
    InvalidFormatError,
)
from .__version__ import __supported_formats__
from .decoder import (
    decode_jaon,
    decode_json,
    decode_xml
)


def load(file_name: str):
    file_format = file_name.split('.')
    file_format = file_format[len(file_format) - 1]

    if file_format not in __supported_formats__:
        raise InvalidFormatError("Reserializer doesn't support", file_format)

    match file_format:
        case 'jaon':
            return decode_jaon(file_name)
        case 'json':
            return decode_json(file_name)
        case 'xml':
            return decode_xml(file_name)
