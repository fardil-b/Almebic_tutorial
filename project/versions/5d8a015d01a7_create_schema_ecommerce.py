"""create schema ecommerce

Revision ID: 5d8a015d01a7
Revises: 
Create Date: 2024-07-09 10:29:51.287400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d8a015d01a7'
down_revision = None
branch_labels = None
depends_on = None


# alembic does not support creating schema directly and we need to use op.execute
def upgrade() -> None:
    op.execute('CREATE SCHEMA IF NOT EXISTS ecommerce_olist;')


def downgrade() -> None:
    op.execute('DROP SCHEMA IF EXISTS ecommerce_olist CASCADE;')