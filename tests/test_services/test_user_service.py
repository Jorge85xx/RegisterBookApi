import unittest
import random
import string
from app import create_app
from extensions import db
from models import User
from services.user_service import UserService
from config.test_config import TestingConfig
import json

class UserServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
    

    def _generate_random_string(self, length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def _generate_random_cpf(self):
        return ''.join(random.choices(string.digits, k=11))
      
    def test_create_and_delete_user(self):
        with self.app.app_context():
            first_name = self._generate_random_string()
            last_name = self._generate_random_string()
            nickname = self._generate_random_string()
            cpf = self._generate_random_cpf()
            phone_number = self._generate_random_string(10)  
            profile_picture = 'profile.jpg'
            password = 'password123'
            quote = self._generate_random_string()

            user = UserService.create_user(
                first_name=first_name,
                last_name=last_name,
                nickname=nickname,
                cpf=cpf,
                phone_number=phone_number,
                profile_picture=profile_picture,
                password=password,
                quote=quote
            )

            self.assertIsNotNone(user)
            self.assertEqual(user.first_name, first_name)

            success = UserService.delete_user(user.user_id)
            self.assertTrue(success)

            deleted_user = UserService.get_user_by_id(user.user_id)
            self.assertIsNone(deleted_user)
    def test_update_user(self):
        with self.app.app_context():
            original_nickname = self._generate_random_string()
            original_cpf = self._generate_random_cpf()
            user = UserService.create_user(
                first_name='John',
                last_name='Doe',
                nickname=original_nickname,
                cpf=original_cpf,
                phone_number='555-5557',
                profile_picture='profile3.jpg',
                password='password789',
                quote='Live and Let Live'
            )
            self.assertIsNotNone(user)
            self.assertEqual(user.nickname, original_nickname)
            self.assertEqual(user.cpf, original_cpf)
            updated_nickname = 'UpdatedNickname'
            updated_phone_number = '998986598'
            updated_cpf = self._generate_random_cpf()
            updated_user = UserService.update_user(
                user_id=user.user_id,
                nickname=updated_nickname,
                phone_number=updated_phone_number,
                cpf=updated_cpf
            )
            self.assertIsNotNone(updated_user)
            self.assertEqual(updated_user.nickname, updated_nickname)
            self.assertEqual(updated_user.phone_number, updated_phone_number)
            self.assertEqual(updated_user.cpf, updated_cpf)


            self.assertEqual(updated_user.first_name, user.first_name)
            self.assertEqual(updated_user.last_name, user.last_name)

            
            UserService.delete_user(user.user_id)
        
    def test_get_user_by_id(self):
        with self.app.app_context():
          nicknameee = self._generate_random_string()
          user = UserService.create_user(
                first_name='Jane',
                last_name='Doe',
                nickname=nicknameee,
                cpf= self._generate_random_cpf(),
                phone_number='555-5556',
                profile_picture='profile2.jpg',
                password='password456',
                quote='Carpe Diem!'
            )

          fetched_user = UserService.get_user_by_id(user.user_id)
          self.assertIsNotNone(fetched_user)
          self.assertEqual(fetched_user.nickname, nicknameee)
          UserService.delete_user(user.user_id)
          
          #testar o update com e sem erro 
            
            
    def test_create_user_with_missing_fields(self):
        with self.app.app_context():
            with self.assertRaises(TypeError) or self.assertRaises(ValueError):
                UserService.create_user(
                    first_name='Incomplete',
                    last_name='User',
                    nickname='incompleteuser',
                    cpf='12345678900'
                ) 


    def test_get_user_by_non_existent_id(self):
        with self.app.app_context():
            non_existent_id = 99999
            fetched_user = UserService.get_user_by_id(non_existent_id)
            self.assertIsNone(fetched_user)

    def _generate_random_string(self, length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def _generate_random_cpf(self):
        return ''.join(random.choices(string.digits, k=11))
            

if __name__ == '__main__':
    unittest.main()
