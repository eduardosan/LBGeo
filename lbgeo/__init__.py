#!/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eduardo'
import os
from . import config
import logging
import logging.config
from pyramid.config import Configurator


def load_config(environment='production.ini'):
    """
    Load configuration
    :param environment: Configuration file name
    """
    config.environment = environment
    config.set_globals()

    # Logging
    logging.config.fileConfig(config.INI_FILE)


class LBGeo(object):
    """
    Global configuration class
    """

    def __init__(self,
                 environment='production.ini'
                 ):
        """
        Construction method
        """
        load_config(environment)

        # SQLAlchemy
        self.engine = config.create_new_engine()
        self.session = config.create_scoped_session(self.engine)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    ini_file = settings['environment'] + ".ini"
    load_config(ini_file)

    cfg = Configurator(settings=settings)

    # Import routes
    from lbgeo.config import routing
    routing.make_routes(cfg)
    cfg.scan()

    return cfg.make_wsgi_app()
