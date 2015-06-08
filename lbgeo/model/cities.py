#!/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eduardo'
import json
from sqlalchemy import ForeignKey
from sqlalchemy.schema import Column, Sequence
from sqlalchemy.types import Integer, Unicode, Float
from . import Base


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

    def __init__(self,
                 name,
                 slug,
                 state_id,
                 lat,
                 lng):
        """
        :param name: City name
        :param slug:  Slug
        :param state_id: State
        :param lat: Latitude (double)
        :param lng: Longitude (double)
        """
        self.name = name
        self.slug = slug
        self.state_id = state_id
        self.lat = lat
        self.lng = lng

    def __repr__(self):
        """
        List class attributes
        """
        return "<State('%s, %s, %s, %s, %s')>" % (
            self.name,
            self.slug,
            self.state_id,
            self.lat,
            self.lng
        )
