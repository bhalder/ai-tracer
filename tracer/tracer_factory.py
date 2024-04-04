from tracer.tracers.base import BaseTracer
from tracer.tracers.duckdb import DuckDBTracer
from tracer.tracers.memory import InMemoryTracer

class TracerFactory:
    @staticmethod
    def create_tracer(tracer_type: str, **kwargs) -> BaseTracer:
        if tracer_type == "duck-db":
            return DuckDBTracer(**kwargs)
        elif tracer_type == "in-memory":
            return InMemoryTracer(**kwargs)
        else:
            raise ValueError(f"Tracer type {tracer_type} is not supported.")

