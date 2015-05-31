"""Load estados data

Revision ID: 117575e9547
Revises: 00000000000
Create Date: 2015-05-31 16:52:44.890013

"""

# revision identifiers, used by Alembic.
revision = '117575e9547'
down_revision = '00000000000'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import os.path


def upgrade():
    here = os.path.abspath(os.path.dirname(__file__))
    sql_file = os.path.join(here, '../sql/estados.sql')
    fd = open(sql_file, 'r')

    connection = op.get_bind()
    result = connection.execute(fd.read())

    pass


def downgrade():
    connection = op.get_bind()
    result = connection.execute(
        "DELETE FROM estados"
    )

    pass
