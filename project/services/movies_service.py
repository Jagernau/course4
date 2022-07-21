
from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Movie


#  Сервис фильмов, принимает общее ДАО :BaseDAO  #
#  До вьюх  !!  #
#  get ?page, ?status  #
#  get/id  #



class MoviesService:
    def __init__(self, dao: BaseDAO) -> None:
        """Сохраняет дао как класс BASEDAO"""
        self.dao = dao


    def get_by_id(self, mid: int) -> Movie:
        """Отдаёт информацию по фильму, принимает pk (или id по другому)"""
        if movie := self.dao.get_by_id(mid):
            return movie
        else:
            raise ItemNotFound(f'Movie with mid={mid} not exists.')


    def get_all(self, **kwargs) -> list[Movie]:
        """Отдаёт все при все фильмы, для пагинации принимает номер страницы и статус для сортировки"""
        return self.dao.get_all(**kwargs)
