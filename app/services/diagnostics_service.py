from app.models.domain import DiagnosticsResponse

class DiagnosticsService:
    def get_diagnostics(self, asset_id: str) -> DiagnosticsResponse:
        return DiagnosticsResponse(
            asset_id=asset_id,
            anomalies=[
                "SAG mill power draw shows high high-frequency noise, check sensor connection.",
                "Cyclone feed pressure slightly drifting downwards."
            ],
            sensor_health=92.5,
            confidence=0.88
        )

diagnostics_service = DiagnosticsService()
