from fastapi import APIRouter
from app.models.api_models import APIResponse
from app.models.domain import Plant
from app.services.plant_service import plant_service
from typing import List

router = APIRouter()

@router.get("", response_model=APIResponse[List[Plant]])
def list_plants():
    plants = plant_service.get_all_plants()
    return APIResponse(data=plants)
