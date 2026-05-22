from fastapi.testclient import TestClient
from fast_api_zero.app import app

client = TestClient(app)


def test_html():
    response = client.get("/html")

    assert response.status_code == 200
    assert "<h1>Olá mundo</h1>" in response.text