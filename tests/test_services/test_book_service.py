import unittest
from extensions import db
from models import Book, Publisher, Author, Genre
from services.book_service import BookService
from services.author_service import AuthorService
from services.publisher_service import PublisherService
from services.genre_service import GenreService
from config.test_config import TestingConfig
from app import create_app

class BookServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def test_create_book(self):
        with self.app.app_context():
            
            publisher = PublisherService.create_publisher(name="DC Comics")
            self.assertIsNotNone(publisher)
            
            
            author = AuthorService.create_author(
                first_name="J.R.R.",
                last_name="Tolkien",
                bio="Author of The Lord of the Rings"
            )
            self.assertIsNotNone(author)

            
            genre_fantasy = GenreService.create_genre("Fantasy")
            self.assertIsNotNone(genre_fantasy)

            
            book = BookService.create_book(
                title="The Lord of the Rings",
                publisher_id=publisher.publisher_id,
                cover_image="lotr_cover.jpg",
                author_id=author.author_id,
                synopsis="An epic fantasy novel."
            )
            self.assertIsNotNone(book)
            self.assertEqual(book.title, "The Lord of the Rings")
            self.assertEqual(book.publisher_id, publisher.publisher_id)
            self.assertEqual(book.author_id, author.author_id)

           
            BookService.delete_book(book.book_id)
            PublisherService.delete_publisher(publisher.publisher_id)
            AuthorService.delete_author(author.author_id)
            GenreService.delete_genre(genre_fantasy.genre_id)

    def test_update_book(self):
        with self.app.app_context():
            
            publisher = PublisherService.create_publisher(name="DC Comics")
            self.assertIsNotNone(publisher)
            
            
            author = AuthorService.create_author(
                first_name="J.R.R.",
                last_name="Tolkien",
                bio="Author of The Lord of the Rings"
            )
            self.assertIsNotNone(author)

            
            genre_fantasy = GenreService.create_genre("Fantasy")
            self.assertIsNotNone(genre_fantasy)

            
            book = BookService.create_book(
                title="The Lord of the Rings",
                publisher_id=publisher.publisher_id,
                cover_image="lotr_cover.jpg",
                author_id=author.author_id,
                synopsis="An epic fantasy novel."
            )
            self.assertIsNotNone(book) 
            updated_book = BookService.update_book(
                book_id=book.book_id,
                title="The Hobbit",
                synopsis="A prequel to The Lord of the Rings."
            )
            self.assertIsNotNone(updated_book)
            self.assertEqual(updated_book.title, "The Hobbit")
            self.assertEqual(updated_book.synopsis, "A prequel to The Lord of the Rings.")

            BookService.delete_book(updated_book.book_id)
            PublisherService.delete_publisher(publisher.publisher_id)
            AuthorService.delete_author(author.author_id)
            GenreService.delete_genre(genre_fantasy.genre_id)

    def test_delete_book(self):
        with self.app.app_context():
            publisher = PublisherService.create_publisher(name="DC Comics")
            self.assertIsNotNone(publisher)
            

            author = AuthorService.create_author(
                first_name="J.R.R.",
                last_name="Tolkien",
                bio="Author of The Lord of the Rings"
            )
            self.assertIsNotNone(author)

            genre_fantasy = GenreService.create_genre("Fantasy")
            self.assertIsNotNone(genre_fantasy)

            book = BookService.create_book(
                title="The Lord of the Rings",
                publisher_id=publisher.publisher_id,
                cover_image="lotr_cover.jpg",
                author_id=author.author_id,
                synopsis="An epic fantasy novel."
            )
            self.assertIsNotNone(book)
            success = BookService.delete_book(book.book_id)
            self.assertTrue(success)


            deleted_book = BookService.get_book_by_id(book.book_id)
            self.assertIsNone(deleted_book)


            PublisherService.delete_publisher(publisher.publisher_id)
            AuthorService.delete_author(author.author_id)
            GenreService.delete_genre(genre_fantasy.genre_id)

    def test_add_genre_to_book(self):
        with self.app.app_context():

            publisher = PublisherService.create_publisher(name="DC Comics")
            self.assertIsNotNone(publisher)
            
            author = AuthorService.create_author(
                first_name="J.R.R.",
                last_name="Tolkien",
                bio="Author of The Lord of the Rings"
            )
            self.assertIsNotNone(author)

            # Create Genre
            genre_fantasy = GenreService.create_genre(name="Fantasy")
            self.assertIsNotNone(genre_fantasy)
            book = BookService.create_book(
                title="The Lord of the Rings",
                publisher_id=publisher.publisher_id,
                cover_image="img.jpg",
                author_id=author.author_id,
                synopsis="An epic fantasy hisotry."
            )
            self.assertIsNotNone(book)

            success = BookService.add_genre_to_book(book.book_id, genre_fantasy.genre_id)
            self.assertTrue(success)
           
            book = BookService.get_book_by_id(book.book_id)
            self.assertIsNotNone(book)
            
            genres = [genre.genre_id for genre in book.genres]
            self.assertIn(genre_fantasy.genre_id, genres)
           
            BookService.delete_book(book.book_id)
            PublisherService.delete_publisher(publisher.publisher_id)
            AuthorService.delete_author(author.author_id)
            GenreService.delete_genre(genre_fantasy.genre_id)

if __name__ == '__main__':
    unittest.main()
