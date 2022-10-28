"""Add a column

Revision ID: 55e0355affab
Revises: 
Create Date: 2022-10-27 23:58:20.364463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55e0355affab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('phonebook', sa.Column('email', sa.String(50)))


def downgrade() -> None:
    op.drop_column('phonebook', 'email')
