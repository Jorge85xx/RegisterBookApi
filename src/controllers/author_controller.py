from flask import Blueprint, request
from services.author_service import AuthorService
from utils.response import response


class AuthorController:
    def __init__(self, app=None):
        self.author_bp = Blueprint('authors', __name__, url_prefix='/authors')
        self.author_service = AuthorService()

        #routes
        self.author_bp.add_url_rule('/', 'create_author', self.create_author, methods=['POST'])
        self.author_bp.add_url_rule('/<int:author_id>', 'get_author', self.get_author, methods=['GET'])
        self.author_bp.add_url_rule('/<int:author_id>', 'update_author', self.update_author, methods=['PUT'])
        self.author_bp.add_url_rule('/<int:author_id>', 'delete_author', self.delete_author, methods=['DELETE'])

        if app:
            self.init_app(app)

    def init_app(self, app):
        app.register_blueprint(self.author_bp)

    def create_author(self):
        data = request.get_json()
        try:
            author = self.author_service.create_author(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                bio=data.get('bio')
            )
            if author:
                return response(
                    status=201,
                    name_of_content='author',
                    content={
                        'author_id': author.author_id,
                        'first_name': author.first_name,
                        'last_name': author.last_name,
                        'bio': author.bio
                    }
                )
            else:
                return response(
                    status=400,
                    name_of_content='error',
                    content={},
                    message='Failed to create author'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )

    def get_author(self, author_id):
        author = self.author_service.get_author_by_id(author_id)
        if author:
            return response(
                status=200,
                name_of_content='author',
                content={
                    'author_id': author.author_id,
                    'first_name': author.first_name,
                    'last_name': author.last_name,
                    'bio': author.bio
                }
            )
        else:
            return response(
                status=404,
                name_of_content='error',
                content={},
                message='Author not found'
            )

    def update_author(self, author_id):
        data = request.get_json()
        try:
            author = self.author_service.update_author(author_id, **data)
            if author:
                return response(
                    status=200,
                    name_of_content='author',
                    content={
                        'author_id': author.author_id,
                        'first_name': author.first_name,
                        'last_name': author.last_name,
                        'bio': author.bio
                    }
                )
            else:
                return response(
                    status=404,
                    name_of_content='error',
                    content={},
                    message='Author not found'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )

    def delete_author(self, author_id):
        try:
            success = self.author_service.delete_author(author_id)
            if success:
                return response(
                    status=204,
                    name_of_content='message',
                    content={},
                    message='Author deleted successfully'
                )
            else:
                return response(
                    status=404,
                    name_of_content='error',
                    content={},
                    message='Author not found'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )
