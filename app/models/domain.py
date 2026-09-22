from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from app.models.enums import UnitType, OptimizationObjective, DataQualityFlag, AlertLevel

class Sensor(BaseModel):
    tag: str
    value: float
    quality: DataQualityFlag

class UnitOperation(BaseModel):
    unit_id: str
    type: UnitType
    sensors: List[Sensor] = []

class Circuit(BaseModel):
    circuit_id: str
    type: str
    units: List[str]

class Plant(BaseModel):
    plant_id: str
    name: str
    location: str
    ore_type: str
    design_throughput_tph: float
    circuits: List[Circuit]
    design_recovery_pct: float
    design_concentrate_grade_pct: float

class KPI(BaseModel):
    name: str
    value: float
    unit: str
    target: Optional[float] = None

class SimulationRequest(BaseModel):
    plant_id: str
    inputs: Dict[str, float]
    duration_hours: float = 1.0

class SimulationResult(BaseModel):
    scenario: str
    kpis: Dict[str, float]
    outputs: Dict[str, float]

class OptimizationRequest(BaseModel):
    plant_id: str
    objective: OptimizationObjective
    constraints: Optional[Dict[str, Dict[str, float]]] = None

class OptimizationResult(BaseModel):
    recommended_setpoints: Dict[str, float]
    expected_kpi_impact: Dict[str, float]
    confidence_score: float

class AdvisoryRequest(BaseModel):
    plant_id: str

class AdvisoryResponse(BaseModel):
    apc_readiness: float
    suggested_actions: List[str]

class DiagnosticsResponse(BaseModel):
    asset_id: str
    anomalies: List[str]
    sensor_health: float
    confidence: float

class DataQualityResponse(BaseModel):
    overall_quality: float
    tag_reports: Dict[str, Dict[str, Any]]
