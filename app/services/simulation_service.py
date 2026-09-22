from app.models.domain import SimulationRequest, SimulationResult
from app.twin.circuit_models import FullCircuitModel
from app.services.plant_service import plant_service

class SimulationService:
    def __init__(self):
        self.model = FullCircuitModel()
        
    def run_simulation(self, request: SimulationRequest) -> SimulationResult:
        # Validate plant exists
        plant = plant_service.get_plant_by_id(request.plant_id)
        
        # Run model
        results = self.model.simulate(request.inputs)
        
        kpis = {
            "throughput_tph": results.get("throughput_tph", 0),
            "recovery_pct": results.get("recovery_pct", 0),
            "conc_grade_pct": results.get("conc_grade_pct", 0)
        }
        
        return SimulationResult(
            scenario="base_case",
            kpis=kpis,
            outputs=results
        )

simulation_service = SimulationService()
