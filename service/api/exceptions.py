"""
REST-API exceptions
"""


class NotFound(Exception):
    """
    Raised when a resource is not found
    """
    status_code = 404
    error_message = "Resource is not found"
