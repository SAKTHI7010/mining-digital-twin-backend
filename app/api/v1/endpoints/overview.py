from fastapi import APIRouter
from app.models.api_models import APIResponse
from app.services.overview_service import overview_service
from typing import Dict, Any

router = APIRouter()

@router.get("/{plant_id}/overview", response_model=APIResponse[Dict[str, Any]])
def get_overview(plant_id: str):
    data = overview_service.get_plant_overview(plant_id)
    return APIResponse(plant_id=plant_id, data=data)
