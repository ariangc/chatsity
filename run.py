#!/usr/bin/env python

"""
      run.py
      ----------
      This module calls necessary parameters and configuration
      variables to execute the flask application.
"""

__author__ = "Arian Gallardo"

from app import Create_app

app = Create_app('config')

if __name__ == '__main__':
    app.run(
        host = app.config['HOST'],
        port = app.config['PORT'],
        debug = app.config['DEBUG']
    )