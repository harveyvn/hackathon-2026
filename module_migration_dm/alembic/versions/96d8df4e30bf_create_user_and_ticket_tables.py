"""create user and ticket tables

Revision ID: 96d8df4e30bf
Revises: 7c22d61f7a4b
Create Date: 2026-03-17 17:53:11.099594

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96d8df4e30bf'
down_revision: Union[str, Sequence[str], None] = '7c22d61f7a4b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True)
    )
    op.create_table(
        'ticket',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('description', sa.String(length=255), nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'))
    )

def downgrade():
    op.drop_table('ticket')
    op.drop_table('user')

