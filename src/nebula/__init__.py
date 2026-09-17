"""Nebula: reproducible AI-guided software evolution."""

from .engine import (
    EvolutionEngine,
    EvolutionResult,
    Fitness,
    IdentityMutator,
    Mutator,
    candidate_id,
)
from .experiment import ExperimentManifest
from .models import Candidate, Evaluation, EvolutionConfig, Generation

__all__ = [
    "Candidate",
    "Evaluation",
    "EvolutionConfig",
    "EvolutionEngine",
    "EvolutionResult",
    "ExperimentManifest",
    "Fitness",
    "Generation",
    "IdentityMutator",
    "Mutator",
    "candidate_id",
]
__version__ = "0.1.0"
