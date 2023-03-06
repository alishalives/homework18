# Импорт
from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema


# Регистрация неймспейса и схем для дальнейшей сериализации
movie_ns = Namespace("movies")
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MoviesView(Resource):
    """CBV"""
    def get(self):
        """Метод получения всех фильмов"""
        if request.args.get("director_id"):
            movie = movie_service.get_by_director_id(request.args.get("director_id"))
            return movies_schema.dump(movie)
        elif request.args.get("genre_id"):
            movie = movie_service.get_by_genre_id(request.args.get("genre_id"))
            return movies_schema.dump(movie)
        elif request.args.get("year"):
            movie = movie_service.get_by_year(request.args.get("year"))
            return movies_schema.dump(movie)

        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        """Метод создания нового фильма"""
        req_json = request.json
        movie_service.create(req_json)
        return "Новый фильм добавлен в подборку", 201


@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    """CBV"""
    def get(self, mid):
        """Метод получения фильма по его mid"""
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        """Метод обновления данных о конкретном фильме"""
        req_json = request.json
        req_json["id"] = mid
        movie_service.update(req_json)

        return "", 204

    def delete(self, mid):
        """Метод удаления конкретного фильма"""
        movie_service.delete(mid)

        return "", 204

