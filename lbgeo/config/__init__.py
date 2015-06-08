#!/usr/env python
# -*- coding: utf-8 -*-
__author__ = 'eduardo'
import os
import tempfile
import configparser as ConfigParser
from sqlalchemy.schema import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.engine import create_engine

environment = 'production.ini'

def set_globals():

    config = ConfigParser.ConfigParser()
    here = os.path.abspath(os.path.dirname(__file__))
    config_file = os.path.join(here, '../../' + environment)
    config.read(config_file)

    global INI_FILE

    INI_FILE = config_file

    global DB_URL
    global DB_NAME
    global POOL_SIZE
    global MAX_OVERFLOW
    global TMP_DIR
    global REQUESTS_TIMEOUT

    # Add configuration as environment vars
    DB_URL = os.environ.get('DATABASE_URL', None)
    if DB_URL is None:
        DB_URL = config.get('alembic', 'sqlalchemy.url')
    DB_NAME = DB_URL.split('/')[-1]

    POOL_SIZE = os.environ.get('SQLALCHEMY_POOL_SIZE', None)
    if POOL_SIZE is None:
        POOL_SIZE = int(config.get('lbgeo', 'sqlalchemy.pool_size'))
    else:
        POOL_SIZE = int(POOL_SIZE)

    MAX_OVERFLOW = os.environ.get('SQLALCHEMY_MAX_OVERFLOW', None)
    if MAX_OVERFLOW is None:
        MAX_OVERFLOW = int(config.get('lbgeo', 'sqlalchemy.max_overflow'))
    else:
        MAX_OVERFLOW = int(MAX_OVERFLOW)

    TMP_DIR = os.environ.get('STORAGE_TMP_DIR', None)
    if TMP_DIR is None:
        TMP_DIR = config.get('lbgeo', 'storage.tmp_dir')

    # Eduardo: 20150114
    # Use system tmpdir in worst case scenario
    if not os.path.exists(TMP_DIR):
        TMP_DIR = tempfile.gettempdir()

    REQUESTS_TIMEOUT = os.environ.get('REQUESTS_TIMEOUT', None)
    if REQUESTS_TIMEOUT is None:
        REQUESTS_TIMEOUT = int(config.get('lbgeo', 'requests.timeout'))
    else:
        REQUESTS_TIMEOUT = int(REQUESTS_TIMEOUT)

    global ENGINE
    global METADATA

    ENGINE = create_engine(
        DB_URL,
        pool_size=POOL_SIZE,
        max_overflow=MAX_OVERFLOW,
        echo=True
    )
    METADATA = MetaData(ENGINE)

def create_new_engine():
    """
    Create new connection Engine for SQLAlchemy
    :return: SQLALchemy Engine
    """
    return create_engine(
        globals()['DB_URL'],
        pool_size=globals()['POOL_SIZE'],
        max_overflow=globals()['MAX_OVERFLOW']
    )


def create_scoped_session(engine):
    """
    Get Scoped Session for the engine
    :param engine: SQLALchemy Engine
    :return: SQLALchemy scoped session
    """
    return scoped_session(
        sessionmaker(
            bind=engine,
            autocommit=True
        )
    )
