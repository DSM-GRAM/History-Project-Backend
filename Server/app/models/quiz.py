from app.models.main import HistorySiteModel

from mongoengine import *


class QuizModel(Document):
    site_code = StringField()

    ox_question = ListField(
        StringField(),
        null=True
    )

    multiple_question = ListField(
        StringField(),
        null=True
    )

    ox_answer = ListField(
        StringField(
            max_length=1
        ),
        null=True
    )

    multiple_answer = ListField(
        StringField(),
        null=True
    )

    word_list = ListField(
        ListField(
            StringField()
        ),
        null=True
    )
