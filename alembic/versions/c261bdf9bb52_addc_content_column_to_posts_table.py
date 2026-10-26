"""Addc content column to posts table

Revision ID: c261bdf9bb52
Revises: 5a421597208a
Create Date: 2026-10-26 06:05:52.213142

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c261bdf9bb52'
down_revision: Union[str, Sequence[str], None] = '5a421597208a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
