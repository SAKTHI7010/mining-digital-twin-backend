from fastapi import APIRouter, HTTPException
from app.models.api_models import APIResponse
from app.models.domain import SimulationRequest, SimulationResult
from app.services.simulation_service import simulation_service
from app.core.exceptions import SimulationError

router = APIRouter(prefix="/simulate")

@router.post("", response_model=APIResponse[SimulationResult])
def run_simulation(request: SimulationRequest):
    try:
        result = simulation_service.run_simulation(request)
        return APIResponse(plant_id=request.plant_id, data=result)
    except Exception as e:
        raise SimulationError(str(e))
