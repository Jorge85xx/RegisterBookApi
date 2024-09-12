import unittest
from app import create_app
from extensions import db
from models import Book, Author, Publisher, Genre, BookGenre
from services.book_service import BookService
from config.test_config import TestingConfig

class BookServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()
        self.book_service = BookService()

        with self.app.app_context():
            db.create_all()
            
            self.author_id = 1  
            self.publisher_id = 1  
            self.genre_id = 1  

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()

    def test_create_book(self):
        with self.app.app_context():
            title = "The Great Gatsby"
            cover_image = "cover_image_url"
            synopsis = "A novel about the American dream."

            book = self.book_service.create_book(
                title=title,
                publisher_id=self.publisher_id,
                cover_image=cover_image,
                author_id=self.author_id,
                synopsis=synopsis
            )

            self.assertIsNotNone(book)
            self.assertEqual(book.title, title)
            self.assertEqual(book.publisher_id, self.publisher_id)
            self.assertEqual(book.cover_image, cover_image)
            self.assertEqual(book.author_id, self.author_id)
            self.assertEqual(book.synopsis, synopsis)
            self.book_service.delete_book(book.book_id)

    def test_get_books(self):
        with self.app.app_context():
            created_books = []
            for i in range(5):
                book = self.book_service.create_book(
                    title=f"Book {i}",
                    publisher_id=self.publisher_id,
                    cover_image="cover_image_url",
                    author_id=self.author_id,
                    synopsis=f"Synopsis {i}"
                )
                created_books.append(book)

        
            books = self.book_service.get_books(quantity=3)
            
            
            print(books)
            self.assertEqual(len(books), 3, "Should return exactly 3 books.")

            
            for book in created_books:
                self.book_service.delete_book(book.book_id)


    def test_get_books_with_author_and_genre(self):
        with self.app.app_context():
            books = self.book_service.get_books_with_author_and_genre(quantity=3)
            print(books)
            self.assertEqual(len(books), 3)
            

    def test_get_book_by_id(self):
        with self.app.app_context():
            book = self.book_service.create_book(
                title="1984",
                publisher_id=self.publisher_id,
                cover_image="cover_image_url",
                author_id=self.author_id,
                synopsis="A dystopian novel."
            )

            fetched_book = self.book_service.get_book_by_id(book.book_id)
            self.assertIsNotNone(fetched_book)
            self.assertEqual(fetched_book.title, "1984")
            self.assertEqual(fetched_book.synopsis, "A dystopian novel.")
            self.book_service.delete_book(book.book_id)

    def test_update_book(self):
        with self.app.app_context():
            book = self.book_service.create_book(
                title="To Kill a Mockingbird",
                publisher_id=self.publisher_id,
                cover_image="cover_image_url",
                author_id=self.author_id,
                synopsis="A novel about racial injustice."
            )

            updated_title = "To Kill a Mockingbird - Updated"
            updated_book = self.book_service.update_book(
                book.book_id,
                title=updated_title
            )

            self.assertIsNotNone(updated_book)
            self.assertEqual(updated_book.title, updated_title)
            self.book_service.delete_book(book.book_id)

    def test_delete_book(self):
        with self.app.app_context():
            book = self.book_service.create_book(
                title="Moby Dick",
                publisher_id=self.publisher_id,
                cover_image="cover_image_url",
                author_id=self.author_id,
                synopsis="A novel about the quest to hunt a giant whale."
            )

            success = self.book_service.delete_book(book.book_id)
            self.assertTrue(success)

            deleted_book = self.book_service.get_book_by_id(book.book_id)
            self.assertIsNone(deleted_book)

    def test_add_genre_to_book(self):
        with self.app.app_context():
            book = self.book_service.create_book(
                title="Ender's Game",
                publisher_id=self.publisher_id,
                cover_image="cover_image_url",
                author_id=self.author_id,
                synopsis="A science fiction novel."
            )

            success = self.book_service.add_genre_to_book(book.book_id, self.genre_id)
            self.assertTrue(success)

            book_genres = (
                db.session.query(BookGenre)
                .filter(BookGenre.book_id == book.book_id)
                .filter(BookGenre.genre_id == self.genre_id)
                .all()
            )
            self.assertGreater(len(book_genres), 0)

    def test_get_books_by_genre(self):
        with self.app.app_context():
            books = self.book_service.get_books_by_genre(1)
            print(books)
            self.assertGreater(len(books), 0)
            self.assertEqual(books[0].title, "Clean Code")

if __name__ == '__main__':
    unittest.main()
