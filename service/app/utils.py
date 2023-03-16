"""
Useful function for app creation
"""
import logging
import sys

logger = logging.getLogger('app')


def handle_exception(exc_type, exc_value, exc_traceback) -> None:
    """
    Handler for uncaught exceptions
    """
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.critical("Uncaught exception!", exc_info=(exc_type, exc_value, exc_traceback))
