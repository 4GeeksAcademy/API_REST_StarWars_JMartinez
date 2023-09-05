"""empty message

Revision ID: 90cefb6b81e0
Revises: ef39d243326f
Create Date: 2023-09-05 19:07:53.736115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90cefb6b81e0'
down_revision = 'ef39d243326f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.alter_column('Activo',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.alter_column('Activo',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)

    # ### end Alembic commands ###