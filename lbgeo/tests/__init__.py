import os
import os.path
import logging
from .. import config
from .. import LBGeo
from ..model import estados
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
    Base.metadata.drop_all(config.ENGINE)
    pass
