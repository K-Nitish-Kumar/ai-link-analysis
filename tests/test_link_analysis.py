from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_health(): assert client.get('/').status_code==200
def test_invalid(): assert client.post('/link-analysis',json={'url':'bad'}).status_code==422
def test_private(): assert client.post('/link-analysis',json={'url':'http://127.0.0.1'}).status_code==400
def test_metadata(): assert client.post('/link-analysis',json={'url':'http://169.254.169.254'}).status_code==400
