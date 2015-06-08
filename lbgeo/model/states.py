#!/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eduardo'
import json
from sqlalchemy.schema import Column, Sequence
from sqlalchemy.types import Integer, Unicode
from . import Base


class State(Base):
    """
    Other Brazillian state database
    """
    __tablename__ = 'states'
    id = Column(Integer, Sequence('states_id_seq'), primary_key=True, nullable=False)
    name = Column(Unicode(30), nullable=False)
    short_name = Column(Unicode(4), nullable=True)
    country_id = Column(Integer, nullable=True)
    slug = Column(Unicode(255), nullable=False)

    def __init__(self,
                 name,
                 slug,
                 short_name=None,
                 country_id=None):
        """
        :param name: State name
        :param slug: State slug
        :param short_name: Short name (sigla)
        :param country_id:
        """
        self.name = name
        self.slug = slug
        self.short_name = short_name
        self.country_id = country_id

    def __repr__(self):
        """
        List class attributes
        """
        return "<State('%s, %s, %s, %s')>" % (
            self.name,
            self.slug,
            self.short_name,
            self.country_id
        )

class StateBase(object):
    """
    State object base
    """
    def __init__(self, session):
        """
        Constructor
        :param session: SQLAlchemy scoped session
        """
        self.session = session