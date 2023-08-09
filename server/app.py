#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session
from flask_restful import Resource

# Local imports
from config import app, db, api

# Add your model imports
from models import User, Page, Edit

# Views go here!


@app.route("/")
def index():
    return "<h1>Phase 4 Project Server</h1>"

class Users(Resource):
    def get (self):
        return make_response ([u.to_dict() for u in User.query.all()])

    def post(self):
        data = request.get_json()
        try:
            # Add password
            new_user = User(username=data['username'], password_hash=data['password'])
        except Exception as e:
            return make_response({"message": "Error while creating user: " + str(e)}, 400)
        
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id

        return make_response(new_user.to_dict(), 201)

class UserById(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({"message" : "we have an error"}, 404)
        
        return make_response(user.to_dict())
    
    def patch(self, id):
        data = request.get_json()
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({"message" : "we have an error"}, 404)

        for key in data:
            setattr(user, key, data[key])

        db.session.commit()
        return make_response(user.to_dict())

api.add_resource(UserById, '/users/<int:id>')
api.add_resource(Users, '/users')

#RESTful Page views
class Pages(Resource):
    def get(self):
        pages = [page.to_dict(only=('id','title')) for page in Page.query.all()]
        return make_response(pages, 200)

    def post(self):
        try:
            data = request.get_json()
            new_page = Page(
                title = data['title'],
                text = data['text']
            )
            db.session.add(new_page)
            db.session.commit()
            return make_response(new_page.to_dict(), 201)
        except Exception as e:
            return make_response({'error':str(e)}, 400)

api.add_resource(Pages, '/pages')

class PagesById(Resource):
    def get(self, id):
        try:
            page = Page.query.filter_by(id=id).first()
            return make_response(page.to_dict(), 200)
        except:
            return make_response({'error':"Page not found"}, 404)

    #also send user_id
    def patch(self, id):
        try:
            page = Page.query.filter_by(id=id).first()
            data = request.get_json()
            for attr in data:
                setattr(page, attr, data[attr])
            db.session.commit()
            return make_response(page.to_dict(), 202)
        except AttributeError:
            return make_response({'error':'Page not found'}, 404)
        except Exception as e:
            return make_response({'error':str(e)}, 400)

    def delete(self, id):
        try:
            page = Page.query.filter_by(id=id).first()
            db.session.delete(page)
            db.session.commit()
            return make_response({}, 204)
        except:
            return make_response({'error':'Page not found'}, 404)

api.add_resource(PagesById, '/pages/<int:id>')

class Edits(Resource):
    def get(self):
        return make_response([edit.to_dict() for edit in Edit.query.all()])


    def post(self):
        data = request.json
        try:
            edit = Edit(
                user_id=data['user_id'], 
                page_id=data['page_id']
            )
            db.session.add(edit)
            db.session.commit()
            return make_response(edit.to_dict(), 201)
        except Exception as e:
            return make_response({'errors': [str(e)]}, 422)
        
api.add_resource( Edits, '/edits' )
        
class EditById(Resource):
    def get(self, id):
        edit = Edit.query.filter(Edit.id == id).first()
        if edit:
            return make_response(edit.to_dict())
        else:
            return make_response({ 'error': 'can not find that edit' }, 404 )

api.add_resource( EditById, '/edits/<int:id>')


"""
expects JSON of the format:
{
    page_id: <int>,
    user_id: <int>,
    new_text: <string>
}
"""
@app.route('/create_edit', methods=['POST'])
def add_edit_and_patch_page():
    data = request.get_json()
    new_text = data['new_text']
    if new_text[-1] != '\n':
        new_text += '\n'
    page = Page.query.filter_by(id=data['page_id']).first()
    new_edit = page.create_edit(new_text, data['user_id'])
    page.text = new_text
    db.session.add(new_edit)
    db.session.commit()
    return make_response(new_edit.to_dict(), 201)

@app.route('/search_by_title/<string:search>')
def search_by_title(search):
    pages = Page.query.filter(Page.title.like(f'%{search}%')).all()
    if not pages:
        return make_response({'error':f'No pages found matching "{search}"'}, 404)
    page_dicts = [p.to_dict(only=('title','id')) for p in pages]
    return make_response(page_dicts, 200)

@app.route('/pages/<string:title>')
def page_by_title(title):
    page = Page.query.filter_by(title=title).first()
    if page:
        return make_response(page.to_dict(), 200)
    else:
        return make_response({'error':f'page "{title}" not found'}, 404)
    

# Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    # Check if user exists
    user = User.query.filter_by(username=username).first()
    if not user:
        return make_response({'error': 'User not found'}, 404)
    
    # Authenticate the user
    if user.authenticate(password):
        session['user_id'] = user.id
        return make_response(user.to_dict(), 200)
    else:
        return make_response({'error': 'Incorrect password'}, 401)

# Logout
@app.route('/logout', methods=['DELETE'])
def logout():
    session.pop('user_id', None)
    return make_response({'message': 'Logged out successfully'}, 204)

@app.route('/check_session')
def check_session ():
    user = User.query.filter(User.id == session.get('user_id')).first()
    if user:
        return make_response (user.to_dict())
    else:
        return {'message': '401: Not Authorized'}, 401    

@app.route('/get_user_info')
def get_user_info():
    user_stats = db.session.query(User, db.func.count(Edit.id).label('edit_count')).join(Edit).group_by(Edit.user_id).order_by(db.desc('edit_count')).limit(3).all()
    dict_list = []
    for tuple in user_stats:
        res_dict = tuple[0].to_dict(only = ('username', 'id'))
        res_dict['num_of_edits'] = tuple[1]
        dict_list.append(res_dict)
    
    return make_response(dict_list)

@app.route('/get_page_info')
def get_page_info():
    page_stats = db.session.query(Page, db.func.count(Edit.id).label('edit_count')).join(Edit).group_by(Edit.page_id).order_by(db.desc('edit_count')).limit(3).all()
    dict_list = []
    for tuple in page_stats:
        res_dict = tuple[0].to_dict(only = ('title', 'id'))
        res_dict['num_of_edits'] = tuple[1]
        dict_list.append(res_dict)
    
    return make_response(dict_list)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
