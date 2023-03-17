"""
Dynaconf app configuration
"""
import platform

from dynaconf import LazySettings

if platform.system() == "Windows":
    settings = LazySettings(
        SETTINGS_FILE_FOR_DYNACONF=[
            "settings/logging.toml",
            'settings/database.toml',
            'settings/app.toml',
            'settings/server.toml'
        ],
        SECRETS='settings/.secrets.toml',
        INCLUDES_FOR_DYNACONF="settings/dev_support/windows.toml"
    )
else:
    settings = LazySettings(
        SETTINGS_FILE_FOR_DYNACONF=[
            "settings/logging.toml",
            'settings/database.toml',
            'settings/app.toml',
            'settings/server.toml'
        ],
        SECRETS='settings/.secrets.toml'
    )
