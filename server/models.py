from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)

    edits = db.relationship('Edit', back_populates='user', cascade='all,delete-orphan')
    pages = association_proxy('edits', 'page')

    def __repr__(self):
        return f'<User {self.id} {self.username}>'

class Edit(db.Model, SerializerMixin):
    __tablename__ = 'edits'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    page_id = db.Column(db.Integer, db.ForeignKey('pages.id'))
    diff = db.Column(db.String)
    # time = db.Column(db.DateTime)

    user = db.relationship('User', back_populates='edits')
    page = db.relationship('Page', back_populates='edits')

    def __repr__(self):
        return f'<Edit {self.id} {self.user_id} {self.page_id}>'



class Page(db.Model, SerializerMixin):
    __tablename__ = 'pages'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    text = db.Column(db.String)

    edits = db.relationship('Edit', back_populates='page', cascade='all,delete-orphan')
    users = association_proxy('edits', 'user')

    def __repr__(self):
        return f'<Page {self.id} {self.title}>'

