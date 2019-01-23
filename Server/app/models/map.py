from mongoengine import *


class MapModel(Document):
    meta = {
        'collection': 'map'
    }

    name = StringField()
    address = StringField()
