from dao.model.movie import Movie


class MovieDAO:
    """ Создание слоя DAO с методами обработки данных """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_by_director_id(self, qr):
        return self.session.query(Movie).filter(Movie.director_id == qr).all()

    def get_by_genre_id(self, qr):
        return self.session.query(Movie).filter(Movie.genre_id == qr).all()

    def get_by_year(self, qr):
        return self.session.query(Movie).filter(Movie.year == qr).all()

    def create(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, movie):
        self.session.delete(movie)

