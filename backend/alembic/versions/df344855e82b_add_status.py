"""add status

Revision ID: df344855e82b
Revises: ec8f080f8af4
Create Date: 2024-09-10 20:05:45.298644

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df344855e82b'
down_revision: Union[str, None] = 'ec8f080f8af4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('to_do', sa.Column('status', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('to_do', 'status')
    # ### end Alembic commands ###
