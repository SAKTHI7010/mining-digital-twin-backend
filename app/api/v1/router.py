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

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(plants.router, prefix="/plants", tags=["Plants"])
api_router.include_router(overview.router, prefix="/plants", tags=["Overview"])
api_router.include_router(live_state.router, prefix="/plants", tags=["Live State"])
api_router.include_router(timeseries.router, prefix="/plants", tags=["Timeseries"])
api_router.include_router(unit_ops.router, prefix="/plants", tags=["Unit Operations"])
api_router.include_router(simulation.router, tags=["Simulation"])
api_router.include_router(optimization.router, tags=["Optimization"])
api_router.include_router(control_advisory.router, tags=["Control Advisory"])
api_router.include_router(diagnostics.router, tags=["Diagnostics"])
api_router.include_router(data_quality.router, tags=["Data Quality"])
api_router.include_router(model_metadata.router, tags=["Model Metadata"])
