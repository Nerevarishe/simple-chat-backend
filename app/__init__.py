from flask import Flask, Blueprint,
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_cors import CORS


db = MongoEngine()
jwt = JWTManager()

def create_app(config):
    app = Flask(__name__)
    db.init_app(app)
    jwt.init_app(app)
    CORS()

    # Blueprints


    return app
