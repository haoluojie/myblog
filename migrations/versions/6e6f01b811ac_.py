"""empty message

Revision ID: 6e6f01b811ac
Revises: c2d937b06f82
Create Date: 2017-04-19 23:57:06.719401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e6f01b811ac'
down_revision = 'c2d937b06f82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('wx_img', sa.String(length=200), nullable=True))
    op.add_column('users', sa.Column('wx_unm', sa.String(length=20), nullable=True))
    op.add_column('users', sa.Column('zfb_img', sa.String(length=200), nullable=True))
    op.add_column('users', sa.Column('zfb_unm', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'zfb_unm')
    op.drop_column('users', 'zfb_img')
    op.drop_column('users', 'wx_unm')
    op.drop_column('users', 'wx_img')
    # ### end Alembic commands ###
