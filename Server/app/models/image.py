from mongoengine import *


class ImagePathModel(Document):
    meta = {
        'collection': 'image'
    }

    area = StringField(primary_key=True)
    historical_site_name = StringField()
    historical_site_location = StringField()
    historical_site_image_path = StringField()
    text = StringField()
    extra_text = StringField()
    explain = StringField()

