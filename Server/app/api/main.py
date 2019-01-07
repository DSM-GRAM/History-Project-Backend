from flask import Blueprint, abort, request
from flask_restful import Api

from app.api import BaseResource
from app.models.image import ImagePathModel

main_blueprint = Blueprint(__name__, __name__)
api = Api(main_blueprint)


@api.resource('/main')
class LocationView(BaseResource):
    def post(self):
        area = request.json['area']
        all_location = ImagePathModel.objects(area=area).all()

        if area == "bla" or area == "usu":
            return self.unicode_safe_json_dumps([
                {
                    "historicalSiteName": historic_site.historical_site_name,
                    "historicalSiteLocation": historic_site.historical_site_location,
                    "historicalSiteImagePath": historic_site.historical_site_image_path
                } for historic_site in all_location
            ], 200)
        else:
            abort(401)


@api.resource('/main/<area>')
class DetailLocationView(BaseResource):
    def post(self, area):
        historical_site_name = request.json['historicalSiteName']
        data = ImagePathModel.objects(historical_site_name=historical_site_name).first()
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
