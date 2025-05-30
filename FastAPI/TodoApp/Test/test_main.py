from fastapi.testclient import TestClient
from TodoApp.main import app
from fastapi import status

client = TestClient(app)

def test_return_health_check():
    endpoint_response = client.get('/healthy')
    assert endpoint_response.status_code == status.HTTP_200_OK
    assert endpoint_response.json() == {'status': 'Healthy'}