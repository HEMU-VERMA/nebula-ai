# Effects & Handlers

Nebula keeps **policy** separate from the evolution engine.

A mutator decides how a candidate changes. A fitness evaluator decides how a candidate is measured. The engine orchestrates the loop but does not decide what an AI provider, benchmark, or execution environment should do.

This separation is intentional: it keeps the core small, testable, and usable without a particular model vendor.

## Future handler boundaries

Planned handlers include:

- model/LLM providers
- benchmark runners
- sandboxed execution
- filesystem and Git operations
- experiment persistence
- distributed workers

Handlers that perform side effects should be explicit. Generated code must be treated as untrusted input and must never inherit application secrets or unrestricted host access.
