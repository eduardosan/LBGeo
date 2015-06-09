#!/usr/env python
# -*- coding: utf-8 -*-
__author__ = 'eduardo'
import logging
from ..model.estados import EstadoBase
from ..model.cities import CitiesBase
from .. import config


log = logging.getLogger()

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
        self.cities_base = CitiesBase(self.session)

    def estados(self):
        """
        Controller to get states JSON
        :return: JSON request with all data
        """
        limit = self.request.params.get('limit')

        return self.base.get_json(limit=limit)

    def city(self):
        """
        Controller to get a JSON with the closest city
        :param: JSON in following format
                {"lat": -15.794087361891,
                 "lng": -47.8879054780313}
        :return: JSON with city data
        """
        try:
            data = self.request.json_body
        except ValueError as e:
            log.error("Error parsing JSON\n%s", e.message)

            error_dict = {
                "error_code": 99,
                'error_message': "Invalid JSON"
            }
            self.request.response.status = 500

            return error_dict

        if data is None:
            error_dict = {
                "error_code": 99,
                'error_message': "Invalid JSON"
            }
            self.request.response.status = 500

            return error_dict
        elif data.get('lat') is None:
            error_dict = {
                "error_code": 1,
                'error_message': "lat is mandatory"
            }
            self.request.response.status = 500

            return error_dict
        elif data.get('lng') is None:
            error_dict = {
                "error_code": 1,
                'error_message': "lng is mandatory"
            }
            self.request.response.status = 500

            return error_dict

        city = self.cities_base.get_city(
            lat=data['lat'],
            lng=data['lng']
        )

        # Get a JSON friendly version
        output = {
            "city_id": city.id,
            "city_name": city.name,
            "city_state_id": city.state_id,
            "state_name": city.state_name,
            "state_short_name": city.state_short_name,
            "state_slug": city.state_slug,
            "city_slug": city.slug,
            "city_lat": city.lat,
            "city_lng": city.lng,
            "city_distance": city.distance
        }

        return output
