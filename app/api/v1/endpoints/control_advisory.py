from fastapi import APIRouter
from app.models.api_models import APIResponse
from app.models.domain import AdvisoryResponse
from app.services.advisory_service import advisory_service

router = APIRouter(prefix="/control_advisory")

@router.get("/{plant_id}", response_model=APIResponse[AdvisoryResponse])
def get_control_advisory(plant_id: str):
    data = advisory_service.get_control_advisory(plant_id)
    return APIResponse(plant_id=plant_id, data=data)
