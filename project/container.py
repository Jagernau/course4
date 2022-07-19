from project.dao import GenresDAO, DirectorsDAO, UsersDAO, MoviesDAO, AuthDAO

from project.services import GenresService, DirectorsService, UsersService, MoviesService, AuthService 

from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
user_dao = UsersDAO(db.session)
movie_dao = MoviesDAO(db.session)
auth_dao = AuthDAO(db.session)


# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
user_service = UsersService(dao=user_dao)
movie_service = MoviesService(dao=movie_dao)
auth_service = AuthService(dao=auth_dao)
