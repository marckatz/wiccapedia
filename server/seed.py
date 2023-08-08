#!/usr/bin/env python3

# Standard library imports
from random import randint as ri, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Edit, Page

if __name__ == "__main__":
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # clear database
        User.query.delete()
        Edit.query.delete()
        Page.query.delete()
        print("Datebase Cleared")
        marc = User(username="marc123", password_hash="123456")
        yu = User(username="yu1234", password_hash="abcdef")
        tj = User(username="tj1234", password_hash="qweasd")

        print("Adding users")
        page1 = Page(title="title1", text=\
"""<h1>header</h1>
<p>This is line 1</p>
<p>This is line 2</p>
<p>This is line 3</p>
<p>This is line 4</p>
""")
        page2 = Page(title="title2", text="text2\n")
        page3 = Page(title="title3", text="text3\n")
        print("Adding pages")

        db.session.add_all(
            [marc, yu, tj, page1, page2, page3]
        )
        db.session.commit()


        edit_text1 = """<h1>header</h1>
<p>This is a new line</p>
<p>This is line 1</p>
<p>This is line 2 modified</p>
<p>This is line 3</p>
"""
        edit_text2 = """<h1>header</h1>
<p>This is not a new line anymore</p>
<p>This is line 1</p>
<p>This is line 2 modified again</p>
<p>This is line 3</p>
"""
        edit1 = page1.create_edit(edit_text1, 1)
        page1.text = edit_text1
        edit2 = page1.create_edit(edit_text2, 1)
        page1.text = edit_text2
        db.session.add_all([edit1, edit2])
        db.session.commit()
        print("Adding edits")

        print("Finished Seeding")
