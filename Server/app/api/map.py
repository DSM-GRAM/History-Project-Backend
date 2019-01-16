from flask import Blueprint, request, abort
from flask_restful import Api
from flasgger import swag_from

from app.api import BaseResource
from app.models.map import MapModel
from app.docs.map import MAP_GET

map_blueprint = Blueprint(__name__, __name__)
api = Api(map_blueprint)


@api.resource('/map/<area>')
class MapView(BaseResource):
    @swag_from(MAP_GET)
    def get(self, area):
        map = MapModel.objects(name=area).first()

        if map is None:
            return '', 204

        return {
            'latitude': map.latitude,
            'longitude': map.longitude
        }, 200
