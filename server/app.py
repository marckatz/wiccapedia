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
