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

def Create_app(config_filename):
    """ Creates and configures a flask app to be deployed.
    
        :type config_filename: str
        :param config_filename: Path of configuration file. 
    """
    app = Flask(__name__)
    app.config.from_object(config_filename)
    CORS(app)

    from views import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix = '/api')
    
    return app