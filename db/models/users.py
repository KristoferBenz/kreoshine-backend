"""
Model of a 'users' table
"""
from sqlalchemy import Table, MetaData, String, Column, PrimaryKeyConstraint

metadata_obj = MetaData()

UsersTable = Table(
    'tasks',
    metadata_obj,
    Column('user_id', String(length=36), nullable=False),
    Column('first_name', String(length=36), nullable=True),
    Column('second_name', String(length=36), nullable=True),
    Column('email', String(), nullable=False),
    Column('password_hash', String(), nullable=False),

    PrimaryKeyConstraint('user_id', name='user_id__pk')
)
