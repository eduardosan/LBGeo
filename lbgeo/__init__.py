#!/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eduardo'
import os
import config
import logging
import logging.config


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
