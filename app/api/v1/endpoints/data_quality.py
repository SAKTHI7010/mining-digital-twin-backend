from fastapi import APIRouter
from app.models.api_models import APIResponse
from app.models.domain import DataQualityResponse
from app.services.data_quality_service import data_quality_service

router = APIRouter(prefix="/data_quality")

@router.get("/{plant_id}", response_model=APIResponse[DataQualityResponse])
def get_data_quality(plant_id: str):
    data = data_quality_service.get_data_quality(plant_id)
    return APIResponse(plant_id=plant_id, data=data)
