from flask import Blueprint
from flask_restful import Api
from flasgger import swag_from

from app.api import BaseResource
from app.models.quiz import OXQuizModel, MultipleQuizModel
from app.docs.quiz import MULTIPLE_QUIZ_GET, OX_QUIZ_GET

quiz_blueprint = Blueprint(__name__, __name__)
api = Api(quiz_blueprint)


@api.resource('/quiz/ox/<area>')
class OXQuizView(BaseResource):
    @swag_from(OX_QUIZ_GET)
    def get(self, area):
        quiz = OXQuizModel.objects(area=area).first()

        return self.unicode_safe_json_dumps({
            "question": quiz.question,
            "OXAnswer": quiz.answer
        }, 200)


@api.resource('/quiz/multiple/<area>')
class MultipleQuizView(BaseResource):
    @swag_from(MULTIPLE_QUIZ_GET)
    def get(self, area):
        quiz = MultipleQuizModel.objects(area=area).first()

        return self.unicode_safe_json_dumps({
            "question": quiz.question,
            "answer_word": quiz.answer,
            "NumberOfAnswer": len(quiz.answer),
            "WordList": quiz.WordList
        }, 200)
