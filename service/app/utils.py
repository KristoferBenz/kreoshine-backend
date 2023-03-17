"""
Useful function for app creation
"""
import logging
import os.path
import platform
import sys

from config import settings

logger = logging.getLogger('app')


class RootUtils:
    """
    Class with privilege escalation utilities for a Linux-based system
    """

    @property
    def sudo_passwd(self) -> str:
        """ Password of a user with sudo rights on the server """
        return settings["server"]['admin']["sudo_passwd"]

    def create_protect_directory(self, dir_path: str) -> None:
        """ Equivalent of 'mkdirs -p {dir_path}' """
        if platform.system() == "Windows":  # dev support
            try:
                os.makedirs(dir_path)
            except FileExistsError:
                pass
            except PermissionError as err:
                sys.exit(f"\n PermissionError: {err}")

        else:  # target OS is Linux-based
            os.system(command=f"echo {self.sudo_passwd} | sudo -S mkdir -p {dir_path}")

    def touch_protected_file(self, file_path: str) -> None:
        """ Equivalent of 'touch {file_name}'"""
        if platform.system() == "Windows":  # dev support
            try:
                from pathlib import Path
                Path(file_path).touch()
            except PermissionError as err:
                sys.exit(f"\n PermissionError: {err}")

        else:  # target OS is Linux-based
            os.system(command=f"echo {self.sudo_passwd} | sudo -S touch {file_path}")

    def change_file_mode(self, file_path: str, access_rights: str):
        """ Equivalent of 'chmod {access_rights} {file_name}' with privilege escalation for Linux-based system """
        if platform.system() == "Windows":  # dev support
            pass

        else:  # target OS is Linux-based
            os.system(command=f"echo {self.sudo_passwd} | sudo -S chmod {access_rights} {file_path}")


def handle_exception(exc_type, exc_value, exc_traceback) -> None:
    """
    Handler for uncaught exceptions
    """
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.critical("Uncaught exception!", exc_info=(exc_type, exc_value, exc_traceback))


def create_logger_files() -> None:
    """
    Creates logger file for each handler if necessary
    """
    handlers = settings['logging']['handlers']
    root_utils = RootUtils()
    for handler_name, data in handlers.items():
        logger_file = data['filename']
        log_dir = os.path.dirname(logger_file)
        root_utils.create_protect_directory(dir_path=log_dir)
        root_utils.touch_protected_file(file_path=logger_file)
        root_utils.change_file_mode(file_path=logger_file, access_rights='0666')
