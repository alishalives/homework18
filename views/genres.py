# Импорт
from flask_restx import Resource, Namespace

from container import genre_service
from dao.model.genre import GenreSchema


# Регистрация неймспейса и схем для дальнейшей сериализации
genre_ns = Namespace("genres")
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenresView(Resource):
    """CBV"""
    def get(self):
        """Метод получения всех жанров"""
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genre_ns.route("/<int:gid>")
class GenreView(Resource):
    """CBV"""
    def get(self, gid):
        """Метод получения жанра по его gid"""
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200
