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
    feed_rate: Optional[float] = 1100.0
    ore_hardness: Optional[float] = 14.5
    cu_feed_grade: Optional[float] = 0.85
    moisture: Optional[float] = 6.5
    sag_speed: Optional[float] = 72.0
    ball_charge: Optional[float] = 32.0
    cyclone_pressure: Optional[float] = 95.0
    air_flow_rate: Optional[float] = 1200.0
    froth_depth: Optional[float] = 12.0
    collector_dosage: Optional[float] = 35.0
    frother_dosage: Optional[float] = 18.0
    flocculant_dosage: Optional[float] = 28.0
    duration_hours: float = 1.0
    inputs: Optional[Dict[str, float]] = None

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
