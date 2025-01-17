"""title should be unique

Revision ID: bcc5da212dc2
Revises: 6c7a61a83816
Create Date: 2022-05-05 15:17:39.905298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcc5da212dc2'
down_revision = '6c7a61a83816'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'task', ['title'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='unique')
    # ### end Alembic commands ###
