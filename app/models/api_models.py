from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, Any
from datetime import datetime, timezone

T = TypeVar('T')

class APIResponse(BaseModel, Generic[T]):
    status: str = "success"
    timestamp: str = datetime.now(timezone.utc).isoformat()
    plant_id: Optional[str] = None
    data: T
    
class PaginatedList(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int
    size: int
