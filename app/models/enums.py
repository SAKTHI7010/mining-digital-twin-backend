from enum import Enum

class ProcessStatus(str, Enum):
    RUNNING = "running"
    STOPPED = "stopped"
    MAINTENANCE = "maintenance"
    ALARM = "alarm"

class UnitType(str, Enum):
    MILL = "mill"
    CYCLONE = "cyclone"
    FLOTATION = "flotation"
    THICKENER = "thickener"
    CRUSHER = "crusher"
    OTHER = "other"

class AlertLevel(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"

class OptimizationObjective(str, Enum):
    THROUGHPUT = "throughput"
    RECOVERY = "recovery"
    ENERGY = "energy"
    WATER = "water"
    GRADE = "grade"
    ECONOMIC = "economic"

class OperatingMode(str, Enum):
    MANUAL = "manual"
    AUTO = "auto"
    APC = "apc"

class DataQualityFlag(str, Enum):
    GOOD = "good"
    BAD = "bad"
    STALE = "stale"
    OUTLIER = "outlier"
    MISSING = "missing"
