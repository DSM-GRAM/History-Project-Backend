from flask import Blueprint, request, abort
from flask_restful import Api

from app.api import BaseResource
from app.models.map import MapModel

map_blueprint = Blueprint(__name__, __name__)
api = Api(map_blueprint)


@api.resource('/map/<area>')
class MapView(BaseResource):
    def get(self, area):
        map = MapModel.objects(name=area).first()
        return {
            'latitude': map.latitude,
            'longitude': map.longitude
        }, 200
