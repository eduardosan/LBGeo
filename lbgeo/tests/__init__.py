import os
import os.path
import logging
from .. import config
from .. import LBGeo
from ..model import estados
from ..model import Base

# Set to test environment
config.environment = 'test.ini'

lbg = LBGeo(environment='test.ini')
test_dir = os.path.dirname(os.path.realpath(__file__))
log = logging.getLogger()


def setup_package():
    """
    Setup test data for the package
    """
    Base.metadata.create_all(config.ENGINE)
    pass


def teardown_package():
    """
    Remove test data
    """
    Base.metadata.drop_all(config.ENGINE)
    pass
