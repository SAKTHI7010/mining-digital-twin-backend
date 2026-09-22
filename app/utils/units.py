def tonnes_per_hour_to_kg_per_sec(tph: float) -> float:
    return tph * 1000 / 3600

def kg_per_sec_to_tonnes_per_hour(kg_s: float) -> float:
    return kg_s * 3600 / 1000
