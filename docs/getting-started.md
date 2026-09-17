# Getting Started

## Install from PyPI

```bash
python -m pip install nebula-ai
```

Nebula currently requires Python 3.12 or newer.

## Run the built-in demo

```bash
nebula demo
```

The demo intentionally has no network dependency and does not execute generated code. It demonstrates the evolution loop with a deterministic local mutator and fitness function.

## Embed Nebula

Nebula is a library first. Implement two small policies:

1. **Mutator** — creates a candidate from a parent.
2. **Fitness** — measures the candidate.

Then pass them to `EvolutionEngine`.

```python
from nebula import Candidate, Evaluation, EvolutionConfig, EvolutionEngine, candidate_id

class Mutator:
    def mutate(self, candidate, rng):
        source = candidate.source + "!"
        return Candidate(candidate_id(source, candidate.candidate_id), source, candidate.candidate_id)

class Fitness:
    def evaluate(self, candidate):
        return Evaluation(candidate.candidate_id, float(len(candidate.source)), True, 0.0)

result = EvolutionEngine(
    EvolutionConfig(population_size=8, generations=20, seed=42),
    Mutator(),
    Fitness(),
).run(Candidate(candidate_id("seed"), "seed"))
```

## Reproducibility

Use a fixed `seed` for deterministic mutation policies. Candidate IDs include source content and parent identity, which makes lineage inspectable.

## Development

```bash
git clone https://github.com/HEMU-VERMA/nebula-ai.git
cd nebula-ai
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
ruff check .
mypy src
pytest
python -m build
```
