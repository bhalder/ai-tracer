from abc import ABC, abstractmethod
from typing import Optional
from tracer.models.span import Span

class BaseTracer(ABC):
    @abstractmethod
    def start_span(self, operation_name: str, **kwargs) -> Span:
        pass

    @abstractmethod
    def end_span(self, span_id: str, **kwargs) -> Optional[Span]:
        pass

    @abstractmethod
    def _process_completed_span(self, span: Span):
        pass

