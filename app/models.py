from datetime import datetime
from mongoengine import fields as fl
from flask_mongoengine import Document


class BaseDocument(Document):
    meta = {
        'abstract': True
    }

    date_created = fl.DateTimeField(default=datetime.utcnow)
    date_edited = fl.DateTimeField(default=datetime.utcnow)


class User(BaseDocument):
    username = fl.StringField(max_length=30, unique=True)
    # TODO: implement password hashing!
    password_hash = fl.StringField(max_length=30)
    avatar = fl.URLField()


class Channel(BaseDocument):
    name = fl.StringField(max_length=30, unique=True)
    users_in_chat = fl.ListField(fl.ReferenceField(User))


class Message(BaseDocument):
    user = fl.ReferenceField(User)
    message = fl.StringField()
