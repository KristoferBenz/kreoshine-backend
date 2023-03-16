"""
Application module
"""
import asyncio
import logging
import logging.config
import sys
from concurrent.futures import ThreadPoolExecutor

import aiohttp_cors
from aiohttp import web

from db import init_engine
from service.api import ServicesEndpoint
from service.dao import DAOUsers
from service.app import utils

logger = logging.getLogger('app')


async def on_app_start(app):
    """
    Service initialization on application start

    Args:
        app: instance of the application
    """
    app_config = app['config']['application']

    asyncio.get_event_loop().set_default_executor(ThreadPoolExecutor(max_workers=app_config['thread_pool_size']))

    logger.info('Init Database engine')
    database_config = app_config['postgresql'].copy()
    engine = await init_engine(database_config)
    app['engine'] = engine

    app['dao_inventory'] = DAOUsers(engine)


async def on_app_stop(app) -> None:
    """
    Stops tasks on the application destroy

    Args:
        app: instance of the application
    """
    app['engine'].close()
    await app['engine'].wait_closed()


def create_app(config: dict) -> web.Application:
    """
    Creates web application

    Args:
        config: config represented as a dict
    Returns:
        application
    """
    app = web.Application(client_max_size=1024 ** 3)

    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    cors.add(app.router.add_route('GET', '/services', ServicesEndpoint))

    app['config'] = config
    logging.config.dictConfig(config['logging'])  # fixme: resolve path for a log-file — /var/log/kreoshine/service.log

    sys.excepthook = utils.handle_exception

    app.on_startup.append(on_app_start)
    app.on_shutdown.append(on_app_stop)

    return app
