#!/usr/env python
# -*- coding: utf-8 -*-
import unittest
from .. import LBGeo
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
        self.engine = config.ENGINE
        self.session = config.create_scoped_session(self.engine)

    def test_connection(self):
        """
        Test database connection
        """
        db_name = config.DB_NAME
        self.assertEqual(db_name, 'tests_lbgeo')

        conn = self.engine.connect()
        self.assertIsInstance(conn, Connection)

        ses = self.session.begin()
        self.assertIsInstance(ses, SessionTransaction)

    def test_create_db(self):
        """
        Test metadata model loading
        """
        db_name = config.DB_NAME
        self.assertEqual(db_name, 'tests_lbgeo')

        conn = self.engine.connect()
        self.assertIsInstance(conn, Connection)

        result = conn.execute("""
        SELECT name
        FROM estados
        """)

        self.assertGreater(len(result.fetchall()), 0)

    def tearDown(self):
        """
        Remove parameters
        """