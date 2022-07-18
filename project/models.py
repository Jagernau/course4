from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


#  Это модели бд  #



class Genre(models.Base):
    __tablename__ = 'genres'
    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))


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


class User(models.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(200))
    name = Column(String(200))


