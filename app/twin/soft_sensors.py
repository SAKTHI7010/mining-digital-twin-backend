from typing import Tuple, Dict

class SoftSensorEngine:
    
    @staticmethod
    def estimate_p80(mill_power: float, feed_rate: float, wi: float = 13.0) -> Tuple[float, float]:
        """Estimate particle size P80 from mill power and feed rate using simplified Bond equation"""
        if feed_rate <= 0:
            return 0.0, 0.0
        # W = 10 * Wi * (1/sqrt(P80) - 1/sqrt(F80)) 
        # Simplified inverse calculation for soft sensor
        # Assuming fixed F80 and typical W
        w = mill_power / feed_rate
        p80 = 150.0 * (13.0 / max(w, 1.0))**2 # Rough simplified correlation
        confidence = 0.85
        return p80, confidence

    @staticmethod
    def estimate_percent_solids(density: float, sg_solids: float = 2.7) -> Tuple[float, float]:
        """Estimate % solids from density measurements"""
        if density <= 1.0:
            return 0.0, 0.0
        pct_solids = (sg_solids * (density - 1.0)) / (density * (sg_solids - 1.0)) * 100.0
        confidence = 0.90
        return pct_solids, confidence

    @staticmethod
    def estimate_recovery(conc_grade: float, tail_grade: float, feed_grade: float) -> Tuple[float, float]:
        """Estimate recovery from concentrate/tails/feed grade using two-product formula"""
        if feed_grade <= tail_grade or conc_grade <= tail_grade:
            return 0.0, 0.0
        recovery = (conc_grade * (feed_grade - tail_grade)) / (feed_grade * (conc_grade - tail_grade)) * 100.0
        confidence = 0.88
        return recovery, confidence
