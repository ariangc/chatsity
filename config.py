#!/usr/bin/env python

"""
      config.py
      ----------
      This module contains configuration variables for the flask application.
"""

__author__ = "Arian Gallardo"

import os

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
PORT = 9997
HOST = "0.0.0.0"
SECRET_KEY = 'flaskisfun'
TOKEN_EXP_MINUTES = 60000
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER="chatsity_admin", DB_PASS="chatsity2020", DB_ADDR="54.83.145.92", DB_NAME="chatsity")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Test variables
