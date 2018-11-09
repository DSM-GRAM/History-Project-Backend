import os

IMAGE_FOLDER_PATH = '../static/images'


class Config:
    SERVICE_NAME = "History-Project"

    HOST = '0.0.0.0'
    PORT = 80
    DEBUG = True

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



