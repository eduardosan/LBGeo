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

    # States data and model
    cursor = connection.connection.cursor()
    sql_file = os.path.join(here, '../sql/states.data')
    fd = open(sql_file, 'r')
    cursor.copy_from(
        fd,
        'states',
        columns=('id', 'name', 'short_name', 'country_id', 'slug')
    )
    cursor.close()

    sql_file = os.path.join(here, '../sql/states.sql')
    fd = open(sql_file, 'r')
    result = connection.execute(fd.read())

    # Cities data and model
    cursor = connection.connection.cursor()
    sql_file = os.path.join(here, '../sql/cities.data')
    fd = open(sql_file, 'r')
    cursor.copy_from(
        fd,
        'cities',
        columns=('id', 'name', 'lat', 'lng', 'state_id', 'slug')
    )
    cursor.close()

    sql_file = os.path.join(here, '../sql/cities.sql')
    fd = open(sql_file, 'r')
    result = connection.execute(fd.read())

    pass


def downgrade():
    connection = op.get_bind()
    result = connection.execute(
        "DELETE FROM estados"
    )

    result = connection.execute(
        "DELETE FROM states"
    )

    result = connection.execute(
        "DELETE FROM cities"
    )

    pass
