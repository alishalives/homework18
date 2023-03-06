from setup_db import db
from marshmallow import Schema, fields
from dao.model.director import Director
from dao.model.genre import Genre


class Movie(db.Model):
    """ Создание модели таблицы movie """
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(50))
    trailer = db.Column(db.String(50))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))


class MovieSchema(Schema):
    """ Создание схемы таблицы movie для дальнейшей сериализации """
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
