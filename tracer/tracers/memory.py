# in_memory_tracer.py
from typing import Dict, List, Optional

from tracer.models.span import Span
from tracer.tracers.base import BaseTracer


class InMemorySpanDB:
    def __init__(self):
        self.spans: Dict[str, Span] = {}

    def create_span(self, span: Span) -> None:
        """Adds a new Span to the database."""
        self.spans[span.id] = span

    def delete_span(self, span_id: str) -> bool:
        """Deletes a Span from the database by its ID."""
        if span_id in self.spans:
            del self.spans[span_id]
            return True
        return False

    def get_span(self, span_id: str) -> Optional[Span]:
        """Retrieves a Span by its ID."""
        return self.spans.get(span_id)

    def query_spans(self, **criteria) -> List[Span]:
        """Queries Spans based on various criteria (e.g., status, operation_name)."""
        results = []
        for span in self.spans.values():
            if all(getattr(span, key) == value for key, value in criteria.items()):
                results.append(span)
        return results


_db = InMemorySpanDB()


class InMemoryTracer(BaseTracer):
    def __init__(self):
        self.active_spans: List[Span] = []

    def process_completed_span(self, span: Span):
        _db.create_span(span)
        pass
