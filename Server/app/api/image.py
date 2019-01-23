from flask import send_file, Blueprint, make_response
from flasgger import swag_from
from flask_restful import Api

from app.api import BaseResource
from app.docs.image import IMAGE_GET
from config import IMAGE_FOLDER_PATH

image_blueprint = Blueprint(__name__, __name__)
api = Api(image_blueprint)


def send_image(area, image_name, ext):
    image = make_response(send_file(f'{IMAGE_FOLDER_PATH}/{area}/{image_name}.{ext}',
                                    attachment_filename=f'{image_name}.{ext}'))
    return image


@api.resource('/image/<area>/<image_name>')
class ImageView(BaseResource):
    @swag_from(IMAGE_GET)
    def get(self, area, image_name):
        try:
            return send_image(area, image_name, 'jpg')
        except FileNotFoundError:
            return send_image(area, image_name, 'jpeg')
