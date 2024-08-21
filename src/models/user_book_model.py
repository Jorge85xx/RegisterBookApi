from extensions import db


class UserBook(db.Model):
    user_book_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), nullable=False)
    progress = db.Column(db.Float)  # Percentual de progresso de leitura
    rating = db.Column(db.Integer)  # Nota de 1 a 10
    notes = db.Column(db.Text)  

    # Relationships
    user_relation = db.relationship('User', back_populates='user_books')
    book_relation = db.relationship('Book', back_populates='book_user_relations')

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if 1 <= value <= 10:
            self._rating = value
        else:
            raise ValueError('Rating must be between 1 and 10.')

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        if 0.0 <= value <= 100.0:
            self._progress = value
        else:
            raise ValueError('Progress must be between 0.0 and 100.0.')

    def __repr__(self):
        return f'<UserBook UserID={self.user_id} BookID={self.book_id}>'
