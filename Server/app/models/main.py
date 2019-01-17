from mongoengine import *


class ExtraHistoryModel(EmbeddedDocument):
    name = StringField(primary_key=True)
    image_path = StringField()
    location = StringField()


class HistorySiteModel(Document):
    meta = {
        'collection': 'main'
    }

    area = StringField()
    name = StringField(primary_key=True)

    image_path = StringField()
    location = StringField()
    text = StringField()

    extra = EmbeddedDocumentListField(ExtraHistoryModel)

    extra_text = StringField()
    explain = StringField()
