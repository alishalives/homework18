from dao.genre import GenreDAO
from service.genre import GenreService

from dao.director import DirectorDAO
from service.director import DirectorService

from setup_db import db


genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
