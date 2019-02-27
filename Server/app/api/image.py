from flask import send_file, Blueprint
from flasgger import swag_from
from flask_restful import Api
import mongoengine
import os

from app.api import BaseResource
from app.models.main import HistorySiteModel
from app.docs.image import IMAGE_GET, VR_IMAGE_GET
from config import IMAGE_FOLDER_PATH

image_blueprint = Blueprint(__name__, __name__)
api = Api(image_blueprint)


def send_image(area, image_name, ext):
    return send_file(f'{IMAGE_FOLDER_PATH}/{area}/{image_name}.{ext}',
                     attachment_filename=f'{image_name}.{ext}')


@api.resource('/image/<area>/<image_name>')
class ImageView(BaseResource):
    @swag_from(IMAGE_GET)
    def get(self, area, image_name):
        try:
            return send_image(area, image_name, 'jpg')
        except FileNotFoundError:
            return send_image(area, image_name, 'jpeg')

#
# @api.resource('/vr/image/{history_site_code}')
# class VRImageView(BaseResource):
#     @swag_from(VR_IMAGE_GET)
#     def get(self, history_site_code):
#         try:
#             return send_image('vr', history_site_code, 'jpg')
#         except FileNotFoundError:
#             return '', 204


@api.resource('/vr/image/<site_code>')
class VRImageUrlView(BaseResource):
    def get(self, site_code):
        try:
            site = HistorySiteModel.objects(id=site_code).first()
            if site is None:
                return '', 204
            if not os.path.isfile(IMAGE_FOLDER_PATH + f'/vr/{site_code}.JPG'):
                return '', 204

        except mongoengine.errors.ValidationError:
            return '', 204

        return {
            'imagePath': f'http://52.199.207.14/image/vr/{site_code}'
        }
