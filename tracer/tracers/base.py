import datetime
from typing import Optional

from tracer.models.span import Span, SpanStatus


class BaseTracer:
    def start_span(self, operation_name: str, inputs: dict) -> Span:
        # Implementation specific to in-memory storage
        span = Span(operation_name=operation_name, inputs=inputs)
        self.active_spans.append(span)

    def end_span(
        self, span_id: str, status: SpanStatus, outputs: dict = {}
    ) -> Optional[Span]:
        # Implementation specific to in-memory storage

        for span in self.active_spans:
            if span.id == span_id:
                span.end_time = datetime.utcnow()
                span.status = status
                span.outputs = outputs
                self.process_completed_span(span)
                self.active_spans.remove(span)
                return span

        return None

    def process_completed_span(self, span: Span):
        raise NotImplementedError("Subclasses must implement this method")
