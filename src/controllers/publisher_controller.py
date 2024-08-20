from flask import Blueprint, request
from services.publisher_service import PublisherService
from utils.response import response  


class PublisherController:
    def __init__(self, app=None):
        self.publisher_bp = Blueprint('publishers', __name__, url_prefix='/publishers')
        self.publisher_service = PublisherService()

        # Register routes
        self.publisher_bp.add_url_rule('/', 'create_publisher', self.create_publisher, methods=['POST'])
        self.publisher_bp.add_url_rule('/<int:publisher_id>', 'get_publisher', self.get_publisher, methods=['GET'])
        self.publisher_bp.add_url_rule('/<int:publisher_id>', 'update_publisher', self.update_publisher, methods=['PUT'])
        self.publisher_bp.add_url_rule('/<int:publisher_id>', 'delete_publisher', self.delete_publisher, methods=['DELETE'])

        if app:
            self.init_app(app)

    def init_app(self, app):
        app.register_blueprint(self.publisher_bp)

    def create_publisher(self):
        data = request.get_json()
        try:
            publisher = self.publisher_service.create_publisher(
                name=data.get('name')
            )
            if publisher:
                return response(
                    status=201,
                    name_of_content='publisher',
                    content={
                        'publisher_id': publisher.publisher_id,
                        'name': publisher.name
                    }
                )
            else:
                return response(
                    status=400,
                    name_of_content='error',
                    content={},
                    message='Failed to create publisher'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )

    def get_publisher(self, publisher_id):
        publisher = self.publisher_service.get_publisher_by_id(publisher_id)
        if publisher:
            return response(
                status=200,
                name_of_content='publisher',
                content={
                    'publisher_id': publisher.publisher_id,
                    'name': publisher.name
                }
            )
        else:
            return response(
                status=404,
                name_of_content='error',
                content={},
                message='Publisher not found'
            )

    def update_publisher(self, publisher_id):
        data = request.get_json()
        try:
            publisher = self.publisher_service.update_publisher(publisher_id, **data)
            if publisher:
                return response(
                    status=200,
                    name_of_content='publisher',
                    content={
                        'publisher_id': publisher.publisher_id,
                        'name': publisher.name
                    }
                )
            else:
                return response(
                    status=404,
                    name_of_content='error',
                    content={},
                    message='Publisher not found'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )

    def delete_publisher(self, publisher_id):
        try:
            success = self.publisher_service.delete_publisher(publisher_id)
            if success:
                return response(
                    status=204,
                    name_of_content='message',
                    content={},
                    message='Publisher deleted successfully'
                )
            else:
                return response(
                    status=404,
                    name_of_content='error',
                    content={},
                    message='Publisher not found'
                )
        except Exception as e:
            return response(
                status=400,
                name_of_content='error',
                content={},
                message=str(e)
            )
