from extensions import db
from sqlalchemy.exc import SQLAlchemyError
from models import Book, Genre, BookGenre
import random


class BookService:
    @staticmethod
    def create_book(title, publisher_id, cover_image, author_id, synopsis):
        try:
            book = Book(
                title=title,
                publisher_id=publisher_id,
                cover_image=cover_image,
                author_id=author_id,
                synopsis=synopsis
            )
            db.session.add(book)
            db.session.commit()
            return book
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error creating book: {e}")
            return None
        
    @staticmethod
    def get_books(quantity):
        try:
            total_books = Book.query.count()
            if quantity > total_books:
                quantity = total_books
            random_ids = random.sample(range(1, total_books + 1), quantity)
            books = Book.query.filter(Book.book_id.in_(random_ids)).all()
            
            return books
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error fetching books: {e}")
            return None
        except ValueError as e:
            print(f"Error in random selection: {e}")
            return None
    
    @staticmethod
    def get_books_with_author_and_genre(quantity):
        try:
            total_books = Book.query.count()
            
            if quantity > total_books:
                quantity = total_books

            books = (
                db.session.query(Book)
                .join(Book.author)
                .outerjoin(Book.genres)
                .options(db.contains_eager(Book.author), db.contains_eager(Book.genres))
                .order_by(db.func.random())  # Seleciona livros aleatórios
                .limit(quantity)
                .all()
            )
            
            return books
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error fetching books with authors and genres: {e}")
            return None
        except ValueError as e:
            print(f"Error in random selection: {e}")
            return None
        
    @staticmethod
    def get_book_by_id(book_id):
        try:
            return Book.query.get(book_id)
        except SQLAlchemyError as e:
            print(f"Error find book: {e}")
            return None
        
    # @staticmethod
    # def get_books(quantity):
    #     try:
    #         return Book.query.limit(quantity).all()
    #     except SQLAlchemyError as e:
    #         print(f"Error fetching books: {e}")
    #         return None

    @staticmethod
    def update_book(book_id, **kwargs):
        try:
            book = Book.query.get(book_id)
            if not book:
                print("Book not found")
                return None
            for key, value in kwargs.items():
                if hasattr(book, key):
                    setattr(book, key, value)
            db.session.commit()
            return book
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error updating book: {e}")
            return None

    @staticmethod
    def delete_book(book_id):
        try:
            book = Book.query.get(book_id)
            if not book:
                print("Book not found")
                return None
            db.session.delete(book)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error deleting book: {e}")
            return None

    @staticmethod
    def add_genre_to_book( book_id, genre_id):
        try:
            book = Book.query.get(book_id)
            genre = Genre.query.get(genre_id)
            if book and genre:
                book_genre = BookGenre(book_id=book_id, genre_id=genre_id)
                db.session.add(book_genre)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            raise e