"""
Database logic
"""
from aiopg.sa import Engine, create_engine


async def init_engine(db_config: dict) -> Engine:
    """
    Initiates database engine

    Returns:
         async engine for postgresql
    """
    assert 'credentials' in db_config
    return await create_engine(
        database=db_config['name'],
        host=db_config['host'],
        user=db_config['credentials']['login'],
        password=db_config['credentials']['password'],
    )
