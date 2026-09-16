# Security Policy

Nebula may eventually execute generated software. Generated code must always be treated as untrusted input.

## Reporting

Do not disclose exploitable vulnerabilities in a public issue. Use GitHub's private security reporting mechanism.

## Execution requirements

Any execution backend must isolate generated code, enforce CPU and wall-clock limits, restrict filesystem access, make network access explicit, prevent secret exposure, and record failures safely.

Never run arbitrary generated candidates directly on a developer workstation.
