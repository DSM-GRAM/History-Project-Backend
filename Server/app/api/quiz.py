from random import randint

from flask import Blueprint, request
from flask_restful import Api

from app.api import BaseResource
from app.models.quiz import QuizModel

quiz_blueprint = Blueprint(__name__, __name__)
api = Api(quiz_blueprint)


@api.resource('/quiz')
class QuizView(BaseResource):
    def get(self):
        quiz_list = QuizModel.objects().all()
        quiz = quiz_list[randint(0, len(quiz_list) - 1)]

        if "O" in quiz.answer or "X" in quiz.answer:
            answer = quiz.answer[0]

            return self.unicode_safe_json_dumps({
                "question": quiz.question,
                "OXanswer": answer,
                "WordList": quiz.WordList
            }, 200)

        else:
            return self.unicode_safe_json_dumps({
                "question": quiz.question,
                "answer_word": quiz.answer,
                "NumberOfAnswer": len(quiz.answer),
                "WordList": quiz.WordList
            }, 200)

    # Test

    # def post(self):
    #     QuizModel(
    #         question=request.json['question'],
    #         answer=request.json['answer'],
    #          WordList=request.json['WordList']
    #     ).save()
    #
    #     return '', 201
