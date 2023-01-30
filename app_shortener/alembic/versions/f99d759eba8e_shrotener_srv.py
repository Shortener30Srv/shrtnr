"""shrotener srv

Revision ID: f99d759eba8e
Revises: 
Create Date: 2023-01-30 01:11:05.019317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f99d759eba8e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'shortlink',
        sa.Column('id', sa.String(40), primary_key=True, index=True),
        sa.Column('short_link', sa.String(30), unique=True, nullable=False),
        sa.Column('usual_link', sa.String(4096)),
        sa.Column('modified_on', sa.DateTime),
        sa.Column('valid_up_to', sa.DateTime),
    )


def downgrade() -> None:
    op.drop_table('shortlink')
