from flask_restx import Namespace, Resource
from flask import request

from project.container import user_service
from project.setup.api.models import user

from project.tools.security import auth_required, decode_token


api = Namespace('user')



@api.route('/')
class UserView(Resource):

    @auth_required
    @api.marshal_with(user, code=200, description='OK')
    def get(self):
        """
        Get user by id.
        """
        token = request.headers["Authorization"].split("Bearer ")[-1]
        uid = decode_token(token)["id"]
        return user_service.get_by_id(uid), 200


    @auth_required
    def patch(self):
        """
        Изменить информацию пользователя
        """
        token = request.headers["Authorization"].split("Bearer ")[-1]
        uid = decode_token(token)["id"]
        data = request.get_json()
        user_service.update_part(data, uid)
        return "", 204




@api.route("/password/")
class UserChangePassword(Resource):

    @auth_required
    def put(self):
        token = request.headers["Authorization"].split("Bearer ")[-1]
        uid = decode_token(token)["id"]
        req_json = request.json
        user_service.update(req_json, uid)
        return "", 204

