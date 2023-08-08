#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
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
            new_user = User(username = data['username'])
        except Exception:
            return make_response({"message" : "we have an error"}, 404)
        db.session.add(new_user)
        db.session.commit()

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
            edit = Edit(user_id=data["user_id"], page_id=data["page_id"])
            db.session.add(edit)
            db.session.commit()
            return make_response(edit.to_dict(), 201)
        except Exception as e:
            return make_response({"errors": [str(e)]}, 422)
        
api.add_resource( Edits, '/edits' )
        
class EditById(Resource):
    def get(self, id):
        edit = Edit.query.filter(Edit.id == id).first()
        if edit:
            return make_response(edit.to_dict())
        else:
            return make_response({ 'error': 'can not find that edit' }, 404 )

api.add_resource( EditById, '/edits/<int:id>')

if __name__ == "__main__":
    app.run(port=5555, debug=True)
