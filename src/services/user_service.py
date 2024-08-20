from models import User
from extensions import db
from sqlalchemy.exc import SQLAlchemyError


class UserService:

    @staticmethod
    def create_user(first_name, last_name, nickname, cpf, phone_number, profile_picture, password, quote):
        try:
            user = User(
                first_name=first_name,
                last_name=last_name,
                nickname=nickname,
                cpf=cpf,
                phone_number=phone_number,
                profile_picture=profile_picture,
                password=password,
                quote=quote
            )
            db.session.add(user)
            db.session.commit()
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"error creating user, try again\n {e}")
            return None

    @staticmethod
    def get_user_by_id(user_id):
        try:
            return User.query.get(user_id)
        except SQLAlchemyError as e:
            print(f"Error retrieving user: {e}")
            return None

    @staticmethod
    def update_user(user_id, **kwargs):
        try:
            user = User.query.get(user_id)
            if not user:
                print("User not found")
                return None
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            db.session.commit()
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error updating user: {e}")
            return None

    @staticmethod
    def delete_user(user_id):
        try:
            user = User.query.get(user_id)
            if not user:
                print("User not found")
                return None
            db.session.delete(user)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error deleting user: {e}")
            return None

    @staticmethod
    def add_dc_users():
        # Instanciar o UserService
        user_service = UserService()

        # Dados dos personagens da DC Comics
        users = [
            {"first_name": "Bruce", "last_name": "Wayne", "nickname": "Batman", "cpf": "12345678900", "phone_number": "555-1234", "profile_picture": "http://example.com/batman.jpg", "password": "batman123", "quote": "I am Batman"},
            {"first_name": "Clark", "last_name": "Kent", "nickname": "Superman", "cpf": "12345678901", "phone_number": "555-5678", "profile_picture": "http://example.com/superman.jpg", "password": "superman123", "quote": "I can do this all day"},
            {"first_name": "Diana", "last_name": "Prince", "nickname": "Wonder Woman", "cpf": "12345678902", "phone_number": "555-9101", "profile_picture": "http://example.com/wonderwoman.jpg", "password": "wonderwoman123", "quote": "I am Wonder Woman"},
            {"first_name": "Barry", "last_name": "Allen", "nickname": "Flash", "cpf": "12345678903", "phone_number": "555-1122", "profile_picture": "http://example.com/flash.jpg", "password": "flash123", "quote": "Fastest man alive"},
            {"first_name": "Hal", "last_name": "Jordan", "nickname": "Green Lantern", "cpf": "12345678904", "phone_number": "555-3344", "profile_picture": "http://example.com/greenlantern.jpg", "password": "greenlantern123", "quote": "In brightest day, in blackest night"}
        ]

        # Adicionar usuários ao banco de dados
        added_users = []
        for user_data in users:
            user = user_service.create_user(**user_data)
            if user:
                added_users.append({
                    'id': user.user_id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'nickname': user.nickname,
                    'cpf': user.cpf,
                    'phone_number': user.phone_number,
                    'profile_picture': user.profile_picture,
                    'quote': user.quote
                })

        return added_users

