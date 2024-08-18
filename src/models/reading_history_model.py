from extensions import db

class ReadingHistory(db.Model):
    reading_history_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), nullable=False)
    status = db.Column(db.String(50))  # Status como "Iniciado", "Concluído", "Pausado".
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relationships
    user = db.relationship('User', backref=db.backref('reading_history', lazy=True))
    book = db.relationship('Book', backref=db.backref('reading_history', lazy=True))

    def __repr__(self):
        return f'<ReadingHistory UserID={self.user_id} BookID={self.book_id}>'