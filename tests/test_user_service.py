import unittest
from src.app import create_app
from src.extensions import db
from src.models import User
from src.services.user_service import UserService

class UserServiceTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:2453@localhost/bookprojectteste' # banco de dados em memória para testes
        cls.client = cls.app.test_client()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_create_user(self):
        user = UserService.create_user(
            first_name='John',
            last_name='Doe',
            nickname='jdoe',
            cpf='12345678901',
            phone_number='555-5555',
            profile_picture='profile.jpg',
            password='password',
            quote='Hello World'
        )
        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_get_user_by_id(self):
        user = UserService.create_user(
            first_name='Jane',
            last_name='Doe',
            nickname='jdoe',
            cpf='12345678901',
            phone_number='555-5555',
            profile_picture='profile.jpg',
            password='password',
            quote='Hello World'
        )
        retrieved_user = UserService.get_user_by_id(user.id)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.id, user.id)

    def test_update_user(self):
        user = UserService.create_user(
            first_name='Jane',
            last_name='Doe',
            nickname='jdoe',
            cpf='12345678901',
            phone_number='555-5555',
            profile_picture='profile.jpg',
            password='password',
            quote='Hello World'
        )
        updated_user = UserService.update_user(user.id, first_name='Janet')
        self.assertIsNotNone(updated_user)
        self.assertEqual(updated_user.first_name, 'Janet')

    def test_delete_user(self):
        user = UserService.create_user(
            first_name='Jane',
            last_name='Doe',
            nickname='jdoe',
            cpf='12345678901',
            phone_number='555-5555',
            profile_picture='profile.jpg',
            password='password',
            quote='Hello World'
        )
        result = UserService.delete_user(user.id)
        self.assertTrue(result)
        self.assertIsNone(UserService.get_user_by_id(user.id))

if __name__ == '__main__':
    unittest.main()
