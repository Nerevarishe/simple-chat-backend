from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config


db = MongoEngine()
jwt = JWTManager()

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    jwt.init_app(app)
    CORS()

    # Blueprints
    from app.frontpage import bp as frontpage_bp
    app.register_blueprint(frontpage_bp, url_prefix='/')

    return app
