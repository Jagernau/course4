from flask_restx import fields, Model

from project.setup.api import api


# Здесь похоже сериализация типа Marshmellow

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})


director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, example='Квентин Тарантино')
})


movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=255, example='Чикаго'),
    'description': fields.String(required=True, max_length=255, example='Рассказ о начале творческого пути Виктора Цоя и группы «Кино», о его взаимоотношениях с Майком Науменко, его женой Натальей и многими, ктiо был в авангарде рок-движения Ленинграда 1981 года.'),
    'trailer': fields.String(required=True, max_lenght=255, example='https://www.youtube.com/watch?v=NMSUEhDWXH0'),
    'year': fields.Integer(required=True, example=1988),
    'rating': fields.Float(required=True, example=8.4),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),

})


user: Model = api.model('Юзер', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=150, example="superman@mail.ru"),
    'password': fields.String(required=True, max_length=250, example="uuygTt&5)=uu7yghu8uggt4efh"),
    'name': fields.String(required=True, max_length=150, example="Максон Каркасон"),
    'surname': fields.String(required=True, max_length=200, example="Петров"),
    'favorite_genre': fields.String(required=True, max_length=150, example="Ужасы")
})
