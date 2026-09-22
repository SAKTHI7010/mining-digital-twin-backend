from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_simulation():
    payload = {
        "plant_id": "PLANT_001",
        "inputs": {
            "feed_rate": 1200.0,
            "f80": 150000.0,
            "feed_grade": 0.8
        },
        "duration_hours": 1.0
    }
    response = client.post("/api/v1/simulate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "throughput_tph" in data["data"]["kpis"]
