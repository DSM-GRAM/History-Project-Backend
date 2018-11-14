from mongoengine import *


class ImagePathModel(Document):
    area = StringField()
    historicalsitename = StringField()
    historicalsitelocation = StringField()
    historicalsiteimagepath = StringField()
    text = StringField()
    extratext = StringField()
    explain = StringField()

