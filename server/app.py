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

if __name__ == '__main__':
    app.run(port=5555, debug=True)

