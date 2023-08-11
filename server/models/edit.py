from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.sql import func

from config import db

class Edit(db.Model, SerializerMixin):
    __tablename__ = 'edits'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    page_id = db.Column(db.Integer, db.ForeignKey('pages.id'))
    diff = db.Column(db.String)
    time = db.Column(db.DateTime, server_default=func.now())

    user = db.relationship('User', back_populates='edits')
    page = db.relationship('Page', back_populates='edits')

    serialize_rules = ('-user.edits', '-page.edits',)

    @validates('diff')
    def validate_diff(self, key, new_diff):
        if not new_diff:
            raise ValueError("Edit cannot be empty")
        return new_diff

    def __repr__(self):
        return f'<Edit {self.id} {self.user_id} {self.page_id}>'