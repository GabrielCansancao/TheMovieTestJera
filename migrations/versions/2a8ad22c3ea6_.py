"""empty message

Revision ID: 2a8ad22c3ea6
Revises: 5412db91597f
Create Date: 2021-01-29 01:51:23.199480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a8ad22c3ea6'
down_revision = '5412db91597f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('perfis', sa.Column('contaId', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'perfis', type_='foreignkey')
    op.drop_constraint(None, 'perfis', type_='foreignkey')
    op.create_foreign_key(None, 'perfis', 'conta', ['contaId'], ['id'])
    op.drop_column('perfis', 'conta')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('perfis', sa.Column('conta', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'perfis', type_='foreignkey')
    op.create_foreign_key(None, 'perfis', 'filme', ['filmes'], ['id'])
    op.create_foreign_key(None, 'perfis', 'conta', ['conta'], ['id'])
    op.drop_column('perfis', 'contaId')
    # ### end Alembic commands ###
