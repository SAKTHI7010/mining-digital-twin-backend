from typing import Dict, List, Tuple

class OperatingConstraints:
    def __init__(self):
        self.bounds = {
            "sag_power_kw": (0, 12000),
            "ball_power_kw": (0, 14000),
            "p80_um": (100, 200),
            "recovery_pct": (0, 100),
            "throughput_tph": (0, 1500)
        }
        
    def check_constraints(self, state: Dict[str, float]) -> List[Dict[str, str]]:
        violations = []
        for var, (min_val, max_val) in self.bounds.items():
            if var in state:
                val = state[var]
                if val < min_val:
                    violations.append({"variable": var, "issue": f"Below minimum ({val} < {min_val})", "severity": "high"})
                elif val > max_val:
                    violations.append({"variable": var, "issue": f"Above maximum ({val} > {max_val})", "severity": "high"})
        return violations
