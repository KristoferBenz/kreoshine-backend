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

from settings import settings

logger = logging.getLogger('app')


async def on_app_start(app):
    """
    Service initialization on application start

    Args:
        app: instance of the application
    """
    app_config = settings['application']
    asyncio.get_event_loop().set_default_executor(ThreadPoolExecutor(max_workers=app_config['thread_pool_size']))

    logger.info('Init Database engine')
    engine = await init_engine()
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


def create_app() -> web.Application:
    """
    Creates web application

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

    utils.create_logger_files()
    logging.config.dictConfig(settings['logging'])

    sys.excepthook = utils.handle_exception

    app.on_startup.append(on_app_start)
    app.on_shutdown.append(on_app_stop)

    return app
