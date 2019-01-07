from mongoengine import *


class MapModel(Document):
    name = StringField()
    latitude = FloatField()
    longitude = FloatField()
