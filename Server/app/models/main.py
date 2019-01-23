from mongoengine import *


class ExtraHistoryModel(EmbeddedDocument):
    extra_name = StringField(primary_key=True)
    extra_image_path = StringField()
    extra_location = StringField()


class HistorySiteModel(Document):
    meta = {
        'collection': 'main'
    }

    area = StringField()
    name = StringField()

    image_path = StringField()
    location = StringField()
    text = StringField()

    extra = EmbeddedDocumentListField(ExtraHistoryModel)

    extra_text = StringField()
    explain = StringField()
