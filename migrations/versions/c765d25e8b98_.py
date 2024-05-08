"""empty message

Revision ID: c765d25e8b98
Revises: 13cbc51f4847
Create Date: 2024-05-07 15:41:31.062500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c765d25e8b98'
down_revision = '13cbc51f4847'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact_msj', schema=None) as batch_op:
        batch_op.alter_column('comment',
               existing_type=sa.VARCHAR(length=250),
               type_=sa.String(length=600),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact_msj', schema=None) as batch_op:
        batch_op.alter_column('comment',
               existing_type=sa.String(length=600),
               type_=sa.VARCHAR(length=250),
               existing_nullable=False)

    # ### end Alembic commands ###
