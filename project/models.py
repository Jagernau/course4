from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


#  Это модели бд  #



class Genre(models.Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    def __repr__(self):
        return f"<Genre '{self.name.title()}'>"


class Director(models.Base):
    __tablename__ = 'directors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    def __repr__(self):
        return f"<Director '{self.name.title()}'>"


class Movie(models.Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    trailer = Column(String(255))
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey("directors.id"))
    director = relationship("Director")
    def __repr__(self):
        return f"<Movie '{self.title.title()}'>"


class User(models.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(200))
    name = Column(String(200))
    surname = Column(String(200))
    favorite_genre = Column(String(200), ForeignKey("genres.id"))
    genre = relationship("Genre")
    def __repr__(self):
        return f"<User '{self.email}'>"


