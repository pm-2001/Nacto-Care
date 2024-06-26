"""empty message

Revision ID: 42ce299d6094
Revises: 6b840cfc6ea9
Create Date: 2024-05-19 21:33:29.369552

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision: str = '42ce299d6094'
down_revision: Union[str, None] = '6b840cfc6ea9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

CITY = [
    ('MUMBAI', 'mumbai'),
    ('DELHI', 'delhi'),
    ('AHMEDABAD', 'ahmedabad'),
    ('BANGALORE', 'bangalore'),
    ('CHENNAI', 'chennai')
]



def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nurses',
    sa.Column('nurse_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('nurse_name', sa.String(), nullable=True),
    sa.Column('nurse_email', sa.String(), nullable=True),
    sa.Column('nurse_city', sqlalchemy_utils.types.choice.ChoiceType(CITY), nullable=True),
    sa.Column('nurse_created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('nurse_dob', sa.Date(), nullable=True),
    sa.Column('nurse_phone_number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('nurse_id'),
    sa.UniqueConstraint('nurse_email'),
    sa.UniqueConstraint('nurse_phone_number')
    )
    op.create_table('patients',
    sa.Column('patient_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('patient_name', sa.String(), nullable=True),
    sa.Column('patient_email', sa.String(), nullable=True),
    sa.Column('patient_created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('patient_dob', sa.Date(), nullable=True),
    sa.Column('patient_phone_number', sa.String(), nullable=True),
    sa.Column('patient_address', sa.String(), nullable=True),
    sa.Column('patient_city', sqlalchemy_utils.types.choice.ChoiceType(CITY), nullable=True),
    sa.PrimaryKeyConstraint('patient_id'),
    sa.UniqueConstraint('patient_email'),
    sa.UniqueConstraint('patient_phone_number')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patients')
    op.drop_table('nurses')
    # ### end Alembic commands ###
