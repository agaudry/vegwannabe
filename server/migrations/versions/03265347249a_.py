"""empty message

Revision ID: 03265347249a
Revises: 
Create Date: 2020-05-26 10:29:56.838700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "03265347249a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "food",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=True),
        sa.Column("quantity", sa.Integer(), nullable=True),
        sa.Column("date", sa.DateTime(), nullable=True),
        sa.Column("reason", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("food")
    # ### end Alembic commands ###
