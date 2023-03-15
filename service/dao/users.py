"""
Database users API
"""
from aiopg.sa import Engine

from db import const as db_const
from db.models import UsersTable
from service.api.exceptions import NotFound


class DAOUsers:
    """
    Data access object for 'users' table
    """

    def __init__(self, engine: Engine):
        self.engine = engine

    async def add(self, obj: dict) -> str:
        """
        Adds new user to the database

        Args:
            obj: user info to be saved

        Returns:
            email
        """
        async with self.engine.acquire() as conn:
            async with conn.begin():
                await conn.execute(
                    UsersTable.insert().values(**obj)
                )
                return obj[db_const.EMAIL]

    async def get_by_email(self, email: str) -> dict:
        """
        Gets user info by email

        Args:
            email: email to be used for searching

        Returns:
            user info
        """
        async with self.engine.acquire() as conn:
            async with conn.begin():
                row = await (
                    await conn.execute(
                        UsersTable.select().where(
                            UsersTable.c.email == email
                        )
                    )
                ).first()

                if row is None:
                    raise NotFound("Not found")
                return dict(row)
