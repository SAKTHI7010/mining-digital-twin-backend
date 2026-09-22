from typing import Dict, Any
from app.twin.equipment_models import GrindingMillModel, HydrocycloneModel, FlotationModel
from app.twin.balances import MassBalance

class GrindingCircuit:
    def __init__(self):
        self.sag = GrindingMillModel(wi=14.0)
        self.ball = GrindingMillModel(wi=13.0)
        self.cyclone = HydrocycloneModel()
        
    def simulate(self, fresh_feed: float, f80: float) -> Dict[str, float]:
        # Simplified grinding circuit simulation
        sag_p80 = 2000.0
        sag_power = self.sag.calculate_power(fresh_feed, f80, sag_p80)
        
        # Assume circulating load of 250%
        circulating_load_ratio = 2.5
        ball_feed = fresh_feed * (1 + circulating_load_ratio)
        ball_p80 = 150.0
        ball_power = self.ball.calculate_power(ball_feed, sag_p80, ball_p80)
        
        return {
            "sag_power_kw": sag_power,
            "ball_power_kw": ball_power,
            "p80_um": ball_p80,
            "circulating_load_pct": circulating_load_ratio * 100
        }

class FlotationCircuit:
    def __init__(self):
        self.rougher = FlotationModel(r_max=92.0, k=0.18)
        self.cleaner = FlotationModel(r_max=85.0, k=0.12)
        
    def simulate(self, feed_rate: float, feed_grade: float) -> Dict[str, float]:
        # Rough simplified simulation
        residence_time_r = 15.0
        rec_r = self.rougher.calculate_recovery(residence_time_r)
        
        # Overall estimated
        overall_rec = rec_r * 0.95
        conc_mass = feed_rate * (feed_grade/100.0) * (overall_rec/100.0) / (28.0/100.0)
        tail_mass = feed_rate - conc_mass
        
        return {
            "recovery_pct": overall_rec,
            "conc_grade_pct": 28.0,
            "tail_grade_pct": (feed_rate * feed_grade/100 - conc_mass * 0.28) / max(tail_mass, 1.0) * 100
        }

class FullCircuitModel:
    def __init__(self):
        self.grinding = GrindingCircuit()
        self.flotation = FlotationCircuit()
        
    def simulate(self, inputs: Dict[str, float]) -> Dict[str, float]:
        feed_rate = inputs.get("feed_rate", 1000.0)
        feed_grade = inputs.get("feed_grade", 0.8)
        f80 = inputs.get("f80", 150000.0)
        
        grind_res = self.grinding.simulate(feed_rate, f80)
        float_res = self.flotation.simulate(feed_rate, feed_grade)
        
        result = {**grind_res, **float_res}
        result["throughput_tph"] = feed_rate
        return result
