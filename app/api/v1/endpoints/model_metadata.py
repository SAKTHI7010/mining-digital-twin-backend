from fastapi import APIRouter
from app.models.api_models import APIResponse
from app.services.metadata_service import metadata_service
from typing import Dict, Any

router = APIRouter()

@router.get("/model-metadata/{plant_id}", response_model=APIResponse[Dict[str, Any]])
def get_model_metadata(plant_id: str):
    data = metadata_service.get_model_metadata(plant_id)
    return APIResponse(plant_id=plant_id, data=data)
