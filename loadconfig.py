import os
import yaml
import uuid

from flask import Flask
from typing import Dict


def load_config(app: Flask, config_type: str = 'development') -> Flask:
    file_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.yml')
    config_file = open(file_name)
    all_config: Dict = yaml.safe_load(config_file)
    config_file.close()

    config = {
        'development': all_config['DevelopmentConfig'],
        'default': all_config['DevelopmentConfig']
    }

    app.config['DEBUG'] = config[config_type]['DEBUG']
    app.config['SQLALCHEMY_DATABASE_URI'] = config[config_type]["SQLALCHEMY_DATABASE_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config[config_type]["SQLALCHEMY_TRACK_MODIFICATIONS"]
    app.config['MYSQL_DATABASE_CHARSET'] = config[config_type]["MYSQL_DATABASE_CHARSET"]

    app.secret_key = str(uuid.uuid4())
    return app
