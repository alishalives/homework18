# Импорт
from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.director import director_ns
from views.genres import genre_ns
from views.movie import movie_ns


def create_app(config: Config = Config()):
    """ Функция создания основного объекта app """
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    register_extensions(application)
    return application


def register_extensions(application):
    """ Функция подключения расширений """
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    create_data(application, db)


def create_data(app, db):
    """ Функция добавления данных в бд """
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run()
