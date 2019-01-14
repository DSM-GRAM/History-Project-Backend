from flask import Blueprint, abort, request
from flask_restful import Api
from flasgger import swag_from

from app.api import BaseResource
from app.models.image import ImagePathModel
from app.docs.main import MAIN_GET, AREA_GET

main_blueprint = Blueprint(__name__, __name__)
api = Api(main_blueprint)


@api.resource('/main/<area>')
class LocationView(BaseResource):
    @swag_from(MAIN_GET)
    def get(self, area):
        all_location = ImagePathModel.objects(area=area).all()

        if area != "bla" and area != "usu":
            abort(401)

        return self.unicode_safe_json_dumps([
            {
                "historicalSiteName": historic_site.historical_site_name,
                "historicalSiteLocation": historic_site.historical_site_location,
                "historicalSiteImagePath": historic_site.historical_site_image_path
            } for historic_site in all_location
        ])


@api.resource('/main/<area>/<history_site_name>')
class DetailLocationView(BaseResource):
    @swag_from(AREA_GET)
    def get(self, area, historical_site_name):
        data = ImagePathModel.objects(historical_site_name=historical_site_name).first()

        if data is None:
            abort(204)

        all_location = ImagePathModel.objects(area=area).all()

        return self.unicode_safe_json_dumps({
            "imagePath": data.historical_site_image_path,
            "location": data.historical_site_location,
            "text": data.text,
            "extra": [{
                "extraName": data.historical_site_name,
                "extraImagePath": data.historical_site_image_path,
                "extraLocation": data.historical_site_location
            } for data in all_location if not data.historical_site_name == historical_site_name],
            "extraText": data.extra_text,
            "explain": data.explain
        })
