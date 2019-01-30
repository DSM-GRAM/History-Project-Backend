from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.api import BaseResource
from app.models.quiz import QuizModel
from app.docs.quiz import QUIZ_GET

quiz_blueprint = Blueprint(__name__, __name__)
api = Api(quiz_blueprint)


@api.resource('/quiz/<history_site_code>')
class OXQuizView(BaseResource):
    @swag_from(QUIZ_GET)
    def get(self, history_site_code):
        quiz = QuizModel.objects(id=history_site_code).first()

        return self.unicode_safe_json_dumps({
            'oxQuestion': quiz.ox_question,
            'multipleQuestion': quiz.multiple_question,
            'oxAnswer': quiz.ox_answer,
            'multipleAnswer': quiz.multiple_answer,
            'wordList': quiz.word_list
        })
