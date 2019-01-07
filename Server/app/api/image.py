from flask import send_file, Blueprint, make_response, abort
from flasgger import swag_from
from flask_restful import Api

from app.api import BaseResource
from app.docs.image import IMAGE_GET
from config import IMAGE_FOLDER_PATH

image_blueprint = Blueprint(__name__, __name__)
api = Api(image_blueprint)


@api.resource('/image/<image_name>')
class ImageView(BaseResource):
    @swag_from(IMAGE_GET)
    def get(self, image_name):
        try:
            image = make_response(send_file(f'{IMAGE_FOLDER_PATH}\\{image_name}.jpg',
                                            attachment_filename=f'{image_name}.jpg'))
            return image
        except FileNotFoundError:
            abort(404)

