"""Added Todo List and relationship between Item and List

Revision ID: 4917cec0b456
Revises: c6a42e8abb37
Create Date: 2021-07-05 15:37:36.919626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4917cec0b456'
down_revision = 'c6a42e8abb37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('list',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('done', sa.BOOLEAN(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todo', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todo', 'list', ['list_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todo', type_='foreignkey')
    op.drop_column('todo', 'list_id')
    op.drop_table('list')
    # ### end Alembic commands ###