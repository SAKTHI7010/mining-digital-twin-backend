from typing import Dict, Any
from app.core.config import get_settings
from datetime import datetime, timezone

class MetadataService:
    def get_model_metadata(self, plant_id: str) -> Dict[str, Any]:
        settings = get_settings()
        return {
            "model_version": settings.MODEL_VERSION,
            "last_updated": datetime.now(timezone.utc).isoformat(),
            "assumptions": [
                "Steady state conditions assumed for base balances",
                "First order kinetics for flotation",
                "Constant ore hardness (Wi=13.5)"
            ]
        }

metadata_service = MetadataService()
