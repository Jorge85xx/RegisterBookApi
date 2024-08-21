from flask import Blueprint, request
from services.user_book_service import UserBookService
from utils.response import response


class UserBookController:
    def __init__(self, app=None):
        self.user_book_bp = Blueprint('user_books', __name__, url_prefix='/user_books')
        self.user_book_service = UserBookService()

        # Register routes
        self.user_book_bp.add_url_rule('/', 'add_user_book', self.add_user_book, methods=['POST'])
        self.user_book_bp.add_url_rule('/<int:user_book_id>', 'get_user_book', self.get_user_book, methods=['GET'])
        self.user_book_bp.add_url_rule('/<int:user_book_id>', 'update_user_book', self.update_user_book, methods=['PUT'])
        self.user_book_bp.add_url_rule('/<int:user_book_id>', 'delete_user_book', self.delete_user_book, methods=['DELETE'])
        self.user_book_bp.add_url_rule('/user/<int:user_id>', 'get_all_user_books_by_user', self.get_all_user_books_by_user, methods=['GET'])

        if app:
            self.init_app(app)

    def init_app(self, app):
        app.register_blueprint(self.user_book_bp)

    def add_user_book(self):
        data = request.get_json()
        try:
            user_book = self.user_book_service.add_user_book(
                user_id=data.get('user_id'),
                book_id=data.get('book_id'),
                progress=data.get('progress', 0.0),
                rating=data.get('rating'),
                notes=data.get('notes')
            )
            if user_book:
                return response(
                    status=201,
                    name_of_content='user_book',
                    content={
                        'user_book_id': user_book.user_book_id,
                        'user_id': user_book.user_id,
                        'book_id': user_book.book_id,
                        'progress': user_book.progress,
                        'rating': user_book.rating,
                        'notes': user_book.notes
                    }
                )
            else:
                return response(
                    status=400,
                    name_of_content='error',
                    content={},
                    message='Failed to add user book'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )

    def get_user_book(self, user_book_id):
        user_book = self.user_book_service.get_user_book(user_book_id)
        if user_book:
            return response(
                status=200,
                name_of_content='user_book',
                content={
                    'user_book_id': user_book.user_book_id,
                    'user_id': user_book.user_id,
                    'book_id': user_book.book_id,
                    'progress': user_book.progress,
                    'rating': user_book.rating,
                    'notes': user_book.notes
                }
            )
        else:
            return response(
                status=404,
                name_of_content='error',
                content={},
                message='UserBook not found'
            )

    def update_user_book(self, user_book_id):
        data = request.get_json()
        try:
            user_book = self.user_book_service.update_user_book(user_book_id, **data)
            if user_book:
                return response(
                    status=200,
                    name_of_content='user_book',
                    content={
                        'user_book_id': user_book.user_book_id,
                        'user_id': user_book.user_id,
                        'book_id': user_book.book_id,
                        'progress': user_book.progress,
                        'rating': user_book.rating,
                        'notes': user_book.notes
                    }
                )
            else:
                return response(
                    status=404,
                    name_of_content='error',
                    content={},
                    message='UserBook not found'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )

    def delete_user_book(self, user_book_id):
        try:
            success = self.user_book_service.delete_user_book(user_book_id)
            if success:
                return response(
                    status=204,
                    name_of_content='message',
                    content={},
                    message='UserBook deleted successfully'
                )
            else:
                return response(
                    status=404,
                    name_of_content='error',
                    content={},
                    message='UserBook not found'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )

    def get_all_user_books_by_user(self, user_id):
        user_books = self.user_book_service.get_all_user_books_by_user(user_id)
        if user_books:
            return response(
                status=200,
                name_of_content='user_books',
                content=[
                    {
                        'user_book_id': ub.user_book_id,
                        'user_id': ub.user_id,
                        'book_id': ub.book_id,
                        'progress': ub.progress,
                        'rating': ub.rating,
                        'notes': ub.notes
                    } for ub in user_books
                ]
            )
        else:
            return response(
                status=404,
                name_of_content='error',
                content={},
                message='No user books found for this user'
            )
