from extensions import db

class Publisher(db.Model):
    publisher_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'<Publisher {self.name}>'