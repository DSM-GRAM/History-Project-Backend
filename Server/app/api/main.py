from flask import Blueprint, abort, request
from flask_restful import Api
from flasgger import swag_from

from app.api import BaseResource
from app.models.main import HistorySiteModel
from app.docs.main import MAIN_GET, AREA_GET

main_blueprint = Blueprint(__name__, __name__)
api = Api(main_blueprint)


@api.resource('/main/<area>')
class LocationView(BaseResource):
    @swag_from(MAIN_GET)
    def get(self, area):
        all_location = HistorySiteModel.objects(area=area).all()

        if area != "bla" and area != "usu":
            abort(401)

        return self.unicode_safe_json_dumps([
            {
                "historicalSiteName": historic_site.name,
                "historicalSiteLocation": historic_site.location,
                "historicalSiteImagePath": historic_site.image_path,
                "historicalSiteCode": historic_site.id
            } for historic_site in all_location
        ])


@api.resource('/main/<area>/<history_site_code>')
class DetailLocationView(BaseResource):
    @swag_from(AREA_GET)
    def get(self, area, historical_site_code):
        data = HistorySiteModel.objects(_id=historical_site_code).first()

        if data is None:
            abort(204)

        return self.unicode_safe_json_dumps({
            "imagePath": data.image_path,
            "location": data.location,
            "text": data.text,
            "extra": [{
                "extraName": extra.name,
                "extraImagePath": data.image_path,
                "extraLocation": data.location
            } for extra in data.extra],
            "extraText": data.extra_text,
            "explain": data.explain
        })
