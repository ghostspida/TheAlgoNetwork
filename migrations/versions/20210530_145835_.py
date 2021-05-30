"""empty message

Revision ID: 026090f2e1e7
Revises: dcf857e540e8
Create Date: 2021-05-30 14:58:35.465032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '026090f2e1e7'
down_revision = 'dcf857e540e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('solved',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('problem_solved', sa.Boolean(), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.Column('problems_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['problems_id'], ['problems.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('reviews')
    op.drop_column('problems', 'solved')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('problems', sa.Column('solved', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.create_table('reviews',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('users_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('problems_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['problems_id'], ['problems.id'], name='reviews_problems_id_fkey'),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], name='reviews_users_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='reviews_pkey')
    )
    op.drop_table('solved')
    # ### end Alembic commands ###
