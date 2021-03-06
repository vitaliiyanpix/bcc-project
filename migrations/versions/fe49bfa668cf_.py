"""empty message

Revision ID: fe49bfa668cf
Revises: 6a3b194eace3
Create Date: 2019-12-24 16:17:52.278429

"""

from datetime import datetime, timezone

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'fe49bfa668cf'
down_revision = '6a3b194eace3'
branch_labels = None
depends_on = None


def populate_billing_cycles(billing_cycles):
    op.bulk_insert(billing_cycles, [
        {
            'id': 1,
            'start_date': datetime(2019, 8, 1, tzinfo=timezone.utc),
            'end_date': datetime(2019, 9, 1, tzinfo=timezone.utc),
        },
        {
            'id': 2,
            'start_date': datetime(2019, 9, 1, tzinfo=timezone.utc),
            'end_date': datetime(2019, 10, 1, tzinfo=timezone.utc),
        },
        {
            'id': 3,
            'start_date': datetime(2019, 10, 1, tzinfo=timezone.utc),
            'end_date': datetime(2019, 11, 1, tzinfo=timezone.utc),
        }
    ])


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    billing_cycles = op.create_table('billing_cycles',
                                     sa.Column('id', sa.Integer(), nullable=False),
                                     sa.Column('start_date', sa.TIMESTAMP(timezone=True), nullable=True),
                                     sa.Column('end_date', sa.TIMESTAMP(timezone=True), nullable=True),
                                     sa.PrimaryKeyConstraint('id')
                                     )
    populate_billing_cycles(billing_cycles)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('billing_cycles')
    # ### end Alembic commands ###
