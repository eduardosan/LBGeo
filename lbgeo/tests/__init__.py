import os
import os.path
import logging
from .. import config
from .. import LBGeo

# Set to test environment
config.environment = 'test.ini'

lbg = LBGeo(environment='test.ini')
test_dir = os.path.dirname(os.path.realpath(__file__))
log = logging.getLogger()


def setup_package():
    """
    Setup test data for the package
    """
    pass


def teardown_package():
    """
    Remove test data
    """
    pass