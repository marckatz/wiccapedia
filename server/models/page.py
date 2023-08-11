from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
import difflib

from config import db
from .edit import Edit

class Page(db.Model, SerializerMixin):
    __tablename__ = 'pages'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    text = db.Column(db.String)
    author = db.Column(db.String)

    edits = db.relationship('Edit', back_populates='page', cascade='all,delete-orphan')
    users = association_proxy('edits', 'user')

    serialize_rules = ('-edits.page',)

    def create_edit(self, new_text, user_id):
        old_text_list = self.text.splitlines(keepends=True)
        new_text_list = new_text.splitlines(keepends=True)
        diff = difflib.unified_diff(old_text_list, new_text_list)
        diff_string = ''.join(l for l in diff)
        new_edit = Edit(
            page_id = self.id,
            user_id = user_id,
            diff = diff_string
        )
        return new_edit

    @property
    def last_to_edit(self):
        return self.edits[-1].user
    @classmethod
    def get_most_edited_list(cls):
        most_edited_tuple = db.session.query(cls, db.func.count(Edit.id).label('edit_count')).join(Edit).group_by(Edit.page_id).order_by(db.desc('edit_count')).limit(3).all()
        return most_edited_tuple
    
    @validates('title')
    def validate_title(self, key, new_title):
        if not new_title:
            raise ValueError("Title cannot be empty")
        if not isinstance(new_title, str):
            raise ValueError("Title must be String")
        return new_title
    
    @validates('text')
    def validate_text(self, key, new_text):
        if not new_text:
            raise ValueError("Text cannot be empty")
        return new_text

    def __repr__(self):
        return f'<Page {self.id} {self.title}>'
