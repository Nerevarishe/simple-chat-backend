from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_socketio import SocketIO
from config import Config

db = MongoEngine()
jwt = JWTManager()
socketio = SocketIO()


def create_app(config=Config, debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.config.from_object(config)
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Blueprints
    # Frontpage
    from app.frontpage import bp as frontpage_bp
    app.register_blueprint(frontpage_bp, url_prefix='/')

    # Chat
    from app.api.v1.chat import bp as chat_bp
    app.register_blueprint(chat_bp)

    socketio.init_app(app, cors_allowed_origins="*")
    return app
