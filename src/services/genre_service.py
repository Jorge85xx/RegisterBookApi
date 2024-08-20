from extensions import db
from models import Genre


class GenreService:

    def get_genre_by_id(self, genre_id):
        return Genre.query.get(genre_id)

    def create_genre(self, name):
        try:
            genre = Genre(name=name)
            db.session.add(genre)
            db.session.commit()
            return genre
        except Exception as e:
            db.session.rollback()
            raise e

    def get_all_genres(self):
        return Genre.query.all()

    def update_genre(self, genre_id, name):
        genre = Genre.query.get(genre_id)
        if genre:
            genre.name = name
            db.session.commit()
            return genre
        return None

    def delete_genre(self, genre_id):
        genre = Genre.query.get(genre_id)
        if genre:
            db.session.delete(genre)
            db.session.commit()
            return True
        return False
