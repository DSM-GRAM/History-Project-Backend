from mongoengine import *


class OXQuizModel(Document):
    meta = {
        'collection': 'ox_quiz'
    }
    area = StringField()
    question = StringField()
    answer = StringField(max_length=1)


class MultipleQuizModel(Document):
    meta = {
        'collection': 'multiple_quiz'
    }
    area = StringField()
    question = StringField()

    answer = ListField(
        StringField()
    )

    WordList = ListField(
        StringField()
    )
