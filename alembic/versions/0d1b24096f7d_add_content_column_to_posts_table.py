"""add content column to posts table

Revision ID: 0d1b24096f7d
Revises: 245fb66a8828
Create Date: 2022-05-04 21:42:31.218969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d1b24096f7d'
down_revision = '245fb66a8828'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts", "content")
