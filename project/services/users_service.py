from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import User
from project.tools.security import generate_password_hash

#  Сервис юзера, принимает общюю ДАО: BaseDAO  #
#  До вьюх  !!  #
#  get/uid  #
#  path/uid/json  #
#  put/uid/json:password  #





class UsersService:
    def __init__(self, dao: BaseDAO):
        self.dao = dao


    def get_by_id(self, uid: int) -> User:
        """Отдаёт одного юзера, принимая id(его uid )"""
        if user:= self.dao.get_by_id(uid):
            return user
        raise ItemNotFound(f'Director with uid={uid} not exists.')


    def update_part(self, data, uid) -> None:
        """Изменить информацию пользователя:  """
        if user:= self.dao.get_by_id(uid):
            if 'name' in data:
                user.name = data['name']
            if 'surname' in data:
                user.surname = data['surname']
            if 'favorite_genre' in data:
                user.favorite_genre = data['favorite_genre']
            pass


    def create(self, data):
        data["password"] = generate_password_hash(data["password"])
        self.dao.create(data)

