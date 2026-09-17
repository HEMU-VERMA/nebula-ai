"""Reproducible experiment manifests for Nebula evolution runs."""

from __future__ import annotations

import json
from dataclasses import asdict
from typing import Any

from .engine import EvolutionResult
from .models import EvolutionConfig


class ExperimentManifest:
    """Serializable metadata describing one evolution experiment."""

    def __init__(
        self,
        *,
        objective: str,
        config: EvolutionConfig,
        result: EvolutionResult,
    ) -> None:
        if not objective.strip():
            raise ValueError("objective must not be empty")
        self.objective = objective
        self.config = config
        self.result = result

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-compatible experiment representation."""
        return {
            "schema_version": 1,
            "objective": self.objective,
            "config": asdict(self.config),
            "generations": [
                {
                    "number": generation.number,
                    "candidate_ids": [
                        candidate.candidate_id for candidate in generation.candidates
                    ],
                }
                for generation in self.result.generations
            ],
            "evaluations": [
                {
                    "candidate_id": evaluation.candidate_id,
                    "score": evaluation.score,
                    "passed": evaluation.passed,
                    "duration_seconds": evaluation.duration_seconds,
                }
                for evaluation in self.result.evaluations
            ],
            "best_candidate_id": (
                None if self.result.best is None else self.result.best.candidate_id
            ),
        }

    def to_json(self, *, indent: int = 2) -> str:
        """Serialize the manifest as stable, human-readable JSON."""
        return json.dumps(self.to_dict(), indent=indent, sort_keys=True)
