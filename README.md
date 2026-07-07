# krino-commitments

The public commitment log for **KRINO** — an experiment testing whether AI + open-source data + commodity
tools can build institution-grade macro-regime **awareness** (not prediction).

## The core claim
KRINO's credibility rests on **ordering**. Every artifact's sha256 is committed here — publicly, timestamped —
**before** it is published, and before the outcome it will be graded against has occurred. The commitment
*precedes* the result. That ordering, provable through this repo's git history, is the entire point: a read you
can change after the fact proves nothing; a read hashed here before the event cannot be silently revised.

## What's here
- `COMMITMENTS.md` — the **append-only** commitment log (artifact · sha256 · date).
- `METHODOLOGY.md` — the pre-committed falsification test and the frozen success scorer KRINO will be graded by.
- `KRINO_SUCCESS_SCORER_v1.0.md` — the frozen, pre-registered scorer (its sha256 is in the log).

## How to verify (nothing here asks for trust)
1. Read a sha256 line and its date from `COMMITMENTS.md`.
2. Confirm via `git log` that the commit landed on or before that date — the git timestamp is the tamper-evidence.
3. Run `sha256sum <artifact>` yourself and compare.

## Status
Phase 1 — the awareness model faces its first graded market episode (candidate ~Aug 2026); zero graded episodes
to date. "Still institution-only" is an accepted, honest outcome. Informational research only; not investment advice.
