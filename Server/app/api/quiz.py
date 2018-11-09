from flask import Blueprint
from flask_restful import Api, Resource

quiz_blueprint = Blueprint(__name__, __name__)
api = Api(quiz_blueprint)


@api.resource('/quiz')
class QuizView(Resource):
    def post(self):
        pass
