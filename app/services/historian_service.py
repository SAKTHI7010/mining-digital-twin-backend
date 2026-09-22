import pandas as pd
import os
from typing import List, Dict, Any

class HistorianService:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(__file__), "..", "data", "sample_timeseries.csv")
        self.df = pd.read_csv(self.data_path)
        
    def get_timeseries(self, plant_id: str, tag: str, start: str, end: str, interval: str) -> List[Dict[str, Any]]:
        # In a real app, this would query a historian DB like OSI PI using start, end, interval
        if tag not in self.df.columns:
            return []
            
        # Mocking filter
        results = []
        for index, row in self.df.iterrows():
            # Adding mock quality flag
            quality = "good"
            if row[tag] == 0:
                quality = "bad"
            
            results.append({
                "timestamp": row["timestamp"],
                "value": row[tag],
                "quality_flag": quality
            })
            
        return results

historian_service = HistorianService()
