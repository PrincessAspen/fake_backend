"""Initial migration

Revision ID: 28a55ae48bd9
Revises: 
Create Date: 2024-10-25 11:46:25.250862

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '28a55ae48bd9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # Commented out as it's unnecessary for identity columns
    # op.alter_column('categories', 'id',
    #        existing_type=sa.BIGINT(),
    #        server_default=None,
    #        type_=sa.Integer(),
    #        existing_nullable=False,
    #        autoincrement=True)
    op.create_index(op.f('ix_categories_id'), 'categories', ['id'], unique=False)
    op.drop_column('categories', 'created_at')
    op.add_column('products', sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('products', sa.Column('price', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('products', sa.Column('quality', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('products', sa.Column('summary', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('products', sa.Column('category_id', sa.Integer(), nullable=True))
    # Commented out as it's unnecessary for identity columns
    # op.alter_column('products', 'id',
    #        existing_type=sa.BIGINT(),
    #        server_default=None,
    #        type_=sa.Integer(),
    #        existing_nullable=False,
    #        autoincrement=True)
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    op.create_foreign_key(None, 'products', 'categories', ['category_id'], ['id'])
    op.drop_column('products', 'created_at')
    # ### end Alembic commands ###
