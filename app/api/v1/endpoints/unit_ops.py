from fastapi import APIRouter
from app.models.api_models import APIResponse
from app.services.plant_service import plant_service
from typing import List, Dict, Any

router = APIRouter(prefix="/unit_ops")

@router.get("/{plant_id}", response_model=APIResponse[List[Dict[str, Any]]])
def get_unit_ops(plant_id: str):
    plant = plant_service.get_plant_by_id(plant_id)
    
    # Mocking unit ops list
    units = []
    for circuit in plant.circuits:
        for unit in circuit.units:
            units.append({
                "unit_id": unit,
                "type": circuit.type,
                "status": "running"
            })
            
    return APIResponse(plant_id=plant_id, data=units)
