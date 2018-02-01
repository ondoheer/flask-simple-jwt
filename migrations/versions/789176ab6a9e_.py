"""empty message

Revision ID: 789176ab6a9e
Revises: 7b7ee7dcf76d
Create Date: 2018-02-01 12:46:04.889180

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '789176ab6a9e'
down_revision = '7b7ee7dcf76d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'registered_on')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('registered_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
