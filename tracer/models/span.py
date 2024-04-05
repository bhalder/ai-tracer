import uuid
from enum import Enum, auto
from typing import List, Optional, Union

from pydantic import BaseModel, Field, root_validator


# BaseModel for KeyValue pairs
class KeyValue(BaseModel):
    key: str = Field(
        ..., regex=r"^[a-zA-Z0-9_.]*$", description="Dot format key"
    )  # noqa
    value: Union[
        int, float, str, List["KeyValue"]
    ]  # Forward reference for recursive definition

    @root_validator
    def validate_value(cls, values):
        # Validate value types
        value = values.get("value")
        if isinstance(value, list):
            # If value is a list of KeyValue, recursively validate each item
            for item in value:
                if not isinstance(item, KeyValue):
                    raise ValueError("List value must contain KeyValue.")
        elif not isinstance(value, (int, float, str)):
            raise ValueError(
                "Value must be one of int, float, str, or list of KeyValue."
            )
        return values


# BaseModel for Event
class Event(BaseModel):
    time_unix_nano: int
    name: str
    attributes: List[KeyValue]
    dropped_attributes_count: int


# Enum class for Status code
class StatusCode(Enum):
    STATUS_CODE_UNSET = auto()
    STATUS_CODE_OK = auto()
    STATUS_CODE_ERROR = auto()


# BaseModel for Status
class Status(BaseModel):
    message: Optional[str]
    code: StatusCode


# Enum class for Span Kind
class SpanKind(Enum):
    SPAN_KIND_UNSPECIFIED = auto()
    SPAN_KIND_INTERNAL = auto()
    SPAN_KIND_SERVER = auto()
    SPAN_KIND_CLIENT = auto()
    SPAN_KIND_PRODUCER = auto()
    SPAN_KIND_CONSUMER = auto()
    SPAN_KIND_TOOL = auto()
    SPAN_KIND_CHAIN = auto()
    SPAN_KIND_LLM = auto()
    SPAN_KIND_RETRIEVER = auto()
    SPAN_KIND_EMBEDDING = auto()
    SPAN_KIND_AGENT = auto()
    SPAN_KIND_RERANKER = auto()


# BaseModel for Span
class Span(BaseModel):
    trace_id: uuid.UUID
    span_id: uuid.UUID
    trace_state: Optional[str]
    parent_span_id: uuid.UUID
    flags: int
    name: str
    kind: SpanKind
    start_time_unix_nano: int
    end_time_unix_nano: int
    attributes: List[KeyValue]
    dropped_attributes_count: int
    events: List[Event]
    dropped_events_count: int
    status: Optional[Status]

    @root_validator
    def validate_end_time_greater_than_start_time(cls, values):
        # Validate end time is greater than or equal to start time
        if (
            values.get("start_time_unix_nano") is not None
            and values.get("end_time_unix_nano") is not None
        ):
            if values["end_time_unix_nano"] < values["start_time_unix_nano"]:
                raise ValueError(
                    "End time must be greater than or equal to start time."
                )
        return values


# Class to hold constants for AI Span attributes
class AISpanAttributes:
    OUTPUT_VALUE = "output.value"
    OUTPUT_MIME_TYPE = "output.mime_type"
    INPUT_VALUE = "input.value"
    INPUT_MIME_TYPE = "input.mime_type"
    EMBEDDING_EMBEDDINGS = "embedding.embeddings"
    EMBEDDING_MODEL_NAME = "embedding.model_name"


# Class to hold constants for AI Message attributes
class AIMessageAttributes:
    MESSAGE_ROLE = "message.role"
    MESSAGE_CONTENT = "message.content"
    MESSAGE_NAME = "message.name"
    MESSAGE_TOOL_CALLS = "message.tool_calls"
    MESSAGE_FUNCTION_CALL_NAME = "message.function_call_name"
    MESSAGE_FUNCTION_CALL_ARGUMENTS_JSON = (
        "message.function_call_arguments_json"  # noqa
    )


# Class to hold constants for Document attributes
class DocumentAttributes:
    DOCUMENT_ID = "document.id"
    DOCUMENT_SCORE = "document.score"
    DOCUMENT_CONTENT = "document.content"
    DOCUMENT_METADATA = "document.metadata"


# Class to hold constants for Reranker attributes
class RerankerAttributes:
    RERANKER_INPUT_DOCUMENTS = "reranker.input_documents"
    RERANKER_OUTPUT_DOCUMENTS = "reranker.output_documents"
    RERANKER_QUERY = "reranker.query"
    RERANKER_MODEL_NAME = "reranker.model_name"
    RERANKER_TOP_K = "reranker.top_k"


# Class to hold constants for Embedding attributes
class EmbeddingAttributes:
    EMBEDDING_TEXT = "embedding.text"
    EMBEDDING_VECTOR = "embedding.vector"


# Class to hold constants for Tool Call attributes
class ToolCallAttributes:
    TOOL_CALL_FUNCTION_NAME = "tool_call.function.name"
    TOOL_CALL_FUNCTION_ARGUMENTS_JSON = "tool_call.function.arguments"


# Enum class for MimeType values
class MimeTypeValues(Enum):
    TEXT = "text/plain"
    JSON = "application/json"
