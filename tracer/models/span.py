from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime
import uuid
from enum import Enum, auto

class SpanOperation(Enum):
    LLM_INTERACTION = auto()
    DATA_RETRIEVAL = auto()
    TOOL_USAGE = auto()
    USER_AUTHENTICATION = auto()
    API_REQUEST = auto()
    BACKGROUND_TASK = auto()
    CUSTOM_OPERATION = auto()

class SpanStatus(Enum):
    SUCCESS = auto()
    ERROR = auto()
    PENDING = auto()
    CANCELLED = auto()


class Span(BaseModel):
    id: str = Field(default_factory=lambda: uuid.uuid4().hex, description="Unique identifier for the span")
    operation_name: SpanOperation = Field(..., description="Type of operation")
    start_time: datetime = Field(default_factory=datetime.utcnow, description="Start time of the operation")
    end_time: Optional[datetime] = Field(None, description="End time of the operation")
    status: SpanStatus = Field(SpanStatus.PENDING, description="Status of the operation")
    inputs: Dict[str, Any] = Field(default_factory=dict, description="Inputs to the operation")
    outputs: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Outputs of the operation")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata related to the operation")

