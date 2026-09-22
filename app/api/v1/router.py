from fastapi import APIRouter

from app.api.v1.endpoints import (
    health,
    plants,
    overview,
    live_state,
    timeseries,
    unit_ops,
    simulation,
    optimization,
    control_advisory,
    diagnostics,
    data_quality,
    model_metadata
)

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"])
api_router.include_router(plants.router, tags=["plants"])
api_router.include_router(overview.router, tags=["overview"])
api_router.include_router(live_state.router, tags=["live_state"])
api_router.include_router(timeseries.router, tags=["timeseries"])
api_router.include_router(unit_ops.router, tags=["unit_ops"])
api_router.include_router(simulation.router, tags=["simulation"])
api_router.include_router(optimization.router, tags=["optimization"])
api_router.include_router(control_advisory.router, tags=["control_advisory"])
api_router.include_router(diagnostics.router, tags=["diagnostics"])
api_router.include_router(data_quality.router, tags=["data_quality"])
api_router.include_router(model_metadata.router, tags=["model_metadata"])
