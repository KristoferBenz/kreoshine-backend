"""
Service running module
"""
from aiohttp import web

from service.app import create_app
from settings import settings


if __name__ == '__main__':
    app = create_app()
    web.run_app(
        app,
        host=settings['application']['host'],
        port=settings['application']['port'],
        access_log_format=settings.get('access_log_format')
    )
