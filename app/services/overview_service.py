from typing import Dict, Any, List
from app.models.domain import KPI
from app.services.plant_service import plant_service
import random

class OverviewService:
    def get_plant_overview(self, plant_id: str) -> Dict[str, Any]:
        plant = plant_service.get_plant_by_id(plant_id)
        
        # Mock live data based on design targets
        throughput = plant.design_throughput_tph * (0.9 + random.random() * 0.15)
        recovery = plant.design_recovery_pct * (0.95 + random.random() * 0.05)
        conc_grade = plant.design_concentrate_grade_pct * (0.95 + random.random() * 0.05)
        
        kpis = [
            KPI(name="Throughput", value=round(throughput, 1), unit="t/h", target=plant.design_throughput_tph),
            KPI(name="Recovery", value=round(recovery, 2), unit="%", target=plant.design_recovery_pct),
            KPI(name="Concentrate Grade", value=round(conc_grade, 2), unit="%", target=plant.design_concentrate_grade_pct),
            KPI(name="Tail Grade", value=round(0.2 + random.random()*0.1, 2), unit="%", target=0.25),
            KPI(name="Energy Intensity", value=round(15.5 + random.random()*2, 2), unit="kWh/t", target=15.0),
            KPI(name="Water Intensity", value=round(0.8 + random.random()*0.2, 2), unit="m3/t", target=0.85),
            KPI(name="Equipment Availability", value=round(94.0 + random.random()*5, 1), unit="%", target=95.0)
        ]
        
        alerts = []
        if throughput < plant.design_throughput_tph * 0.95:
            alerts.append({"message": "Throughput below 95% of target", "level": "warning"})
            
        return {
            "plant_id": plant.plant_id,
            "plant_name": plant.name,
            "kpis": kpis,
            "alerts": alerts
        }

overview_service = OverviewService()
