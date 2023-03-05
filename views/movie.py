from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import Movie, MovieSchema
from setup_db import db


movie_ns = Namespace("movies")
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):
        all_movies = db.session.query(Movie).get_all()
        return movies_schema.dump(all_movies)

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        db.session.add(new_movie)
        db.session.commit()
        return "Новый фильм добавлен в подборку", 200


@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid):
        movie = db.session.query(Movie).get(mid)
        return movie_schema.dump(movie)

    def put(self, mid):
        req_json = request.json
        movie = self.get(mid)

        movie.title = req_json.get("title")
        movie.description = req_json.get("description")
        movie.trailer = req_json.get("trailer")
        movie.year = req_json.get("year")
        movie.rating = req_json.get("rating")
        movie.genre_id = req_json.get("genre.id")
        movie.director_id = req_json.get("director_id")

        db.session.add(movie)
        db.session.commit()

        return "Данные о фильме обновлены", 200

    def delete(self, mid):
        movie = self.get(mid)

        db.session.delete(movie)
        db.session.commit()

        return "Данные о фильме удалены", 200

