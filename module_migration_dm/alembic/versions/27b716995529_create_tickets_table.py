"""create tickets table

Revision ID: 27b716995529
Revises: 96d8df4e30bf
Create Date: 2026-03-18 12:07:38.438771

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '27b716995529'
down_revision: Union[str, Sequence[str], None] = '96d8df4e30bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_table('ticket')
    # Create ticket table
    op.create_table(
        'ticket',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('type', sa.String(100), nullable=False),
        sa.Column('status', sa.Enum('open', 'running', 'failed', 'success', 'needs_review', name='ticketstatusenum'), nullable=False, server_default='open')
    )

    # Create ticket_action table
    op.create_table(
        'ticket_action',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('ticket_id', sa.Integer, sa.ForeignKey('ticket.id', ondelete='CASCADE'), nullable=False),
        sa.Column('action', sa.String(255), nullable=False),
        sa.Column('success', sa.Boolean, nullable=False, default=False)
    )


def downgrade():
    op.drop_table('ticket_action')
    op.drop_table('ticket')
    sa.Enum(name='ticketstatusenum').drop(op.get_bind(), checkfirst=True)
