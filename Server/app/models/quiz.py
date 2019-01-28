from mongoengine import *


class QuizModel(Document):
    ox_question = ListField(
        StringField(),
        null=True
    )

    multiple_question = ListField(
        StringField(),
        null=True
    )

    ox_answer = ListField(
        StringField(1),
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
