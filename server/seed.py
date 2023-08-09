#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

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

        page1 = Page(title="title1", text="text1\n")
        page2 = Page(title="title2", text="text2\n")
        page3 = Page(title="title3", text="text3\n")

        # edit1 = Edit(user_id=1, page_id=1, diff='diff1')
        # edit2 = Edit(user_id=2, page_id=2, diff='diff2')
        # edit3 = Edit(user_id=3, page_id=3, diff='diff3')
        # edit4 = Edit(user_id=1, page_id=3, diff='diff4')

        db.session.add_all(
            [marc, yu, tj, page1, page2, page3]
        )  # ,edit1,edit2,edit3,edit4])
        db.session.commit()
        print("Finished Seeding")
