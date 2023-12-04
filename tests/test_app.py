from app import app

import pytest

import sys
print(sys.path)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_display_secret(client):
    response = client.get('/')
    assert b'Username' in response.data
    assert b'Password' in response.data
