from setup_db import db
from marshmallow import Schema, fields


class Director(db.Model):
    """ Создание модели таблицы director """
    __tablename__ = "director"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class DirectorSchema(Schema):
    """ Создание схемы таблицы director для дальнейшей сериализации """
    id = fields.Int()
    name = fields.Str()
