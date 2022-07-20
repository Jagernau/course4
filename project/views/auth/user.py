from flask_restx import Namespace, Resource
from flask import request

from project.container import user_service
from project.setup.api.models import user

api = Namespace('user')



@api.route('/<int:uid>/')
class UserView(Resource):


    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def get(self, uid: int):
        """
        Get user by id.
        """
        return user_service.get_by_id(uid)


    @api.response(404, 'Not Found')
    def patch(self, uid: int):
        """
        Изменить информацию пользователя
        """
        data = request.get_json()
        user_service.update_part(data, uid)
        return "", 204








