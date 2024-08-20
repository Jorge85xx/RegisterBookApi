from extensions import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    phone_number = db.Column(db.String(15))
    profile_picture = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)  # adicionar algum tipo de criptografia ou hash
    quote = db.Column(db.Text)

    # Relationships
    user_books = db.relationship('UserBook', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'