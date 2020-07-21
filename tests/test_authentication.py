#!/usr/bin/env python

"""
    test_authentication.py
    ----------
    This module implements unit tests for authentication
    routines.
"""

__author__ = "Arian Gallardo"

import sys, os
import tempfile
import pytest

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')

from run import app

@pytest.fixture
def client():
    """ Yields an testing app object.
    """
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client

def login(client, email, password):
    """ Sends a request to the login service. 

        :type client: flask.testing.FlaskClient
        :param client: Flask testing app client.

        :type email: str
        :param email: Email of user.

        :type password: str
        :param password: Password of user.
    """
    print(type(client))
    return client.post('api/login', json=dict(
        email=email,
        password=password
    ), follow_redirects = True)

def logout(client):
    """ Sends a request to the logout service. 

        :type client: flask.testing.FlaskClient
        :param client: Flask testing app client.
    """
    return client.get('api/logout', follow_redirects = True)

def test_login(client):
    rv = login(client, 'ariangallardo21@gmail.com', 'Test_pwd21')
    assert b'error' not in rv.data