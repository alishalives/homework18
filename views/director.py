# Импорт
from flask_restx import Resource, Namespace

from container import director_service
from dao.model.director import DirectorSchema


# Регистрация неймспейса и схем для дальнейшей сериализации
director_ns = Namespace("directors")
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route("/")
class DirectorsView(Resource):
    """CBV"""
    def get(self):
        """Метод получения всех режиссеров"""
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors)


@director_ns.route("/<int:did>")
class DirectorView(Resource):
    """CBV"""
    def get(self, did):
        """Метод получения всех режиссера по did"""
        director = director_service.get(did)
        return director_schema.dump(director)

