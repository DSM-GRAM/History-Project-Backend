import os

IMAGE_FOLDER_PATH = '../static/images'


class Config:
    SERVICE_NAME = "History-Project"

    HOST = '0.0.0.0'
    PORT = 80
    DEBUG = False

    RUN_SETTINGS = {
        'host': HOST,
        'port': PORT,
        'debug': DEBUG
    }

    MONGODB_SETTINGS = {
        'db': SERVICE_NAME,
        'host': None,
        'port': None,
        'username': os.getenv('MONGO_ID', None),
        'password': os.getenv('MONGO_PW', None)
    }

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': os.getenv('SWAGGER_URI', '/docs'),
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': ''
        },
        'basePath': '/',
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ]
    }

