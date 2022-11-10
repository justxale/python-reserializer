from .__version__ import (
    __version__,
    __supported_formats__
)

from .api import *
from .exceptions import (
    InvalidFormatError
)
from .decoder import *


def get_version() -> str:
    """
    :returns: Returns version of Reserializer package
    """
    return __version__


def get_supported_formats() -> tuple:
    """
    Returns supported by Reserializer formats
    :returns: Returns supported by Reserializer formats
    """
    return __supported_formats__


def check_format_supporting(file_format: str) -> bool:
    """
    Checks for supporting the format by Reserializer
    :param file_format: A format you want to check
    :returns: True if file_format supported by Reserializer
    """
    if file_format in __supported_formats__:
        return True
    else:
        return False

