"""empty message

Revision ID: 2458f496cd93
Revises: bcc5da212dc2
Create Date: 2022-05-09 20:16:43.049245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2458f496cd93'
down_revision = 'bcc5da212dc2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(), nullable=True))
    op.add_column('task', sa.Column('goal_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'goal', ['goal_id'], ['goal_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'goal_id')
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###
