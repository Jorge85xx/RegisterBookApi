from extensions import db


class UserPreferences(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    preference_name = db.Column(db.String(50), nullable=False)
    preference_value = db.Column(db.String(255))

    # Relationships
    user = db.relationship('User', backref=db.backref('preferences', uselist=False))

    def __repr__(self):
        return f'<UserPreferences UserID={self.user_id} Preference={self.preference_name}>'
