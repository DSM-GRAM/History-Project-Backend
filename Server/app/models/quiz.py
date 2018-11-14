from mongoengine import *


class QuizModel(Document):
    question = StringField()

    answer = ListField(
        StringField()
    )

    WordList = ListField(
        StringField()
    )
