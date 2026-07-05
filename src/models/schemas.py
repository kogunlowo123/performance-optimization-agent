"""Performance Optimization Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class ProfileRequest(BaseModel):
    """ProfileRequest for Performance Optimization Agent."""
    target: str
    profile_type: str = 'cpu'
    duration_seconds: int = 30


class PerformanceReport(BaseModel):
    """PerformanceReport for Performance Optimization Agent."""
    bottlenecks: list[dict]
    hotspots: list[dict]
    recommendations: list[dict]
    metrics: dict


class BenchmarkResult(BaseModel):
    """BenchmarkResult for Performance Optimization Agent."""
    name: str
    iterations: int
    mean_ms: float
    p95_ms: float
    p99_ms: float
    throughput_rps: float

