from extensions import db


class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.publisher_id'), nullable=False)
    cover_image = db.Column(db.String(255))
    author_id = db.Column(db.Integer, db.ForeignKey('author.author_id'), nullable=False)
    synopsis = db.Column(db.Text)

    # Relationships
    publisher = db.relationship('Publisher', backref=db.backref('books', lazy=True))
    author = db.relationship('Author', backref=db.backref('books', lazy=True))
    user_books = db.relationship('UserBook', backref='book', lazy=True)

    def __repr__(self):
        return f'<Book {self.title}>'