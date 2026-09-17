# Architecture

Nebula is intentionally layered:

```text
                    Experiment
                        |
                 EvolutionEngine
                  /           \
             Mutator         Fitness
                |                |
            Candidate ------ Evaluation
                |                |
                +---- Lineage --+
```

The core layer has no LLM dependency and no arbitrary code execution. This makes the package useful as a foundation for future model adapters, benchmark runners, and isolated execution backends.

## Design principles

1. **Evidence over generation** — a candidate survives because a measurement says it should.
2. **Reproducibility** — seeded runs and stable candidate identity make experiments inspectable.
3. **Small interfaces** — providers implement protocols rather than becoming part of the core.
4. **Explicit side effects** — execution, filesystem, network, and Git operations belong behind clear boundaries.
5. **Safety by default** — the core engine never executes candidate source.
