from flask import Blueprint, request
from services.book_service import BookService
from utils.response import response  


class BookController:
    def __init__(self, app=None):
        self.book_bp = Blueprint('books', __name__, url_prefix='/books')
        self.book_service = BookService()

        # routes
        self.book_bp.add_url_rule('/', 'create_book', self.create_book, methods=['POST'])
        self.book_bp.add_url_rule('/<int:book_id>', 'get_book', self.get_book, methods=['GET'])
        self.book_bp.add_url_rule('/<int:book_id>', 'update_book', self.update_book, methods=['PUT'])
        self.book_bp.add_url_rule('/<int:book_id>', 'delete_book', self.delete_book, methods=['DELETE'])

        if app:
            self.init_app(app)

    def init_app(self, app):
        app.register_blueprint(self.book_bp)

    def create_book(self):
        data = request.get_json()
        try:

            book = self.book_service.create_book(
                title=data.get('title'),
                publisher_id=data.get('publisher_id'),
                cover_image=data.get('cover_image'),
                author_id=data.get('author_id'),
                synopsis=data.get('synopsis')
            )
            genre_id = data.get('genre_id')
            if genre_id:
                self.book_service.add_genre_to_book(book.book_id, genre_id)
            
            if book:
                return response(
                    status=201,
                    name_of_content='book',
                    content={
                        'book_id': book.book_id,
                        'title': book.title,
                        'publisher_id': book.publisher_id,
                        'cover_image': book.cover_image,
                        'author_id': book.author_id,
                        'synopsis': book.synopsis
                    }
                )
            else:
                return response(
                    status=400,
                    name_of_content='error',
                    content={},
                    message='Failed to create book'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )

    def get_book(self, book_id):
        book = self.book_service.get_book_by_id(book_id)
        if book:
            return response(
                status=200,
                name_of_content='book',
                content={
                    'book_id': book.book_id,
                    'title': book.title,
                    'publisher_id': book.publisher_id,
                    'cover_image': book.cover_image,
                    'author_id': book.author_id,
                    'synopsis': book.synopsis
                }
            )
        else:
            return response(
                status=404,
                name_of_content='error',
                content={},
                message='Book not found'
            )

    def update_book(self, book_id):
        data = request.get_json()
        try:
            book = self.book_service.update_book(book_id, **data)
            if book:
                return response(
                    status=200,
                    name_of_content='book',
                    content={
                        'book_id': book.book_id,
                        'title': book.title,
                        'publisher_id': book.publisher_id,
                        'cover_image': book.cover_image,
                        'author_id': book.author_id,
                        'synopsis': book.synopsis
                    }
                )
            else:
                return response(
                    status=404,
                    name_of_content='error',
                    content={},
                    message='Book not found'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )

    def delete_book(self, book_id):
        try:
            success = self.book_service.delete_book(book_id)
            if success:
                return response(
                    status=204,
                    name_of_content='message',
                    content={},
                    message='Book deleted successfully'
                )
            else:
                return response(
                    status=404,
                    name_of_content='error',
                    content={},
                    message='Book not found'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )
