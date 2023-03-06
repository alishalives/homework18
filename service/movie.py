from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_by_director_id(self, qr):
        return self.dao.get_by_director_id(qr)

    def get_by_genre_id(self, qr):
        return self.dao.get_by_genre_id(qr)

    def get_by_year(self, qr):
        return self.dao.get_by_year(qr)

    def create(self, data):
        self.dao.create(data)

    def update(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.dao.update(movie)

    def delete(self, mid):
        movie = self.get_one(mid)
        self.dao.delete(movie)
