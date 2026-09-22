from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_plants():
    response = client.get("/api/v1/plants")
    assert response.status_code == 200
    assert len(response.json()["data"]) > 0

def test_get_overview():
    response = client.get("/api/v1/overview/PLANT_001")
    assert response.status_code == 200
    assert "kpis" in response.json()["data"]

def test_get_live_state():
    response = client.get("/api/v1/live_state/PLANT_001")
    assert response.status_code == 200
    
def test_get_timeseries():
    response = client.get("/api/v1/timeseries?plant_id=PLANT_001&tag=sag_power_kw")
    assert response.status_code == 200
