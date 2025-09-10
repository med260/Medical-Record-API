"""fix_patient_roles

Revision ID: 4185cc3803a8
Revises: 49a5f2e68d93
Create Date: 2025-09-10 18:05:41.122276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4185cc3803a8'
down_revision: Union[str, Sequence[str], None] = '49a5f2e68d93'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("UPDATE users SET role = 'patient' WHERE id IN (SELECT id FROM patients)")

def downgrade():
    op.execute("UPDATE users SET role = 'user' WHERE id IN (SELECT id FROM patients)")

