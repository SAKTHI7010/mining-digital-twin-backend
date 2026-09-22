from app.models.domain import SimulationRequest, SimulationResult
from app.twin.circuit_models import FullCircuitModel
from app.services.plant_service import plant_service

class SimulationService:
    def __init__(self):
        self.model = FullCircuitModel()
        
    def run_simulation(self, request: SimulationRequest) -> SimulationResult:
        plant = plant_service.get_plant_by_id(request.plant_id)

        # Build inputs dict from flat fields or use provided inputs dict
        inputs = request.inputs or {
            "feed_rate": request.feed_rate or 1100.0,
            "ore_hardness": request.ore_hardness or 14.5,
            "cu_feed_grade": request.cu_feed_grade or 0.85,
            "moisture": request.moisture or 6.5,
            "sag_speed": request.sag_speed or 72.0,
            "ball_charge": request.ball_charge or 32.0,
            "cyclone_pressure": request.cyclone_pressure or 95.0,
            "air_flow_rate": request.air_flow_rate or 1200.0,
            "froth_depth": request.froth_depth or 12.0,
            "collector_dosage": request.collector_dosage or 35.0,
            "frother_dosage": request.frother_dosage or 18.0,
            "flocculant_dosage": request.flocculant_dosage or 28.0,
        }

        results = self.model.simulate(inputs)

        kpis = {
            "throughput_tph": results.get("throughput_tph", 0),
            "recovery_pct": results.get("recovery_pct", 0),
            "conc_grade_pct": results.get("conc_grade_pct", 0),
        }

        return SimulationResult(scenario="base_case", kpis=kpis, outputs=results)

simulation_service = SimulationService()
