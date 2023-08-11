from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db, bcrypt
from .edit import Edit

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)

    # add name and password
    _password_hash = db.Column(db.String, nullable=False)

    edits = db.relationship('Edit', back_populates='user', cascade='all,delete-orphan')
    pages = association_proxy('edits', 'page')

    serialize_rules = ('-edits.user', '-_password_hash',)

    # add password property
    @property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, new_password_string):
        plain_byte_obj = new_password_string.encode('utf-8')
        encrypted_hash_object = bcrypt.generate_password_hash(plain_byte_obj)
        hash_object_as_string = encrypted_hash_object.decode('utf-8')
        self._password_hash = hash_object_as_string

    def authenticate(self, some_string):
        return bcrypt.check_password_hash(self.password_hash, some_string.encode('utf-8'))

    @property
    def most_edited_page(self):
        from .page import Page
        # returns most edits for a single page by user
        page_tup = db.session.query(Page, db.func.count(Edit.id).label('count')).join(Edit).filter(Edit.user_id == self.id).group_by(Edit.page_id).order_by(db.desc('count')).first()
        return f'{page_tup[0]} with {page_tup[1]} edits'
    
    
    @classmethod
    def get_most_edited_list(cls):
        most_edited_tuple = db.session.query(cls, db.func.count(Edit.id).label('edit_count')).join(Edit).group_by(Edit.user_id).order_by(db.desc('edit_count')).limit(3).all()
        return most_edited_tuple
    
    @validates('username')
    def validate_username(self, key, new_username):
        if not isinstance(new_username, str) or len(new_username) < 5 or len(new_username) > 25:
            raise ValueError('Username must String between 5 and 25 characters')
        return new_username
    
    @validates('password_hash')
    def validate_password_hash(self, key, new_password):
        if not isinstance(new_password, str) or len(new_password) < 6 or len(new_password) > 25:
            raise ValueError('Password must between 6 and 25 characters')
        return new_password


    def __repr__(self):
        return f'<User {self.id} {self.username}>'