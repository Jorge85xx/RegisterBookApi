from extensions import db


class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Author {self.first_name} {self.last_name}>'
