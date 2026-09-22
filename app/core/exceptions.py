from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)

class PlantNotFoundError(Exception):
    def __init__(self, plant_id: str):
        self.plant_id = plant_id

class UnitNotFoundError(Exception):
    def __init__(self, unit_id: str):
        self.unit_id = unit_id

class SimulationError(Exception):
    def __init__(self, message: str):
        self.message = message

class OptimizationError(Exception):
    def __init__(self, message: str):
        self.message = message

def setup_exception_handlers(app: FastAPI):
    @app.exception_handler(PlantNotFoundError)
    async def plant_not_found_handler(request: Request, exc: PlantNotFoundError):
        return JSONResponse(status_code=404, content={"status": "error", "message": f"Plant {exc.plant_id} not found."})

    @app.exception_handler(UnitNotFoundError)
    async def unit_not_found_handler(request: Request, exc: UnitNotFoundError):
        return JSONResponse(status_code=404, content={"status": "error", "message": f"Unit {exc.unit_id} not found."})
        
    @app.exception_handler(SimulationError)
    async def simulation_error_handler(request: Request, exc: SimulationError):
        return JSONResponse(status_code=400, content={"status": "error", "message": f"Simulation failed: {exc.message}"})

    @app.exception_handler(OptimizationError)
    async def optimization_error_handler(request: Request, exc: OptimizationError):
        return JSONResponse(status_code=400, content={"status": "error", "message": f"Optimization failed: {exc.message}"})
