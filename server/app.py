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

@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'

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

if __name__ == '__main__':
    app.run(port=5555, debug=True)

