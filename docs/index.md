# Nebula

## Software that evolves instead of being rewritten.

Nebula turns optimization into an observable loop:

**Objective → Mutate → Measure → Select → Repeat**

### Start here

```bash
pip install nebula-ai
nebula demo
```

### Explore

- [Getting Started](getting-started.md) — install and embed Nebula.
- [Core Concepts](core-concepts.md) — candidates, mutation, fitness, selection, lineage.
- [Effects & Handlers](effects-and-handlers.md) — how integrations stay outside the core.
- [Architecture](architecture.md) — system boundaries and design principles.

### The idea

AI systems are good at generating possibilities. Nebula is built around the harder question: **which possibility survives measurement?**

The core deliberately has no mandatory model provider and does not execute generated code. That keeps experiments reproducible and makes safety boundaries explicit.
