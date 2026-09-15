from app import app


def test_hello():
    client = app.test_client()

    response = client.get("/api/hello")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "success"


def test_health():
    client = app.test_client()

    response = client.get("/api/health")

    assert response.status_code == 200