import os
import socket

IMAGE_FOLDER_PATH = '../static/images'


class Config:
    SERVICE_NAME = "History-Project"

    HOST = socket.gethostbyname(socket.gethostname())
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
