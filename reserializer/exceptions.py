"""
reserializer.exceptions
"""


class InvalidFormatError(TypeError):
    """
    Raised in :py:meth:`Reserializer.load` if a file_format isn't supported.
    """
    pass


class InvalidStructureError(ValueError):
    """
    Raised in :py:meth:`Reserializer.load` if a file structure is invalid.
    """
    pass
