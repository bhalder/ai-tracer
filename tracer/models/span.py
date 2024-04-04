from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class Span(BaseModel):
    id: str = Field(default_factory=lambda: uuid.uuid4().hex, description="Unique identifier for the span")
    operation_name: str = Field(..., description="Name of the operation")
    start_time: datetime = Field(default_factory=datetime.utcnow, description="Start time of the operation")
    end_time: Optional[datetime] = Field(None, description="End time of the operation")
    status: str = Field(..., description="Status of the operation (e.g., success, error)")
    inputs: Dict[str, Any] = Field(default_factory=dict, description="Inputs to the operation")
    outputs: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Outputs of the operation")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata related to the operation")

