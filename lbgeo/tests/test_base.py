#!/usr/env python
# -*- coding: utf-8 -*-
import unittest
from .. import LBGeo
from .. import config
from ..model.cities import Cities, CitiesBase
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
        self.cities_base = CitiesBase(self.session)

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

        result = conn.execute("""
        SELECT name
        FROM cities
        """)

        self.assertGreater(len(result.fetchall()), 0)

        result = conn.execute("""
        SELECT name
        FROM states
        """)

        self.assertGreater(len(result.fetchall()), 0)

    def test_geo_query(self):
        """
        Text executing a proximity search using some lat and lng
        """
        # bsb = Cities(
        #    name="Brasília",
        #    slug="brasilia",
        #    state_id=13,
        #    lat=-15.794087361891,
        #    lng=-47.8879054780313
        # )
        city = self.cities_base.get_city(-15.794087361891, -47.8879054780313)
        print("City found: %s", city.name)
        print("Distance: %s", city.distance)

        # This should return Águas Lindas de Goiás
        self.assertEqual(city.id, 212)

    def tearDown(self):
        """
        Remove parameters
        """