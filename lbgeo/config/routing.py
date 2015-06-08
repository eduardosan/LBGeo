#!/usr/env python
# -*- coding: utf-8 -*-
__author__ = 'eduardo'

from lbgeo.views import geo


def make_routes(cfg):
    """
    Create module routes
    :param cfg: Configurator object
    """
    cfg.add_static_view('static', 'static', cache_max_age=3600)
    cfg.add_route('home', '/')

    # Get routes
    cfg.add_route('estados', 'estados')
    cfg.add_view(geo.GeoController, attr='estados', route_name='estados',
                 request_method='GET', renderer='json')

    cfg.add_route('city', 'city')
    cfg.add_view(geo.GeoController, attr='city', route_name='city',
                 request_method='POST', renderer='json')
