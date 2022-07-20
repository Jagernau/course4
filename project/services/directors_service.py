from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Director


#  Сервис режиссёров, принимает общюю ДАО: BaseDAO  #
#  До вьюх  !!  #
#  get ?page  #
#  get/did  #



class DirectorsService:
    def __init__(self, dao: BaseDAO) -> None:
        """Сохраняет дао как класс BASEDAO"""
        self.dao = dao

    def get_by_id(self, did: int) -> Director:
        """Отдаёт одного режиссёра, принимая id(его did )"""
        if director:= self.dao.get_by_id(did):
            return director
        else:
            raise ItemNotFound(f'Director with did={did} not exists.')


    def get_all(self, **kwargs) -> list[Director]:
        """Отдаёт всех режжисёров с пагинацией, принимает номер страницы"""
        return self.dao.get_all(page=kwargs["page"])

