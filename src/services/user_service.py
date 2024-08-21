from models import User
from extensions import db
from sqlalchemy.exc import SQLAlchemyError


class UserService:

    @staticmethod
    def create_user(first_name, last_name, nickname, cpf, phone_number, password, profile_picture="", quote=""):
        if not all([first_name, last_name, nickname, cpf, phone_number, profile_picture, password, quote]):
            raise ValueError("All fields are required except phone_number, profile_picture, and quote.")
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
            print(f"Error find user: {e}")
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

    