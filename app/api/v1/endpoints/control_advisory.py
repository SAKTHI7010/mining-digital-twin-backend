from fastapi import APIRouter
from app.models.api_models import APIResponse
from app.models.domain import AdvisoryResponse, AdvisoryRequest
from app.services.advisory_service import advisory_service

router = APIRouter()

@router.post("/control-advisory", response_model=APIResponse[AdvisoryResponse])
def get_control_advisory(request: AdvisoryRequest):
    plant_id = request.plant_id
    data = advisory_service.get_control_advisory(plant_id)
    return APIResponse(plant_id=plant_id, data=data)
