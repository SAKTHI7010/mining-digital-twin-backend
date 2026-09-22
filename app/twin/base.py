from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseDigitalTwin(ABC):
    
    @abstractmethod
    def compute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        pass
        
    @abstractmethod
    def validate_inputs(self, inputs: Dict[str, Any]) -> bool:
        pass
        
    @abstractmethod
    def get_confidence(self) -> float:
        pass
