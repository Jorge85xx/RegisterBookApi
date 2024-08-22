import unittest
from app import create_app
from extensions import db
from models import Author
from services.author_service import AuthorService
from config.test_config import TestingConfig

class AuthorServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()
        self.author_service = AuthorService()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            

    def test_create_author(self):
        with self.app.app_context():
            first_name = "Frank"
            last_name = "Miller"
            bio = "American comic book writer, novelist, and film director."

            author = self.author_service.create_author(first_name=first_name, last_name=last_name, bio=bio)

            self.assertIsNotNone(author)
            self.assertEqual(author.first_name, first_name)
            self.assertEqual(author.last_name, last_name)
            self.assertEqual(author.bio, bio)
            self.author_service.delete_author(author.author_id)

    def test_get_author_by_id(self):
        with self.app.app_context():
            first_name = "Alan"
            last_name = "Moore"
            bio = "English writer known primarily for his work in comic books."

            author = self.author_service.create_author(first_name=first_name, last_name=last_name, bio=bio)

            fetched_author = self.author_service.get_author_by_id(author.author_id)
            self.assertIsNotNone(fetched_author)
            self.assertEqual(fetched_author.first_name, first_name)
            self.assertEqual(fetched_author.last_name, last_name)
            self.assertEqual(fetched_author.bio, bio)
            self.author_service.delete_author(author.author_id)

    def test_update_author(self):
        with self.app.app_context():
            first_name = "Stan"
            last_name = "Lee"
            bio = "American comic book writer, editor, publisher, and producer."

            author = self.author_service.create_author(first_name=first_name, last_name=last_name, bio=bio)

            updated_first_name = "Stanley"
            updated_last_name = "Lieber"
            updated_author = self.author_service.update_author(
                author.author_id,
                first_name=updated_first_name,
                last_name=updated_last_name
            )

            self.assertIsNotNone(updated_author)
            self.assertEqual(updated_author.first_name, updated_first_name)
            self.assertEqual(updated_author.last_name, updated_last_name)
            self.author_service.delete_author(author.author_id)

    def test_delete_author(self):
        with self.app.app_context():
            first_name = "Jack"
            last_name = "Kirby"
            bio = "American comic book artist, writer, and editor."

            author = self.author_service.create_author(first_name=first_name, last_name=last_name, bio=bio)

            success = self.author_service.delete_author(author.author_id)
            self.assertTrue(success)

            deleted_author = self.author_service.get_author_by_id(author.author_id)
            self.assertIsNone(deleted_author)

if __name__ == '__main__':
    unittest.main()
