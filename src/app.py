from flask import Flask
from extensions import db
from config.config import Config
from controllers import UserController, AuthorController, PublisherController, BookController, GenreController, UserBookController
from services.user_service import UserService

user = UserService()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    UserController(app)
    BookController(app)
    PublisherController(app)
    AuthorController(app)
    GenreController(app)
    UserBookController(app)
    with app.app_context():
        db.create_all()
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8000)
