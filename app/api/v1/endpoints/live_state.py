from fastapi import APIRouter
from app.models.api_models import APIResponse
from app.services.plant_service import plant_service
from typing import Dict, Any

router = APIRouter(prefix="/live_state")

@router.get("/{plant_id}", response_model=APIResponse[Dict[str, Any]])
def get_live_state(plant_id: str):
    plant = plant_service.get_plant_by_id(plant_id)
    
    # Mock live state data
    live_state = {
        "sag_power_kw": 9520.5,
        "ball_power_kw": 11050.2,
        "p80_um": 152.4,
        "recovery_pct": 88.3
    }
    
    return APIResponse(plant_id=plant_id, data=live_state)
