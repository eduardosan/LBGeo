#!/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eduardo'
from sqlalchemy import ForeignKey
from sqlalchemy.schema import Column, Sequence
from sqlalchemy.types import String, Integer, Unicode, Date, Numeric
from geoalchemy2 import Geometry
from .. import LBGeo
from . import Base


class Estado(Base):
    """
    Class to hold a brazillian state
    """
    __tablename__ = 'estados'
    gid = Column(Integer, Sequence('estados_gid_pkey'), primary_key=True, nullable=False)
    name = Column(Unicode(80), nullable=True)
    descriptio = Column(Unicode(80), nullable=True)
    timestamp = Column(Date, nullable=True)
    begin = Column(Date, nullable=True)
    end = Column(Date, nullable=True)
    altitudemo = Column(Unicode(80), nullable=True)
    tessellate = Column(Numeric(10, 0), nullable=True)
    extrude = Column(Numeric(10, 0), nullable=True)
    visibility = Column(Numeric(10, 0), nullable=True)
    draworder = Column(Numeric(10, 0), nullable=True)
    icon = Column(Unicode(80), nullable=True)

    # Add geometry type
    geom = Column(Geometry('MULTILINESTRING'))

    def __init__(self,
                 geom,
                 name=None,
                 descriptio=None,
                 timestamp=None,
                 begin=None,
                 end=None,
                 date=None,
                 altitudemo=None,
                 tessellate=None,
                 extrude=None,
                 visibility=None,
                 draworder=None,
                 icon=None):
        """
        Building method for the Class
        :param geom: MultiLineString Geometry type
        :param name: Place name
        :param descriptio: Description
        :param timestamp:
        :param begin:
        :param end:
        :param date:
        :param altitudemo:
        :param tessellate:
        :param extrude:
        :param visibility:
        :param draworder:
        :param icon:
        :return:
        """
        self.geom = geom
        self.name = name
        self.descriptio = descriptio
        self.timestamp = timestamp
        self.begin = begin
        self.end = end
        self.date = date
        self.altitudemo = altitudemo
        self.tessellate = tessellate
        self.extrude = extrude
        self.visibility = visibility
        self.draworder = draworder
        self.icon = icon

    def __repr__(self):
        """
        Método que lista os parâmetros da classe
        """
        return "<Estado('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s')>" % (
            self.geom,
            self.name,
            self.descriptio,
            self.timestamp,
            self.begin,
            self.end,
            self.date,
            self.altitudemo,
            self.tessellate,
            self.extrude,
            self.visibility,
            self.draworder,
            self.icon
        )
