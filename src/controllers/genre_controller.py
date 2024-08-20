from flask import Blueprint, request
from services.genre_service import GenreService
from utils.response import response


class GenreController:
    def __init__(self, app=None):
        self.genre_bp = Blueprint('genres', __name__, url_prefix='/genres')
        self.genre_service = GenreService()

        # Register routes
        self.genre_bp.add_url_rule('/', 'create_genre', self.create_genre, methods=['POST'])
        self.genre_bp.add_url_rule('/<int:genre_id>', 'get_genre', self.get_genre, methods=['GET'])
        self.genre_bp.add_url_rule('/', 'get_all_genres', self.get_all_genres, methods=['GET'])
        self.genre_bp.add_url_rule('/<int:genre_id>', 'update_genre', self.update_genre, methods=['PUT'])
        self.genre_bp.add_url_rule('/<int:genre_id>', 'delete_genre', self.delete_genre, methods=['DELETE'])

        if app:
            self.init_app(app)

    def init_app(self, app):
        app.register_blueprint(self.genre_bp)

    def create_genre(self):
        data = request.get_json()
        try:
            genre = self.genre_service.create_genre(name=data.get('name'))
            if genre:
                return response(
                    status=201,
                    name_of_content='genre',
                    content={
                        'genre_id': genre.genre_id,
                        'name': genre.name
                    }
                )
            else:
                return response(
                    status=400,
                    name_of_content='error',
                    content={},
                    message='Failed to create genre'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )

    def get_genre(self, genre_id):
        genre = self.genre_service.get_genre_by_id(genre_id)
        if genre:
            return response(
                status=200,
                name_of_content='genre',
                content={
                    'genre_id': genre.genre_id,
                    'name': genre.name
                }
            )
        else:
            return response(
                status=404,
                name_of_content='error',
                content={},
                message='Genre not found'
            )

    def get_all_genres(self):
        genres = self.genre_service.get_all_genres()
        return response(
            status=200,
            name_of_content='genres',
            content=[{
                'genre_id': genre.genre_id,
                'name': genre.name
            } for genre in genres]
        )

    def update_genre(self, genre_id):
        data = request.get_json()
        try:
            genre = self.genre_service.update_genre(genre_id, name=data.get('name'))
            if genre:
                return response(
                    status=200,
                    name_of_content='genre',
                    content={
                        'genre_id': genre.genre_id,
                        'name': genre.name
                    }
                )
            else:
                return response(
                    status=404,
                    name_of_content='error',
                    content={},
                    message='Genre not found'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )

    def delete_genre(self, genre_id):
        try:
            success = self.genre_service.delete_genre(genre_id)
            if success:
                return response(
                    status=204,
                    name_of_content='message',
                    content={},
                    message='Genre deleted successfully'
                )
            else:
                return response(
                    status=404,
                    name_of_content='error',
                    content={},
                    message='Genre not found'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )
