"""empty message

Revision ID: f2aec5fea8d7
Revises: e6963ce1c964
Create Date: 2020-07-19 21:19:39.931997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2aec5fea8d7'
down_revision = 'e6963ce1c964'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chatroom',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=1000), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('id_chatroom', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_chatroom'], ['chatroom.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'body')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message')
    op.drop_table('chatroom')
    # ### end Alembic commands ###