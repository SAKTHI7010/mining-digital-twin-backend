from app.models.domain import DataQualityResponse

class DataQualityService:
    def get_data_quality(self, plant_id: str) -> DataQualityResponse:
        return DataQualityResponse(
            overall_quality=95.2,
            tag_reports={
                "sag_power_kw": {"availability": 99.9, "missing": 0.1, "outliers": 0},
                "p80_um": {"availability": 95.0, "missing": 2.0, "outliers": 3.0}
            }
        )

data_quality_service = DataQualityService()
