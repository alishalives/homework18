from setup_db import db
from marshmallow import Schema, fields


class Genre(db.Model):
    """ Создание модели таблицы genre """
    __tablename__ = "genre"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class GenreSchema(Schema):
    """ Создание схемы таблицы genre для дальнейшей сериализации """
    id = fields.Int()
    name = fields.Str()
