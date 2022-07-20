from project.dao.base import BaseDAO

from project.tools.security import compose_passwords
from project.config import BaseConfig


from flask_restx import abort

import calendar
import datetime
import jwt

#  Сервис аутонтификации, принимает общюю ДАО: BaseDAO  #
#  До вьюх  !!  #
#    #
#    #

SEC = BaseConfig.SECRET_KEY
ALG = BaseConfig.ALGORITM

class AuthService:
    def __init__(self, dao: BaseDAO) -> None:
        """Сохраняет дао как класс BASEDAO"""
        self.dao = dao


    def generate_tokens(self, email, password, is_refresh=False):
        user = self.dao.get_user_by_email(email)
        
        if not user:
            abort(401, "Нет такого  пользователя")

        if not is_refresh:
            if not compose_passwords(user.password, password):
                abort(401, "Нет такого пароля")


        data = {
            "email": user.email,
            "id": user.id
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SEC, algorithm=ALG)


        days_130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days_130.timetuple())
        refresh_token = jwt.encode(data, SEC, algorithm=ALG)


        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }


    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=SEC, algorithms=ALG)
        email = data["email"]

        user = self.dao.get_user_by_email(email)

        if not user:
            abort(401, "Нет такого пользователя")
        return self.generate_tokens(user.email, user.password, is_refresh=True)









