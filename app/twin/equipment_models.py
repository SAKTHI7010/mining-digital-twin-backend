import math
from typing import Dict, Any

class GrindingMillModel:
    def __init__(self, wi: float = 13.5):
        self.wi = wi
        
    def calculate_power(self, feed_rate: float, f80: float, p80: float) -> float:
        """Bond work index equation for power draw"""
        if p80 <= 0 or f80 <= 0:
            return 0.0
        w = 10 * self.wi * (1/math.sqrt(p80) - 1/math.sqrt(f80))
        return w * feed_rate

class HydrocycloneModel:
    def calculate_d50(self, feed_density: float, pressure: float) -> float:
        """Empirical cut size calculation"""
        return 50.0 + (feed_density - 60.0) * 2.0 - (pressure - 100.0) * 0.1

class FlotationModel:
    def __init__(self, r_max: float = 95.0, k: float = 0.15):
        self.r_max = r_max
        self.k = k
        
    def calculate_recovery(self, residence_time: float) -> float:
        """First-order kinetics R = Rmax * (1 - exp(-k*t))"""
        return self.r_max * (1 - math.exp(-self.k * residence_time))

class ThickenerModel:
    def calculate_underflow(self, feed_rate: float, feed_solids: float, settling_rate: float) -> float:
        """Simplified underflow density estimation"""
        return min(75.0, feed_solids + settling_rate * 5.0)

class CrusherModel:
    def calculate_power(self, throughput: float, reduction_ratio: float) -> float:
        """Crusher power consumption"""
        return throughput * reduction_ratio * 0.5
