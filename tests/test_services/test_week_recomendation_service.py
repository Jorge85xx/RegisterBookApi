import unittest
from app import create_app
from extensions import db
from models import Book, Author, Publisher, Genre, BookGenre
from services.week_recomendation_service import WeekRecomendationService
from config.test_config import TestingConfig

class WeekRecomendationServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()
        self.week_recomendation_service = WeekRecomendationService()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()

    def test_create_recomendation(self):
        with self.app.app_context():
            book = self.create_test_book()
            title = "Recomendation Title"
            citation = "A great quote from the book."

            recomendation = self.week_recomendation_service.create_recomendation(
                book_id=book.book_id,
                title=title,
                citation=citation
            )

            self.assertIsNotNone(recomendation)
            self.assertEqual(recomendation.book_id, book.book_id)
            self.assertEqual(recomendation.title, title)
            self.assertEqual(recomendation.citation, citation)
            self.week_recomendation_service.delete_recomendation(recomendation.recomendation_id)
            self.delete_test_book(book.book_id)

    def test_get_recomendation_by_id(self):
        with self.app.app_context():
            book = self.create_test_book()
            recomendation = self.week_recomendation_service.create_recomendation(
                book_id=book.book_id,
                title="Recomendation Title",
                citation="A great quote from the book."
            )

            fetched_recomendation = self.week_recomendation_service.get_recomendation_by_id(recomendation.recomendation_id)
            self.assertIsNotNone(fetched_recomendation)
            self.assertEqual(fetched_recomendation.title, "Recomendation Title")
            self.week_recomendation_service.delete_recomendation(recomendation.recomendation_id)
            self.delete_test_book(book.book_id)

    def test_update_recomendation(self):
        with self.app.app_context():
            book = self.create_test_book()
            recomendation = self.week_recomendation_service.create_recomendation(
                book_id=book.book_id,
                title="Recomendation Title",
                citation="A great quote from the book."
            )

            updated_title = "Updated Recomendation Title"
            updated_recomendation = self.week_recomendation_service.update_recomendation(
                recomendation.recomendation_id,
                title=updated_title
            )

            self.assertIsNotNone(updated_recomendation)
            self.assertEqual(updated_recomendation.title, updated_title)
            self.week_recomendation_service.delete_recomendation(recomendation.recomendation_id)
            self.delete_test_book(book.book_id)

    def test_delete_recomendation(self):
        with self.app.app_context():
            book = self.create_test_book()
            recomendation = self.week_recomendation_service.create_recomendation(
                book_id=book.book_id,
                title="Recomendation Title",
                citation="A great quote from the book."
            )

            success = self.week_recomendation_service.delete_recomendation(recomendation.recomendation_id)
            self.assertTrue(success)

            deleted_recomendation = self.week_recomendation_service.get_recomendation_by_id(recomendation.recomendation_id)
            self.assertIsNone(deleted_recomendation)
            self.delete_test_book(book.book_id)

    def test_get_latest_recomendation(self):
        with self.app.app_context():
            book = self.create_test_book()
            recomendation = self.week_recomendation_service.create_recomendation(
                book_id=book.book_id,
                title="Latest Recomendation",
                citation="A great quote from the book."
            )

            latest_recomendation = self.week_recomendation_service.get_latest_recomendation()
            self.assertIsNotNone(latest_recomendation)
            self.assertEqual(latest_recomendation.title, "Latest Recomendation")
            self.week_recomendation_service.delete_recomendation(recomendation.recomendation_id)
            self.delete_test_book(book.book_id)

    def create_test_book(self):
        book = Book(
            title="Test Book",
            publisher_id=1,
            cover_image="test_cover_image_url",
            author_id=1,
            synopsis="Test synopsis."
        )
        db.session.add(book)
        db.session.commit()
        return book

    def delete_test_book(self, book_id):
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)

if __name__ == '__main__':
    unittest.main()
