import unittest
from app import create_app
from extensions import db
from models import Publisher
from services.publisher_service import PublisherService
from config.test_config import TestingConfig

class PublisherServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()
        self.publisher_service = PublisherService()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()

    def test_create_publisher(self):
        with self.app.app_context():
            publisher_name = "Batman Books"
            publisher = self.publisher_service.create_publisher(name=publisher_name)

            self.assertIsNotNone(publisher)
            self.assertEqual(publisher.name, publisher_name)

    def test_get_publisher_by_id(self):
        with self.app.app_context():
            publisher_name = "HarperCollins"
            publisher = self.publisher_service.create_publisher(name=publisher_name)

            fetched_publisher = self.publisher_service.get_publisher_by_id(publisher.publisher_id)
            self.assertIsNotNone(fetched_publisher)
            self.assertEqual(fetched_publisher.name, publisher_name)

    def test_update_publisher(self):
        with self.app.app_context():
            publisher_name = "Testando"
            publisher = self.publisher_service.create_publisher(name=publisher_name)
            print(publisher.name)
            print(publisher.publisher_id)
            
            updated_name = "Updates"
            updated_publisher = self.publisher_service.update_publisher(publisher.publisher_id, name=updated_name)
            print(updated_publisher.name)
            print(updated_publisher.publisher_id)
            self.assertIsNotNone(updated_publisher)
            self.assertEqual(updated_publisher.name, updated_name)
            self.publisher_service.delete_publisher(updated_publisher.publisher_id)

    def test_delete_publisher(self):
        with self.app.app_context():
            publisher_name = "richarlison"
            publisher = self.publisher_service.create_publisher(name=publisher_name)

            success = self.publisher_service.delete_publisher(publisher.publisher_id)
            self.assertTrue(success)

            deleted_publisher = self.publisher_service.get_publisher_by_id(publisher.publisher_id)
            self.assertIsNone(deleted_publisher)

if __name__ == '__main__':
    unittest.main()
