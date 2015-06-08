import os
import os.path
import logging
from .. import config
from .. import LBGeo
from ..model import estados, cities, states
from ..model import Base


def setup_package():
    """
    Setup test data for the package
    """
    # Set to test environment
    config.environment = 'test.ini'
    lbg = LBGeo(environment='test.ini')

    Base.metadata.create_all(config.ENGINE)

    # Load default data
    here = os.path.abspath(os.path.dirname(__file__))
    sql_file = os.path.join(here, '../../alembic/sql/estados.sql')
    fd = open(sql_file, 'r')

    connection = config.ENGINE.connect()
    result = connection.execute(fd.read())

    cursor = connection.connection.cursor()
    sql_file = os.path.join(here, '../../alembic/sql/states.data')
    fd = open(sql_file, 'r')
    cursor.copy_from(
        fd,
        'states',
        columns=('id', 'name', 'short_name', 'country_id', 'slug')
    )
    cursor.close()

    sql_file = os.path.join(here, '../../alembic/sql/states.sql')
    fd = open(sql_file, 'r')
    result = connection.execute(fd.read())

    # Cities data and model
    cursor = connection.connection.cursor()
    sql_file = os.path.join(here, '../../alembic/sql/cities.data')
    fd = open(sql_file, 'r')
    cursor.copy_from(
        fd,
        'cities',
        columns=('id', 'name', 'lat', 'lng', 'state_id', 'slug')
    )
    cursor.close()

    sql_file = os.path.join(here, '../../alembic/sql/cities.sql')
    fd = open(sql_file, 'r')
    result = connection.execute(fd.read())

    # Load only 100 cities on test
    result = connection.execute("""
    SELECT id, name, slug, lat, lng
    FROM cities
    ORDER BY name
    LIMIT 100
    """)

    for linha in result:
        obj = cities.Cities(
            name=linha[1],
            slug=linha[2],
            lat=linha[3],
            lng=linha[4]
        )

        if obj.lat is not None and obj.lng is not None:
            # Update table with new geometry value
            connection.execute(
                cities.Cities.__table__.update().values(
                    geom=obj.geom
                ).where(
                    cities.Cities.__table__.c.id == linha[0]
                )
            )

    pass


def teardown_package():
    """
    Remove test data
    """
    # Set to test environment
    config.environment = 'test.ini'
    lbg = LBGeo(environment='test.ini')

    connection = config.ENGINE.connect()
    result = connection.execute("""
    ALTER TABLE estados
    ALTER COLUMN gid DROP DEFAULT
    """)

    result = connection.execute("""
    ALTER TABLE cities
    ALTER COLUMN id DROP DEFAULT
    """)

    result = connection.execute("""
    ALTER TABLE states
    ALTER COLUMN id DROP DEFAULT
    """)

    Base.metadata.drop_all(config.ENGINE)
    pass
