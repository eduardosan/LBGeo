#!/usr/env python
# -*- coding: utf-8 -*-
__author__ = 'eduardo'
from ..model.estados import EstadoBase
from .. import config

class GeoController(object):
    """
    Geo information controller
    """
    def __init__(self, request):
        """
        Contructor for controller
        :param request: Pyramid request
        :return:
        """
        self.request = request
        self.session = config.create_scoped_session(config.ENGINE)
        self.base = EstadoBase(self.session)

    def estados(self):
        """
        Controller to get states JSON
        :return: JSON request with all data
        """
        limit = self.request.params.get('limit')

        return self.base.get_json(limit=limit)
