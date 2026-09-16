"""Core immutable data models for Nebula."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Final

SCHEMA_VERSION: Final[int] = 1


@dataclass(frozen=True, slots=True)
class Candidate:
    """A candidate implementation identified by stable content."""

    candidate_id: str
    source: str
    parent_id: str | None = None

    def __post_init__(self) -> None:
        if not self.candidate_id.strip():
            raise ValueError("candidate_id must not be empty")


@dataclass(frozen=True, slots=True)
class Evaluation:
    """A reproducible fitness measurement."""

    candidate_id: str
    score: float
    passed: bool
    duration_seconds: float
    measured_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self) -> None:
        if not self.candidate_id.strip():
            raise ValueError("candidate_id must not be empty")
        if self.duration_seconds < 0:
            raise ValueError("duration_seconds must be non-negative")


@dataclass(frozen=True, slots=True)
class Generation:
    """A population snapshot from one evolution step."""

    number: int
    candidates: tuple[Candidate, ...]
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    schema_version: int = SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.number < 0:
            raise ValueError("generation number must be non-negative")
        if self.schema_version != SCHEMA_VERSION:
            raise ValueError("unsupported schema version")


@dataclass(frozen=True, slots=True)
class EvolutionConfig:
    """Safety and reproducibility limits for an evolution run."""

    population_size: int = 8
    generations: int = 10
    timeout_seconds: float = 30.0
    seed: int = 0

    def __post_init__(self) -> None:
        if self.population_size < 1:
            raise ValueError("population_size must be at least 1")
        if self.generations < 1:
            raise ValueError("generations must be at least 1")
        if self.timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")
