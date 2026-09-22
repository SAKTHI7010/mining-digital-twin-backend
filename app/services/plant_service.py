import json
import os
from typing import List
from app.models.domain import Plant
from app.core.exceptions import PlantNotFoundError

class PlantService:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(__file__), "..", "data", "demo_plant.json")
        self._plants = self._load_data()
        
    def _load_data(self) -> List[Plant]:
        with open(self.data_path, 'r') as f:
            data = json.load(f)
            return [Plant(**p) for p in data.get("plants", [])]
            
    def get_all_plants(self) -> List[Plant]:
        return self._plants
        
    def get_plant_by_id(self, plant_id: str) -> Plant:
        for p in self._plants:
            if p.plant_id == plant_id:
                return p
        raise PlantNotFoundError(plant_id=plant_id)
        
plant_service = PlantService()
