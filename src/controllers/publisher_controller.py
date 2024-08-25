from flask_restx import Namespace, Resource, fields
from services.publisher_service import PublisherService
from utils.response import response
from flask import request

api = Namespace('publishers', description='Publisher related operations')

publisher_model = api.model('Publisher', {
    'name': fields.String(required=True, description='The name of the publisher'),
})

@api.route('/')
class PublisherList(Resource):
    @api.doc('create_publisher')
    @api.expect(publisher_model)
    @api.response(201, 'Publisher created')
    @api.response(400, 'Failed to create publisher')
    def post(self):
        """Create a new publisher"""
        data = request.get_json()
        try:
            publisher = PublisherService.create_publisher(name=data.get('name'))
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

@api.route('/<int:publisher_id>')
@api.response(404, 'Publisher not found')
class PublisherResource(Resource):
    @api.doc('get_publisher')
    @api.response(200, 'Publisher details')
    def get(self, publisher_id):
        """Fetch a publisher by ID"""
        publisher = PublisherService.get_publisher_by_id(publisher_id)
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

    @api.doc('update_publisher')
    @api.expect(publisher_model)
    @api.response(200, 'Publisher updated')
    @api.response(400, 'Failed to update publisher')
    def put(self, publisher_id):
        """Update an existing publisher"""
        data = request.get_json()
        try:
            publisher = PublisherService.update_publisher(publisher_id, **data)
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

    @api.doc('delete_publisher')
    @api.response(204, 'Publisher deleted')
    @api.response(400, 'Failed to delete publisher')
    def delete(self, publisher_id):
        """Delete a publisher by ID"""
        try:
            success = PublisherService.delete_publisher(publisher_id)
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
