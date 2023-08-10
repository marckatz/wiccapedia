from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
import difflib

from config import db, bcrypt


# Models go here!
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
        # returns most edits for a single page by user
        page_tup = db.session.query(Page, db.func.count(Edit.id).label('count')).join(Edit).filter(Edit.user_id == self.id).group_by(Edit.page_id).order_by(db.desc('count')).first()
        return f'{page_tup[0]} with {page_tup[1]} edits'

    @classmethod
    def get_most_edited_list(cls):
        most_edited_tuple = db.session.query(cls, db.func.count(Edit.id).label('edit_count')).join(Edit).group_by(Edit.user_id).order_by(db.desc('edit_count')).limit(3).all()
        return most_edited_tuple
        
    @validates('username')
    def validate_username(self, key, new_username):
        if len(new_username) < 5 or len(new_username) > 25:
            raise ValueError('Username must between 5 and 25 characters!')
        return new_username
    
    @validates('password_hash')
    def validate_password_hash(self, key, new_password):
        if len(new_password) < 6 or len(new_password) > 25:
            raise ValueError('Password must between 6 and 25 characters!')
        return new_password


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

    serialize_rules = ('-user.edits', '-page.edits',)

    @validates('diff')
    def validate_diff(self, key, new_diff):
        if not new_diff:
            raise ValueError("Cannot submit blank edit!")
        return new_diff

    def __repr__(self):
        return f'<Edit {self.id} {self.user_id} {self.page_id}>'



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

    def __repr__(self):
        return f'<Page {self.id} {self.title}>'
