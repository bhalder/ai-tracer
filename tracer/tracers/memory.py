# in_memory_tracer.py
from tracer.tracers.base import BaseTracer
from tracer.models.span import Span
from typing import Optional, List

class InMemoryTracer(BaseTracer):
    def __init__(self):
        self.active_spans: List[Span] = []

    def start_span(self, operation_name: str, **kwargs) -> Span:
        # Implementation specific to in-memory storage
        pass

    def end_span(self, span_id: str, **kwargs) -> Optional[Span]:
        # Implementation specific to in-memory storage
        pass

    def _process_completed_span(self, span: Span):
        # In-memory specific processing, e.g., logging or adding to an in-memory DB
        pass

