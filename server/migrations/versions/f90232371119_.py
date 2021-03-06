"""empty message

Revision ID: f90232371119
Revises: c867ce96cb45
Create Date: 2020-11-16 14:23:08.858034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f90232371119'
down_revision = 'c867ce96cb45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('food', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'food', 'user', ['user_id'], ['id'])
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=512),
               nullable=False)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.create_unique_constraint(None, 'user', ['username'])
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'user', type_='unique')
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=512),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.drop_constraint(None, 'food', type_='foreignkey')
    op.drop_column('food', 'user_id')
    # ### end Alembic commands ###
