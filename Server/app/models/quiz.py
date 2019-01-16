from mongoengine import *


class OXQuizModel(Document):
    area = StringField()
    question = StringField()
    answer = StringField(max_length=1)


class MultipleQuizModel(Document):
    area = StringField()
    question = StringField()

    answer = ListField(
        StringField()
    )

    WordList = ListField(
        StringField()
    )
