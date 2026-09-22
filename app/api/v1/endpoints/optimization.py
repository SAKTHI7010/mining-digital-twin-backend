from fastapi import APIRouter
from app.models.api_models import APIResponse
from app.models.domain import OptimizationRequest, OptimizationResult
from app.services.optimization_service import optimization_service
from app.core.exceptions import OptimizationError

router = APIRouter(prefix="/optimize")

@router.post("", response_model=APIResponse[OptimizationResult])
def run_optimization(request: OptimizationRequest):
    try:
        result = optimization_service.run_optimization(request)
        return APIResponse(plant_id=request.plant_id, data=result)
    except Exception as e:
        raise OptimizationError(str(e))
