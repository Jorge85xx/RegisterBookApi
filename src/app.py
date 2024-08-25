from flask import Flask
from flask_restx import Api
from extensions import db
from config.config import Config
# from controllers import UserController, AuthorController, PublisherController, BookController,WeekRecomendationController, GenreController, UserBookController
from controllers import author_controller, book_controller, genre_controller, publisher_controller, user_book_controller, user_controller
from services.user_service import UserService


user = UserService()



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    api = Api(
        app,
        title="RegisterBook API",
        version="1.0",
        description="A API to manage book registration",
        doc='/docs'
    )

    api.add_namespace(user_controller.api, path='/users')
    api.add_namespace(book_controller.api, path='/books')
    api.add_namespace(publisher_controller.api, path='/publishers')
    api.add_namespace(author_controller.api, path='/authors')
    api.add_namespace(genre_controller.api, path='/genres')
    api.add_namespace(user_book_controller.api, path='/userbooks')
    
    
    with app.app_context():
        db.create_all()
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8000)

