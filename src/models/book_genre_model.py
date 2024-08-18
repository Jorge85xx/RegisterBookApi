from extensions import db

class BookGenre(db.Model):
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.genre_id'), primary_key=True)
