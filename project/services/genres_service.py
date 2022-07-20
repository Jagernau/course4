from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Genre


#  Сервис жанров, принимает общее ДАО :BaseDAO  #
#  До вьюх  !!  #
#  get ?page #
#  get/id  #



class GenresService:
    def __init__(self, dao: BaseDAO) -> None:
        """Сохраняет дао как класс BASEDAO"""
        self.dao = dao


    def get_by_id(self, pk: int) -> Genre:
        """Отдаёт жанр текстом, принимает pk (или id по другому)"""
        if genre := self.dao.get_by_id(pk):
            return genre
        else:
            raise ItemNotFound(f'Genre with pk={pk} not exists.')


    def get_all(self, **kwargs ) -> list[Genre]:
        """Отдаёт все при все жанры, для пагинации принимает номер страницы"""
        return self.dao.get_all(page=kwargs["page"])
