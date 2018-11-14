from functools import wraps
import json

from flask import Response, abort, g, request
from flask_restful import Resource


def json_required(required_keys: dict):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not request.is_json:
                abort(406)

            for key, typ in required_keys.items():
                if key not in request.json:
                    return Response('{} key is required.'.format("'" + key + "'"), 400)

                if isinstance(typ, type):
                    if not isinstance(request.json[key], typ):
                        return Response('{} key only accepts {} values.'
                                        .format("'" + str(key) + "'", str(typ)[8:-2]), 406)
                else:
                    abort(400)

            return func(*args, **kwargs)
        return wrapper
    return decorator


class BaseResource(Resource):
    @classmethod
    def unicode_safe_json_dumps(cls, data, status_code=200):
        return Response(
            json.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8'
        )

    @classmethod
    def check_is_exist(cls, *args):
        for data in args:
            if data == 0:
                continue
            if not data:
                abort(406)


def router(app):
    from app.api import image
    app.register_blueprint(image.api.blueprint)
    from app.api import quiz
    app.register_blueprint(quiz.api.blueprint)
    from app.api import main
    app.register_blueprint(main.api.blueprint)
