from flask import Flask
from extensions import db
from config.config import Config
from models import Author, BookGenre, Book, Genre, Publisher, ReadingHistory, UserBook, User, UserPreferences


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)

    with app.app_context():
        db.create_all()  

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
