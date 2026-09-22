from typing import Dict, Any
from app.models.enums import DataQualityFlag

class PreprocessingService:
    
    def preprocess_inputs(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validates, normalizes units, flags outliers"""
        processed = {}
        for k, v in raw_data.items():
            # Basic validation
            if v is None:
                continue
                
            val = float(v)
            quality = DataQualityFlag.GOOD
            
            # Simple outlier check
            if val < 0:
                quality = DataQualityFlag.BAD
                val = 0.0
                
            processed[k] = {
                "value": val,
                "quality": quality.value
            }
        return processed

preprocessing_service = PreprocessingService()
