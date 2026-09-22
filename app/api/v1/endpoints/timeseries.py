from fastapi import APIRouter, Query
from app.models.api_models import APIResponse
from app.services.historian_service import historian_service
from typing import List, Dict, Any, Optional

router = APIRouter(prefix="/timeseries")

@router.get("", response_model=APIResponse[List[Dict[str, Any]]])
def get_timeseries(
    plant_id: str,
    tag: str,
    start: Optional[str] = Query(None),
    end: Optional[str] = Query(None),
    interval: Optional[str] = Query("1h")
):
    data = historian_service.get_timeseries(plant_id, tag, start, end, interval)
    return APIResponse(plant_id=plant_id, data=data)
