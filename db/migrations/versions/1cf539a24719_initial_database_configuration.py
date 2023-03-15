"""Initial database configuration

Revision ID: 1cf539a24719
Revises: 
Create Date: 2023-03-15 20:37:42.471572

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1cf539a24719'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('user_id', sa.String(length=36), nullable=False),
        sa.Column('first_name', sa.String(length=36), nullable=True),
        sa.Column('second_name', sa.String(length=36), nullable=True),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password_hash', sa.String(), nullable=False),

        sa.PrimaryKeyConstraint('user_id', name='user_id__pk'),

    )


def downgrade() -> None:
    op.drop_table('users')

