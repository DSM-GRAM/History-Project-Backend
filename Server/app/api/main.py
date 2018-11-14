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
                    "historicalsitename": historicsite.historicalsitename,
                    "historicalsitelocation": historicsite.historicalsitelocation,
                    "historicalsiteimagepath": historicsite.historicalsiteimagepath
                } for historicsite in all_location
            ], 200)
        else:
            abort(401)


@api.resource('/main/<area>')
class DetailLocationView(BaseResource):
    def post(self, area):
        historicalsitename = request.json['historicalsitename']
        data = ImagePathModel.objects(historicalsitename=historicalsitename).first()
        all_location = ImagePathModel.objects(area=area).all()

        return self.unicode_safe_json_dumps({
            "imagepath": data.historicalsiteimagepath,
            "location": data.historicalsitelocation,
            "text": data.text,
            "extra": [{
                "extraname": data.historicalsitename,
                "extraimagepath": data.historicalsiteimagepath,
                "extralocation": data.historicalsitelocation
            } for data in all_location if not data.historicalsitename == historicalsitename],
            "extratext": data.extratext,
            "explain": data.explain
        })


@api.resource('/test')
class TestView(BaseResource):
    def get(self):
        ImagePathModel(
            area="bla",
            historicalsitename="개척로 및 신한촌",
            historicalsitelocation="러시아, 블라디보스톡",
            historicalsiteimagepath="10.156.147.195/image/a",
            text="블라디보스토크에는 1870년대부터 한인이 점차 집중하기 시작해 1886년에 400명, 1891년에는 840여 명에 이르렀다. 한인 인구가 늘어가자, 시 당국에서는 1893년 한인들만 집단으로 거주하도록 하는 구역을 설정하였다.  ‘카레이 스카야슬라보드카(한인촌)’ 혹은 ‘개척리’라 부르던 이 지역은 블라디보스토크에서 신한촌 성립 이전 한인집단 거주지로 비교적 시내 중심지에 위치해 있었다."
        ).save()

        return '', 201