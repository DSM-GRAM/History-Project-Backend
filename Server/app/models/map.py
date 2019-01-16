from mongoengine import *


class MapModel(Document):
    meta = {
        'collection': 'map'
    }

    name = StringField()
    latitude = FloatField()
    longitude = FloatField()
