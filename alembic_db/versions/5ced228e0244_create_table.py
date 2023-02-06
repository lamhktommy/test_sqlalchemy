"""create_table

Revision ID: 5ced228e0244
Revises: 
Create Date: 2023-02-06 16:03:57.846373

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import NUMERIC

# revision identifiers, used by Alembic.
revision = "5ced228e0244"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "data_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("data_value", NUMERIC(asdecimal=False)),
    )


def downgrade() -> None:
    op.drop_table("data_table")
