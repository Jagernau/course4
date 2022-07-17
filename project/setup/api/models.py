from flask_restx import fields, Model

from project.setup.api import api


# Здесь похоже сериализация типа Marshmellow

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})


movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=255, example='Чикаго'),
    'description': fields.String(required=True, max_length=255, example='Рассказ о начале творческого пути Виктора Цоя и группы «Кино», о его взаимоотношениях с Майком Науменко, его женой Натальей и многими, ктiо был в авангарде рок-движения Ленинграда 1981 года.'),
    'trailer': fields.String(required=True, max_lenght=255, example='https://www.youtube.com/watch?v=NMSUEhDWXH0'),
    'year': fields.Integer(required=True, example=1988),
    'rating': fields.Float(required=True, example=8.4),
    'genre_id': fields.Integer(required=True, example=1),
    'director_id': fields.Integer(required=True, example=1)
})


director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, example='Квентин Тарантино')
})
