from flask import Blueprint, request
from services.user_service import UserService
from utils.response import response  


class UserController:
    def __init__(self, app=None):
        self.user_bp = Blueprint('users', __name__, url_prefix='/users')
        self.user_service = UserService()

        # Register routes
        self.user_bp.add_url_rule('/', 'create_user', self.create_user, methods=['POST'])
        self.user_bp.add_url_rule('/<int:user_id>', 'get_user', self.get_user, methods=['GET'])
        self.user_bp.add_url_rule('/<int:user_id>', 'update_user', self.update_user, methods=['PUT'])
        self.user_bp.add_url_rule('/<int:user_id>', 'delete_user', self.delete_user, methods=['DELETE'])

        if app:
            self.init_app(app)

    def init_app(self, app):
        app.register_blueprint(self.user_bp)

    def create_user(self):
        data = request.get_json()
        try:
            user = self.user_service.create_user(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                nickname=data.get('nickname'),
                cpf=data.get('cpf'),
                phone_number=data.get('phone_number'),
                profile_picture=data.get('profile_picture'),
                password=data.get('password'),  # Inclua o password aqui
                quote=data.get('quote')
            )
            if user:
                return response(
                    status=201,
                    name_of_content='user',
                    content={
                        'id': user.user_id,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'nickname': user.nickname,
                        'cpf': user.cpf,
                        'phone_number': user.phone_number,
                        'profile_picture': user.profile_picture,
                        'quote': user.quote
                    }
                )
            else:
                return response(
                    status=400,
                    name_of_content='error',
                    content={},
                    message='Failed to create user'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )

    def get_user(self, user_id):
        user = self.user_service.get_user_by_id(user_id)
        if user:
            return response(
                status=200,
                name_of_content='user',
                content={
                    'id': user.user_id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'nickname': user.nickname,
                    'cpf': user.cpf,
                    'phone_number': user.phone_number,
                    'profile_picture': user.profile_picture,
                    'quote': user.quote
                }
            )
        else:
            return response(
                status=404,
                name_of_content='error',
                content={},
                message='User not found'
            )

    def update_user(self, user_id):
        data = request.get_json()
        try:
            user = self.user_service.update_user(user_id, **data)
            if user:
                return response(
                    status=200,
                    name_of_content='user',
                    content={
                        'id': user.user_id,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'nickname': user.nickname,
                        'cpf': user.cpf,
                        'phone_number': user.phone_number,
                        'profile_picture': user.profile_picture,
                        'quote': user.quote
                    }
                )
            else:
                return response(
                    status=404,
                    name_of_content='error',
                    content={},
                    message='User not found'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )

    def delete_user(self, user_id):
        try:
            success = self.user_service.delete_user(user_id)
            if success:
                return response(
                    status=204,
                    name_of_content='message',
                    content={},
                    message='User deleted successfully'
                )
            else:
                return response(
                    status=404,
                    name_of_content='error',
                    content={},
                    message='User not found'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )
