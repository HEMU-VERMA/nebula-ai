# Core Concepts

## Candidate

A candidate is an immutable piece of implementation plus a stable ID and optional parent ID.

## Mutation

A mutator transforms a candidate into another candidate. Nebula does not require an LLM: mutation can come from templates, search, genetic operators, or any custom algorithm.

## Fitness

A fitness evaluator turns a candidate into a measurable `Evaluation`. This is where domain-specific evidence belongs: benchmark score, test result, latency, cost, correctness, or another metric.

## Selection

The engine evaluates a population and retains the highest-scoring candidate for the next generation. More sophisticated selection strategies can be layered on later without coupling the core to an AI provider.

## Lineage

Every mutated candidate can point to its parent. Stable IDs make it possible to reconstruct how an implementation changed across an experiment.

## Experiment

An experiment combines an objective, configuration, generations, evaluations, and the selected candidate into a serializable manifest.
