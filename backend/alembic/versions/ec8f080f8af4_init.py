"""init

Revision ID: ec8f080f8af4
Revises: 
Create Date: 2024-09-09 17:13:39.452090

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec8f080f8af4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email_address', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('password_salt', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email_address'), 'user', ['email_address'], unique=True)
    op.create_table('to_do',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_to_do_user_id'), 'to_do', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_to_do_user_id'), table_name='to_do')
    op.drop_table('to_do')
    op.drop_index(op.f('ix_user_email_address'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
