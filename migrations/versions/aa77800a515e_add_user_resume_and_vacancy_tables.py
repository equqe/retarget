"""Add user, resume and vacancy tables

Revision ID: aa77800a515e
Revises: 
Create Date: 2024-04-30 16:17:59.961429

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa77800a515e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('registered_at', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resume',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_title', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('sex', sa.String(), nullable=False),
    sa.Column('birth_date', sa.String(), nullable=False),
    sa.Column('lived_in', sa.String(), nullable=False),
    sa.Column('want_salary', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('about', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vacancy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_title', sa.String(), nullable=False),
    sa.Column('company', sa.String(), nullable=False),
    sa.Column('work_experience', sa.Integer(), nullable=False),
    sa.Column('work_format', sa.String(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.Column('skills', sa.Integer(), nullable=True),
    sa.Column('about', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vacancy')
    op.drop_table('resume')
    op.drop_table('user')
    # ### end Alembic commands ###
