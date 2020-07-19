import os
import tempfile
import pytest

from run import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client

def login(client, email, password):
    return client.post('api/login', data=dict(
        email=email,
        password=password
    ), follow_redirects = True)

def logout(client, id_user):
    return client.post('api/logout', data=dict(
        id_user=id_user
    ), follow_redirects = True)

def test_login_logout(client):
    rv = login(client, app.config['USERNAME'], app.config['PASSWORD'])
    assert b'error' not in rv.data

    rv = logout(client, app.config['ID_USER'])
    assert b'Logged out succesfully.' in rv.data