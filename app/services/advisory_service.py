from app.models.domain import AdvisoryResponse

class AdvisoryService:
    def get_control_advisory(self, plant_id: str) -> AdvisoryResponse:
        return AdvisoryResponse(
            apc_readiness=85.0,
            suggested_actions=[
                "Increase SAG mill feed rate by 50 t/h to approach maximum power constraint.",
                "Decrease cyclone feed density to improve P80 target.",
                "Increase rougher frother dosage slightly to compensate for lower recovery."
            ]
        )

advisory_service = AdvisoryService()
