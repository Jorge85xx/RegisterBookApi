from extensions import db
from sqlalchemy.exc import SQLAlchemyError
from models import Publisher


class PublisherService:
    @staticmethod
    def create_publisher(name):
        try:
            publisher = Publisher(
                name=name
            )
            db.session.add(publisher)
            db.session.commit()
            return publisher
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error creating publisher: {e}")
            return None

    @staticmethod
    def get_publisher_by_id(publisher_id):
        try:
            return Publisher.query.get(publisher_id)
        except SQLAlchemyError as e:
            print(f"Error find publisher: {e}")
            return None

    @staticmethod
    def update_publisher(publisher_id, **kwargs):
        try:
            publisher = Publisher.query.get(publisher_id)
            if not publisher:
                print("Publisher not found")
                return None
            for key, value in kwargs.items():
                if hasattr(publisher, key):
                    setattr(publisher, key, value)
            db.session.commit()
            return publisher
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error updating publisher: {e}")
            return None

    @staticmethod
    def delete_publisher(publisher_id):
        try:
            publisher = Publisher.query.get(publisher_id)
            if not publisher:
                print("Publisher not found")
                return None
            db.session.delete(publisher)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error deleting publisher: {e}")
            return None
