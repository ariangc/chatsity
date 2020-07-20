#!/usr/bin/env python

"""
      app.py
      ----------
      This module contains neccesary functions to create the flask application
      to be deployed.
"""

__author__ = "Arian Gallardo"

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.user import User
from models.message import Message
from models.chatroom import Chatroom

def Create_app(config_filename):
    """ Creates and configures a flask app to be deployed.
    
        :type config_filename: str
        :param config_filename: Path of configuration file. 
    """
    app = Flask(__name__)
    app.config.from_object(config_filename)
    db.init_app(app)
    CORS(app)

    from views import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix = '/api')
    
    return app