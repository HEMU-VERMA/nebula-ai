# Nebula AI

**Software that evolves instead of being rewritten.**

Nebula is a typed Python framework for reproducible, measurable software evolution. Instead of asking an AI for one answer, Nebula treats implementations as candidates and repeatedly **mutates → evaluates → selects** them.

> Give Nebula an objective. Keep the candidates that actually improve.

## 30-second demo

```bash
python -m pip install -e .
nebula demo
```

You should see generations, candidate counts, fitness scores, and the surviving candidate. The demo is deterministic and does not call an LLM or execute generated code.

## Install

```bash
python -m pip install nebula-ai
```

Python 3.12+ is supported.

## Use it as a library

```python
from nebula import Candidate, Evaluation, EvolutionConfig, EvolutionEngine, candidate_id

class Mutator:
    def mutate(self, candidate, rng):
        source = candidate.source + "!"
        return Candidate(
            candidate_id(source, candidate.candidate_id),
            source,
            candidate.candidate_id,
        )

class Fitness:
    def evaluate(self, candidate):
        return Evaluation(candidate.candidate_id, float(len(candidate.source)), True, 0.0)

result = EvolutionEngine(
    EvolutionConfig(population_size=4, generations=10, seed=42),
    Mutator(),
    Fitness(),
).run(Candidate(candidate_id("x"), "x"))

print(result.best)
```

## Why Nebula exists

Most AI coding tools optimize for **producing code**. Nebula is designed around a different loop: **producing candidates, measuring them, and preserving evidence of why a candidate survived**.

```text
Objective
   ↓
Mutation → Candidate → Evaluation
                 ↑         ↓
                 └── Selection
                      ↓
                   Lineage
                      ↓
                 Experiment
```

The core is provider-agnostic. LLMs, search algorithms, genetic operators, benchmarks, or human-written mutators can plug into the same interfaces.

## Safety by architecture

The core engine does **not** execute generated source code. An execution backend is a separate trust boundary and must provide isolation, resource limits, filesystem restrictions, explicit network policy, and secret isolation.

## Project status

Nebula is alpha. The stable foundation currently includes:

- strict mypy typing
- deterministic seeded evolution
- immutable candidates, evaluations, and generations
- stable candidate IDs and parent lineage
- JSON experiment manifests
- CLI entry point
- CI on Python 3.12 and 3.13
- wheel build and clean-install verification

## Roadmap

- [x] Typed evolution core
- [x] Deterministic evolution
- [x] Experiment manifests
- [x] CLI demo
- [ ] Benchmark suite
- [ ] Real mutation providers
- [ ] LLM adapters
- [ ] Sandboxed execution
- [ ] Git-native lineage
- [ ] Web evolution visualizer
- [ ] Distributed workers

## Documentation

- [Getting Started](docs/getting-started.md)
- [Core Concepts](docs/core-concepts.md)
- [Effects & Handlers](docs/effects-and-handlers.md)
- [Architecture](docs/architecture.md)
- [Security](SECURITY.md)

## Contributing

Small, testable changes are preferred. Every change should pass Ruff, strict mypy, tests, wheel building, and clean installation in CI.

## License

Apache-2.0.
