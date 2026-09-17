"""Deterministic, provider-agnostic evolution engine."""

from __future__ import annotations

import hashlib
import random
from dataclasses import dataclass
from typing import Protocol

from .models import Candidate, Evaluation, EvolutionConfig, Generation


class Mutator(Protocol):
    """Create a candidate from an existing candidate."""

    def mutate(self, candidate: Candidate, rng: random.Random) -> Candidate:
        """Return one mutated candidate."""


class Fitness(Protocol):
    """Measure a candidate."""

    def evaluate(self, candidate: Candidate) -> Evaluation:
        """Return a fitness measurement."""


@dataclass(frozen=True, slots=True)
class EvolutionResult:
    """Complete result of a deterministic evolution run."""

    generations: tuple[Generation, ...]
    evaluations: tuple[Evaluation, ...]
    best: Candidate | None


def candidate_id(source: str, parent_id: str | None = None) -> str:
    """Return a stable identifier derived from candidate content and lineage."""
    payload = f"{parent_id or ''}\0{source}".encode()
    return hashlib.sha256(payload).hexdigest()[:16]


class IdentityMutator:
    """Reference mutator that preserves source while creating a new lineage node."""

    def mutate(self, candidate: Candidate, rng: random.Random) -> Candidate:
        """Return an unchanged candidate with deterministic identity."""
        del rng
        return Candidate(
            candidate_id=candidate_id(candidate.source, candidate.candidate_id),
            source=candidate.source,
            parent_id=candidate.candidate_id,
        )


class EvolutionEngine:
    """Run deterministic selection and mutation with user-supplied components."""

    def __init__(
        self,
        config: EvolutionConfig,
        mutator: Mutator,
        fitness: Fitness,
    ) -> None:
        self.config = config
        self.mutator = mutator
        self.fitness = fitness

    def run(self, initial: Candidate) -> EvolutionResult:
        """Evolve an initial candidate and retain the highest-scoring candidate."""
        rng = random.Random(self.config.seed)
        population: tuple[Candidate, ...] = (initial,)
        generations: list[Generation] = []
        evaluations: list[Evaluation] = []

        for number in range(self.config.generations):
            generations.append(Generation(number=number, candidates=population))
            current = tuple(self.fitness.evaluate(item) for item in population)
            evaluations.extend(current)
            survivor, _ = max(
                zip(population, current, strict=True),
                key=lambda pair: pair[1].score,
            )
            if number == self.config.generations - 1:
                break

            next_population = [survivor]
            while len(next_population) < self.config.population_size:
                next_population.append(self.mutator.mutate(survivor, rng))
            population = tuple(next_population)

        all_candidates = (
            item for generation in generations for item in generation.candidates
        )
        best = max(
            zip(all_candidates, evaluations, strict=True),
            key=lambda pair: pair[1].score,
            default=None,
        )
        return EvolutionResult(
            generations=tuple(generations),
            evaluations=tuple(evaluations),
            best=None if best is None else best[0],
        )
