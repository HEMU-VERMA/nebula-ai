# Nebula AI

**Software that evolves instead of being rewritten.**

Nebula is an open-source framework for reproducible AI-guided software evolution.

**Hypothesis → Mutation → Test → Measure → Survive**

## Install

Python 3.12+ is required.

    python -m pip install nebula-ai

The package is currently alpha. Until its first PyPI release, install the repository in development mode:

    python -m pip install -e ".[dev]"

## Development

    git clone https://github.com/HEMU-VERMA/nebula-ai.git
    cd nebula-ai
    python -m venv .venv
    source .venv/bin/activate
    python -m pip install -e ".[dev]"

Run every quality gate:

    ruff check .
    mypy src
    pytest

## Architecture

    Objective
       |
    Population
       |
    Mutator
       |
    Isolated candidate execution
       |
    Fitness evaluator
       |
    Survivors

The first release deliberately starts with typed domain models and safety-oriented foundations. Future AI providers and arbitrary-code execution belong behind explicit interfaces and isolated execution boundaries.

## Design principles

- Reproducibility over magic: record configuration, seed, lineage and measurements.
- Never execute untrusted mutations directly on the host.
- Fitness is domain-specific: users define measurable objectives.
- Every generated candidate should be testable and traceable.

## Roadmap

- [x] Typed core data model
- [x] Strict mypy configuration
- [x] Reproducible evolution configuration
- [ ] Mutation provider interface
- [ ] Fitness/evaluator interface
- [ ] Isolated execution backend
- [ ] Local deterministic evolution engine
- [ ] Git lineage and experiment manifests
- [ ] LLM provider adapters
- [ ] Web evolution visualizer
- [ ] Distributed workers

## Security

Generated code is untrusted. Any execution backend must provide isolation, resource limits, filesystem restrictions, explicit network policy, timeouts, and secret isolation. See SECURITY.md.

## License

Apache-2.0.
