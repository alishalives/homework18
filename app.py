from flask import Flask
from flask_restx import Api

from config import Config
from dao.model.movie import Movie
from setup_db import db
from views.director import director_ns
from views.genres import genre_ns
from views.movie import movie_ns


# функция создания основного объекта app
def create_app(config: Config):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    register_extensions(application)
    return application


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    create_data(application, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run()
