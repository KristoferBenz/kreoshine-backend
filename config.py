"""
Dynaconf app configuration
"""
from dynaconf import LazySettings

settings = LazySettings(
    SETTINGS_FILE_FOR_DYNACONF=[
        "settings/logging.toml",
        'settings/database.toml',
        'settings/app.toml',
        'settings/server.toml'
    ],
    SECRETS='settings/.secrets.toml'
)
