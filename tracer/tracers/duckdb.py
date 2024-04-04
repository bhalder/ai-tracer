# in_memory_tracer.py
from tracer.tracers.base import BaseTracer
from tracer.models.span import Span
from typing import List

class DuckDBTracer(BaseTracer):
    def __init__(self):
        self.active_spans: List[Span] = []

    def process_completed_span(self, span: Span):
        # In-memory specific processing, e.g., logging or adding to an in-memory DB
        pass

