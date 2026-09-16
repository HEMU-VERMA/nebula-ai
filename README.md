# Nebula AI

**Software that evolves instead of being rewritten.**

Nebula is an open-source framework for reproducible AI-guided software evolution.

**Hypothesis → Mutation → Test → Measure → Survive**

## Install

Python 3.12+:

    python -m pip install nebula-ai

The package is alpha; until its first PyPI release, install the repository in development mode:

    python -m pip install -e ".[dev]"

## First evolution run

Nebula keeps the evolution engine provider-agnostic. You supply mutation and fitness policies:

    from nebula import Candidate, Evaluation, EvolutionConfig, EvolutionEngine, candidate_id

    class Mutator:
        def mutate(self, candidate, rng):
            source = candidate.source + "!"
            return Candidate(
                candidate_id=candidate_id(source, candidate.candidate_id),
                source=source,
                parent_id=candidate.candidate_id,
            )

    class Fitness:
        def evaluate(self, candidate):
            return Evaluation(
                candidate_id=candidate.candidate_id,
                score=float(len(candidate.source)),
                passed=True,
                duration_seconds=0.0,
            )

    result = EvolutionEngine(
        EvolutionConfig(population_size=4, generations=10, seed=42),
        Mutator(),
        Fitness(),
    ).run(Candidate(candidate_id=candidate_id("x"), source="x"))

    print(result.best)

## Safety boundary

Nebula does **not** execute generated source code in the core engine. Any future execution backend must provide isolation, resource limits, filesystem restrictions, explicit network policy, and secret isolation.

## Architecture

    Objective → Mutator → Candidate → Isolated Execution → Fitness → Survivor → Lineage

## Quality

    ruff check .
    mypy src
    pytest
    python -m build

CI runs these gates on Python 3.12 and 3.13 and verifies a clean wheel installation.

## Roadmap

- [x] Typed core data model
- [x] Deterministic evolution engine
- [x] Stable candidate identity and lineage
- [x] Strict mypy
- [x] Wheel-install verification
- [ ] Experiment manifest format
- [ ] Production mutation/fidelity interfaces
- [ ] Isolated execution backend
- [ ] Git lineage
- [ ] LLM provider adapters
- [ ] Evolution visualizer
- [ ] Distributed workers

## Security

Generated code is untrusted. See SECURITY.md before implementing an execution backend.

## License

Apache-2.0.
