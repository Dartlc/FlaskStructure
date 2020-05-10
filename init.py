from logging.config import dictConfig
from flask import Flask
from flasgger import Swagger
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from loadconfig import load_config
from models import database


def init_logger() -> None:
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })


def initialize_flask_app(name: str, config: str = 'development') -> Flask:
    app = Flask(name)
    app = load_config(app=app, config_type=config)

    database.init_app(app=app)

    CORS(app)

    # initializing swagger
    swagger = Swagger(app, template={
        "openapi": "3.0.0",
        "info": {
            "tittle": "Bix Backend API",
            "version": "1.0",
            "description": "API For Bix",
            "contact": {
                "responsibleOrganization": "BIX IT ACADEMY",
                "email": "training@bixitacademy.com",
                "url": "bixitacademy.com"
            },
        },
        "produces": [
            "application/json",
        ],
    })

    # Initializing JWT token management
    jwt = JWTManager(app)

    init_logger()

    with app.app_context():
        pass
        # config modules here

    # app.register_blueprint()  # module blueprint
    # app.register_blueprint()  # module blueprint

    return app
