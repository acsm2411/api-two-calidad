import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_route():
    response = client.get('/authUsers/35319')
    assert response.status_code == 200

def test_route_string():
    response = client.get('/authUsers/test')
    assert response.status_code == 422

def test_route_no_content():
    response = client.get('/authUsers/-1')
    assert response.status_code == 204