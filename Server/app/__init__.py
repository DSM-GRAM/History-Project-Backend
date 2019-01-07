from flask import Flask
from flasgger import Swagger
import mongoengine

from app.api import router
from config import IMAGE_FOLDER_PATH


def create_app(*config_obj):
    app_ = Flask(
        __name__,
        static_folder=IMAGE_FOLDER_PATH,
    )

    for obj in config_obj:
        app_.config.from_object(obj)

    router(app_)

    mongoengine.connect(**app_.config["MONGODB_SETTINGS"])
    Swagger(template=app_.config['SWAGGER_TEMPLATE']).init_app(app_)

    return app_
