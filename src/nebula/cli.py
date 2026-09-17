"""Command-line interface for Nebula."""

from __future__ import annotations

import argparse
import random

from .engine import EvolutionEngine, candidate_id
from .models import Candidate, Evaluation, EvolutionConfig


def build_parser() -> argparse.ArgumentParser:
    """Build the Nebula command-line parser."""
    parser = argparse.ArgumentParser(
        prog="nebula",
        description="Reproducible AI-guided software evolution.",
    )
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("demo", help="run a deterministic evolution demo")
    return parser


def _run_demo() -> int:
    class DemoMutator:
        def mutate(self, candidate: Candidate, rng: random.Random) -> Candidate:
            suffix = "!" if rng.random() >= 0.5 else "?"
            source = candidate.source + suffix
            return Candidate(
                candidate_id(source, candidate.candidate_id),
                source,
                candidate.candidate_id,
            )

    class DemoFitness:
        def evaluate(self, candidate: Candidate) -> Evaluation:
            score = float(sum(char == "!" for char in candidate.source))
            return Evaluation(candidate.candidate_id, score, True, 0.0)

    result = EvolutionEngine(
        EvolutionConfig(population_size=4, generations=6, seed=42),
        DemoMutator(),
        DemoFitness(),
    ).run(Candidate(candidate_id(""), ""))
    print("Nebula evolution demo")
    for generation in result.generations:
        candidate_ids = {candidate.candidate_id for candidate in generation.candidates}
        scores = [
            evaluation.score
            for evaluation in result.evaluations
            if evaluation.candidate_id in candidate_ids
        ]
        print(
            f"generation {generation.number}: "
            f"candidates={len(generation.candidates)} best={max(scores):.0f}"
        )
    print(f"survivor: {result.best.source!r}" if result.best else "survivor: none")
    return 0


def main() -> int:
    """Run the command-line interface."""
    args = build_parser().parse_args()
    if args.command == "demo":
        return _run_demo()
    return 0
