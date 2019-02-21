from flask import send_file, Blueprint
from flasgger import swag_from
from flask_restful import Api

from app.api import BaseResource
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


@api.resource('/image/vr/{history_site_code}')
class VRImageView(BaseResource):
    @swag_from(VR_IMAGE_GET)
    def get(self, history_site_code):
        try:
            return send_image('vr', history_site_code, 'jpg')
        except FileNotFoundError:
            return '', 204
