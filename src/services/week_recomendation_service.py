from extensions import db
from sqlalchemy.exc import SQLAlchemyError
from models import WeekRecomendation, Book

class WeekRecomendationService:
    @staticmethod
    def create_recommendation(book_id, title, citation):
        try:
            recommendation = WeekRecomendation(
                book_id=book_id,
                title=title,
                citation=citation
            )
            db.session.add(recommendation)
            db.session.commit()
            return recommendation
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error creating week recommendation: {e}")
            return None

    @staticmethod
    def get_recommendation_by_id(recomendation_id):
        try:
            return WeekRecomendation.query.get(recomendation_id)
        except SQLAlchemyError as e:
            print(f"Error finding week recommendation: {e}")
            return None

    @staticmethod
    def update_recommendation(recomendation_id, **kwargs):
        try:
            recommendation = WeekRecomendation.query.get(recomendation_id)
            if not recommendation:
                print("Week recommendation not found")
                return None
            for key, value in kwargs.items():
                if hasattr(recommendation, key):
                    setattr(recommendation, key, value)
            db.session.commit()
            return recommendation
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error updating week recommendation: {e}")
            return None

    @staticmethod
    def delete_recommendation(recomendation_id):
        try:
            recommendation = WeekRecomendation.query.get(recomendation_id)
            if not recommendation:
                print("Week recommendation not found")
                return None
            db.session.delete(recommendation)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error deleting week recommendation: {e}")
            return None

    @staticmethod
    def get_recommendations_for_book(book_id):
        try:
            return WeekRecomendation.query.filter_by(book_id=book_id).all()
        except SQLAlchemyError as e:
            print(f"Error retrieving recommendations for book: {e}")
            return None
