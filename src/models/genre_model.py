from extensions import db

class Genre(db.Model):
    genre_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    books = db.relationship('Book', secondary='book_genre', backref='genres', lazy=True)

    def __repr__(self):
        return f'<Genre {self.name}>'
