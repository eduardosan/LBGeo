#!/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eduardo'
import json
from sqlalchemy import ForeignKey
from sqlalchemy.schema import Column, Sequence
from sqlalchemy.types import Integer, Unicode, Float
from sqlalchemy import func
from geoalchemy2 import Geometry
from . import Base
from .states import State


class Cities(Base):
    """
    Cities database
    """
    __tablename__ = 'cities'
    id = Column(Integer, Sequence('cities_id_seq'), primary_key=True, nullable=False)
    name = Column(Unicode(255), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=True)
    slug = Column(Unicode(255), nullable=False)
    lat = Column(Float, nullable=True)
    lng = Column(Float, nullable=True)

    # Add geometry type
    geom = Column(Geometry(), nullable=True)

    def __init__(self,
                 name,
                 slug,
                 state_id=None,
                 lat=None,
                 lng=None,
                 geom=None):
        """
        :param name: City name
        :param slug:  Slug
        :param state_id: State
        :param lat: Latitude (double)
        :param lng: Longitude (double)
        :param geom: Geometry from latitude and longitude
        """
        self.name = name
        self.slug = slug
        self.state_id = state_id
        self.lat = lat
        self.lng = lng

        # Geom point type
        if geom is None:
            self.geom = func.ST_MakePoint(self.lng, self.lat)
        else:
            self.geom = geom

    def __repr__(self):
        """
        List class attributes
        """
        return "<State('%s, %s, %s, %s, %s, %s')>" % (
            self.name,
            self.slug,
            self.state_id,
            self.lat,
            self.lng,
            self.geom
        )


class CitiesBase(object):
    """
    Base de objetos do estado
    """
    def __init__(self, session):
        """
        Constructor
        :param session: SQLAlchemy scoped session
        """
        self.session = session

    def get_city(self, lat, lng):
        """
        Get nearby city for this lat and long
        :param lat: Latitude
        :param lng: Longitude
        :return: City object
        """
        point = func.ST_MakePoint(lng, lat)
        city = self.session.query(
            Cities.id,
            Cities.name,
            Cities.state_id,
            State.name.label('state_name'),
            State.short_name.label('state_short_name'),
            State.slug.label('state_slug'),
            Cities.slug,
            Cities.lat,
            Cities.lng,
            Cities.geom,
            func.ST_Distance_Sphere(
                point,
                Cities.__table__.c.geom
            ).label('distance')
        ).join(State).order_by(
            func.ST_Distance_Sphere(
                point,
                Cities.__table__.c.geom
            )
        ).limit(1).first()

        return city
