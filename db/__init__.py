"""
Database logic
"""
from aiopg.sa import Engine, create_engine

from settings import settings


async def init_engine() -> Engine:
    """
    Initiates database engine

    Returns:
         async engine for postgresql
    """
    return await create_engine(
        database=settings['postgresql']['name'],  # fixme: initialize database (locally)
        host=settings['postgresql']['host'],
        user=settings['postgresql']['credentials']['login'],
        password=settings['postgresql']['credentials']['password'],
    )
