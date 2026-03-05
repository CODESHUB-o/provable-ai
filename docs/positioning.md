# Provable AI — Category Positioning

## Category

Provable AI is infrastructure for regulated AI decisions.

It converts AI loan and risk decisions into cryptographically signed proof artifacts that regulators, auditors, and enterprise clients can independently verify.

---

## Problem

Most AI fintech systems rely on logs and internal databases to explain decisions.

Those records are mutable and not independently verifiable.

When regulators, auditors, or enterprise clients ask for proof of how a specific AI decision was made, teams must manually reconstruct decision history from logs and database records.

This process is slow, fragile, and often not defensible.

---

## Solution

Provable AI wraps around existing AI decision pipelines and enforces deterministic execution and governance validation.

Every decision becomes:

- Version-locked (model + policy)
- Canonically hashed
- Cryptographically signed
- Linked to a deterministic state transition
- Exportable as a portable proof artifact

These artifacts can be independently verified without access to internal systems.

---

## Differentiation

### Logging Systems
Logging records events.

Provable AI enforces deterministic execution and produces cryptographic proof artifacts.

---

### Model Observability Tools
Observability monitors model behavior.

Provable AI enforces governance and decision integrity at execution time.

---

### Compliance Documentation
Documentation describes policies.

Provable AI enforces those policies programmatically before decisions execute.

---

## Result

AI decision systems become:

- Deterministic
- Governance-enforced
- Cryptographically verifiable
- Replayable
- Audit-ready

Provable AI turns trust-based AI decisions into provable infrastructure.