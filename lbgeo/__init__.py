#!/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eduardo'
import os
import config
import logging
import logging.config


def load_config(environment='production.ini'):
    here = os.path.abspath(os.path.dirname(__file__))
    config_file = os.path.join(here, '../' + environment)

    config.set_globals(environment)

    # Logging
    logging.config.fileConfig(config_file)


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
        self.Session = config.create_scoped_session(self.engine)
