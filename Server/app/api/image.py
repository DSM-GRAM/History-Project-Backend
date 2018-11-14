from flask import send_file, Blueprint, make_response, abort
from flask_restful import Api

from app.api import BaseResource
from config import IMAGE_FOLDER_PATH

image_blueprint = Blueprint(__name__, __name__)
api = Api(image_blueprint)


@api.resource('/image/<image_name>')
class ImageView(BaseResource):
    def get(self, image_name):
        try:
            image = make_response(send_file(f'{IMAGE_FOLDER_PATH}\{image_name}.jpg',
                                            attachment_filename=f'{image_name}.jpg'))
            return image

        except FileNotFoundError:
            return f'{image_name}.jpg is not found', 401




