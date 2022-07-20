from flask_restx import Namespace, Resource

from project.container import auth_service, user_service
from project.setup.api.models import user

from flask import request




api = Namespace('auth')


@api.route('/register/')
class AuthRigister(Resource):
    def post(self):
        req_json = request.json
        user_service.create(req_json)
        return "", 201


@api.route('/login/')
class AuthLogin(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get("email", None)
        password = req_json.get("password", None)
        if None in (email, password):
            return "", 400

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 201


    def put(self):
        req_json = request.json
        token = req_json.get("refresh_token")
        return auth_service.approve_refresh_token(token), 201


