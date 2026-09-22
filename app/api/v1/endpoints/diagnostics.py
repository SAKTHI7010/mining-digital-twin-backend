from fastapi import APIRouter
from app.models.api_models import APIResponse
from app.models.domain import DiagnosticsResponse
from app.services.diagnostics_service import diagnostics_service

router = APIRouter(prefix="/diagnostics")

@router.get("/{asset_id}", response_model=APIResponse[DiagnosticsResponse])
def get_diagnostics(asset_id: str):
    data = diagnostics_service.get_diagnostics(asset_id)
    return APIResponse(data=data)
