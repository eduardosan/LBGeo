"""Create point

Revision ID: 938a8b9ffee
Revises: 117575e9547
Create Date: 2015-06-08 01:06:23.379497

"""

# revision identifiers, used by Alembic.
revision = '938a8b9ffee'
down_revision = '117575e9547'
branch_labels = None
depends_on = None

from alembic import op
from lbgeo.model import cities
import sqlalchemy as sa
import logging


log = logging.getLogger()

def upgrade():
    """
    Upgrade to add the geo column
    """
    connection = op.get_bind()

    result = connection.execute("""
    SELECT id, name, slug, lat, lng
    FROM cities
    """)

    for linha in result:
        obj = cities.Cities(
            name=linha[1],
            slug=linha[2],
            lat=linha[3],
            lng=linha[4]
        )

        if obj.lat is not None and obj.lng is not None:
            log.debug("Updating id = %s", linha[0])
            # Update table with new geometry value
            connection.execute(
                cities.Cities.__table__.update().values(
                    geom=obj.geom
                ).where(
                    cities.Cities.__table__.c.id == linha[0]
                )
            )


def downgrade():
    """
    Remove value from all columns
    """
    connection = op.get_bind()
    result = connection.execute("""
    UPDATE cities
    SET geom = NULL
    """)
    pass
