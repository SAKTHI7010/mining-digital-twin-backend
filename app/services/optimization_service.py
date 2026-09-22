import numpy as np
from scipy.optimize import minimize
from app.models.domain import OptimizationRequest, OptimizationResult
from app.twin.circuit_models import FullCircuitModel
from app.services.plant_service import plant_service

class OptimizationService:
    def __init__(self):
        self.model = FullCircuitModel()
        
    def run_optimization(self, request: OptimizationRequest) -> OptimizationResult:
        plant = plant_service.get_plant_by_id(request.plant_id)
        
        # Simplified optimization problem
        # Decision variables: feed_rate (800-1400), f80 (100000-200000)
        def objective(x):
            inputs = {"feed_rate": x[0], "f80": x[1], "feed_grade": 0.8}
            res = self.model.simulate(inputs)
            
            if request.objective == "throughput":
                return -res.get("throughput_tph", 0)
            elif request.objective == "recovery":
                return -res.get("recovery_pct", 0)
            else:
                return -res.get("recovery_pct", 0) * x[0] # proxy for economic
                
        bounds = [(800, 1400), (100000, 200000)]
        x0 = [1000, 150000]
        
        res = minimize(objective, x0, bounds=bounds, method='SLSQP')
        
        opt_inputs = {"feed_rate": res.x[0], "f80": res.x[1], "feed_grade": 0.8}
        opt_res = self.model.simulate(opt_inputs)
        
        return OptimizationResult(
            recommended_setpoints={
                "feed_rate_tph": round(res.x[0], 1),
                "f80_um": round(res.x[1], 1)
            },
            expected_kpi_impact={
                "throughput_tph": round(opt_res.get("throughput_tph", 0), 1),
                "recovery_pct": round(opt_res.get("recovery_pct", 0), 2)
            },
            confidence_score=0.85
        )

optimization_service = OptimizationService()
