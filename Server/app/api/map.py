import os
import json
import urllib.parse
import urllib.request

from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.api import BaseResource
from app.models.main import HistorySiteModel
from app.docs.map import MAP_GET

map_blueprint = Blueprint(__name__, __name__)
api = Api(map_blueprint)


def _decode_address_to_coordinates(address: str):
    url_params = {
        'address': address,
        'key': os.getenv('GEO_KEY')
    }

    url = 'https://maps.googleapis.com/maps/api/geocode/json?' + urllib.parse.urlencode(url_params)
    response = urllib.request.urlopen(url)

    response_body = response.read()
    result = json.loads(response_body.decode())

    if 'status' not in result or result['status'] != 'OK':
        return {}, 204

    else:
        return {
            'lat': result['results'][0]['geometry']['location']['lat'],
            'lng': result['results'][0]['geometry']['location']['lng']
        }


@api.resource('/map/<history_site_code>')
class MapView(BaseResource):
    @swag_from(MAP_GET)
    def get(self, history_site_code: str):
        map = HistorySiteModel.objects(id=history_site_code).first()

        if map is None:
            return '', 204

        return _decode_address_to_coordinates(map.address)


