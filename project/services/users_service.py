from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import User


class UsersService:
    def __init__(self, dao: BaseDAO):
        self.dao = dao

