import unittest
from app import create_app
from extensions import db
from models import Genre
from services.genre_service import GenreService
from config.test_config import TestingConfig

class GenreServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()
        self.genre_service = GenreService()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()

    def test_create_genre(self):
        with self.app.app_context():
            genre_name = "tests"
            genre = self.genre_service.create_genre(name=genre_name)

            self.assertIsNotNone(genre)
            self.assertEqual(genre.name, genre_name)
            self.genre_service.delete_genre(genre.genre_id)

    def test_get_genre_by_id(self):
        with self.app.app_context():
            genre_name = "test"
            genre = self.genre_service.create_genre(name=genre_name)

            fetched_genre = self.genre_service.get_genre_by_id(genre.genre_id)
            self.assertIsNotNone(fetched_genre)
            self.assertEqual(fetched_genre.name, genre_name)
            self.genre_service.delete_genre(genre.genre_id)


    def test_update_genre(self):
        with self.app.app_context():
            genre_name = "test4"
            genre = self.genre_service.create_genre(name=genre_name)

            updated_name = "test5"
            updated_genre = self.genre_service.update_genre(genre.genre_id, updated_name)

            self.assertIsNotNone(updated_genre)
            self.assertEqual(updated_genre.name, updated_name)
            self.genre_service.delete_genre(updated_genre.genre_id)

    def test_delete_genre(self):
        with self.app.app_context():
            genre_name = "delete test"
            genre = self.genre_service.create_genre(name=genre_name)

            success = self.genre_service.delete_genre(genre.genre_id)
            self.assertTrue(success)

        
            with self.assertRaises(ValueError) as context:
                self.genre_service.get_genre_by_id(genre.genre_id)
        
            self.assertEqual(str(context.exception), f"Genre with ID {genre.genre_id} does not exist.")

if __name__ == '__main__':
    unittest.main()
