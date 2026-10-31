from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Student Pass Prediction System" in response.data


def test_prediction():
    client = app.test_client()
    response = client.get("/predict?hours=6")

    assert response.status_code == 200
    assert response.json["prediction"] == "Pass"


def test_invalid_input():
    client = app.test_client()
    response = client.get("/predict?hours=30")

    assert response.status_code == 400


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"