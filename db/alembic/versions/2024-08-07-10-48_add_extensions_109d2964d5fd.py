"""add_extensions

Revision ID: 109d2964d5fd
Revises: 
Create Date: 2024-03-05 12:51:54.618052+03:00

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "109d2964dfd"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')


def downgrade():
    op.execute('DROP EXTENSION IF EXISTS "uuid-ossp"')
