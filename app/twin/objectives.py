from typing import Dict

class ObjectiveFunction:
    
    @staticmethod
    def calculate_economic_value(throughput: float, recovery: float, feed_grade: float, 
                               conc_grade: float, power_kw: float, 
                               cu_price: float = 8000.0, power_cost: float = 0.1) -> float:
        """Calculate simplified hourly economic value (revenue - cost)"""
        # Cu produced in tonnes per hour
        cu_tonnes = throughput * (feed_grade / 100.0) * (recovery / 100.0)
        revenue = cu_tonnes * cu_price
        
        cost = power_kw * power_cost
        
        return revenue - cost

    @staticmethod
    def weighted_sum(kpis: Dict[str, float], weights: Dict[str, float]) -> float:
        """Multi-objective weighted sum"""
        score = 0.0
        for k, w in weights.items():
            score += kpis.get(k, 0.0) * w
        return score
