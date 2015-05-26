#!/usr/env python
# -*- coding: utf-8 -*-
import unittest
from .. import LBGeo
from . import lbg
from .. import config
from sqlalchemy.engine import Connection
from sqlalchemy.orm.session import SessionTransaction

class TestBase(unittest.TestCase):
    """
    Testes básicos relativos à conectividade com o PostgreSQL
    """
    def setUp(self):
        """
        Start parameters
        """
        self.geo = lbg

    def test_connection(self):
        """
        Test database connection
        """
        db_name = config.DB_NAME
        self.assertEqual(db_name, 'tests')

        conn = lbg.engine.connect()
        self.assertIsInstance(conn, Connection)

        ses = lbg.session.begin()
        self.assertIsInstance(ses, SessionTransaction)

    def tearDown(self):
        """
        Remove parameters
        """