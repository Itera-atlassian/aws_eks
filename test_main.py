import pytest
from fastapi.testclient import TestClient
from main import app

# Create a TestClient instance for your FastAPI app
client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "DOCTYPE html" in response.text

def test_healthz_endpoint():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_sumatoria_endpoint():
    # Verifica que "sumatoria" sea igual a 15
    response = client.get("/sumatoria/5", headers={"materia": "calculo"})
    assert response.status_code == 200
    assert response.json().get("sumatoria") == 15

    # Verifica que "sumatoria" sea igual a 15
    response = client.get("/sumatoria/5", headers={"materia": "calculo"})
    assert response.status_code == 200
    assert response.json().get("sumatoria") == 16

    # Test an invalid request (negative number)
    response = client.get("/sumatoria/-5", headers={"materia": "calculo"})
    assert response.status_code == 200
    assert response.json() == {"error": "El número debe ser no negativo"}

    # Test an invalid request (wrong 'materia' header)
    response = client.get("/sumatoria/5", headers={"materia": "invalid"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Header 'materia' must be 'calculo'"}

if __name__ == "__main__":
    pytest.main()
