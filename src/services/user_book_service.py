from extensions import db
from sqlalchemy.exc import SQLAlchemyError
from models import UserBook


class UserBookService:
    @staticmethod
    def add_user_book(user_id, book_id, progress=0.0, rating=None, notes=None):
        try:
            user_book = UserBook(
                user_id=user_id,
                book_id=book_id,
                progress=progress,
                rating=rating,
                notes=notes
            )
            db.session.add(user_book)
            db.session.commit()
            return user_book
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error adding user book: {e}")
            return None

    @staticmethod
    def get_user_book(user_book_id):
        try:
            return UserBook.query.get(user_book_id)
        except SQLAlchemyError as e:
            print(f"Error finding user book: {e}")
            return None

    @staticmethod
    def update_user_book(user_book_id, **kwargs):
        try:
            user_book = UserBook.query.get(user_book_id)
            if not user_book:
                print("UserBook not found")
                return None
            for key, value in kwargs.items():
                if hasattr(user_book, key):
                    setattr(user_book, key, value)
            db.session.commit()
            return user_book
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error updating user book: {e}")
            return None

    @staticmethod
    def delete_user_book(user_book_id):
        try:
            user_book = UserBook.query.get(user_book_id)
            if not user_book:
                print("UserBook not found")
                return None
            db.session.delete(user_book)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error deleting user book: {e}")
            return None

    @staticmethod
    def get_all_user_books_by_user(user_id):
        try:
            return UserBook.query.filter_by(user_id=user_id).all()
        except SQLAlchemyError as e:
            print(f"Error retrieving user books: {e}")
            return None
