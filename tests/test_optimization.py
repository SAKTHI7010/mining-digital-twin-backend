from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_optimization():
    payload = {
        "plant_id": "PLANT_001",
        "objective": "throughput"
    }
    response = client.post("/api/v1/optimize", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "recommended_setpoints" in data["data"]
