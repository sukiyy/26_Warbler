"""User model tests."""
# run these tests like:
# python -m unittest test_message_model.py

import os
from unittest import TestCase

from models import db, User, Message, Follows
from sqlalchemy.exc import IntegrityError
# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database
os.environ['DATABASE_URL'] = "postgresql:///warblertest"

# Now we can import app
from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data
db.create_all()

class MessageModelTestCase(TestCase):
    def setUp(self):
        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        db.session.commit()

        m = Message(text="testtext")
        u = User(username="testuser",
                    email="test@test.com",
                    password="password")
        
        u.messages.append(m)
        db.session.add(u)
        db.session.commit()

        self.client = app.test_client()

    def tearDown(self):
        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        db.session.commit()

    def test_user_model(self):
        m = Message(text='testtext2')
        u = User.query.filter_by(username='testuser').one()

        self.assertEqual(len(u.messages), 1)

        u.messages.append(m)
        db.session.commit()

        self.assertEqual(len(m.user.messages), 2)