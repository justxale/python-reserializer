"""
reserializer.api
~~~~~~~~~~~~

This module implements the Reserializer API.
"""

from typing import NewType, IO
from .exceptions import (
    InvalidFormatError,
    InvalidStructureError
)
from .__version__ import __supported_formats__
from .decoder import ReserializerDecoder, decode

# TODO: Remake API
def load(file_name: str):
    return decode(file_name)
