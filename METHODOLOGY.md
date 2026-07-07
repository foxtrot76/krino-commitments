# KRINO — Pre-committed Methodology

Stated on the public record, **before** the first graded episode, so the test cannot be moved after the outcome.

## The falsification condition
KRINO's awareness read is graded against a naive baseline on a real market-stress episode. **FAILED** if the read
is no better than the naive baseline (and, once a live deployment exists, the deployment also no better than a dumb
staged rule). **SUCCESS** if the read beats the naive baseline. A null result — "still institution-only" — is a
valid, published outcome.

## The scorer (frozen v1.0 — full text in `KRINO_SUCCESS_SCORER_v1.0.md`; its sha256 is in the log)
- **Episode trigger:** S&P 500 drawdown -10% within <=20 trading days · or VIX close >=30 · or a StressState
  transition (in/out of STRESS) · or an InflationState transition (in/out of REGIME). Each tagged onset or recovery.
- **Naive baseline:** pure persistence — tomorrow resembles today; no AI, no extra indicators; state changes only
  when the trigger fires.
- **Pass (Layer 1 — the score):** correct directional regime call AND (>=5 trading-day lead over the baseline OR
  the baseline misses the transition entirely) AND no overconfident wrong call.
- **Diagnosis (Layer 2 — separate, never changes the score):** a pre-committed failure taxonomy classifies *why* a
  read failed; it informs learning, not the verdict.
- **Scope:** grades the Phase-1 awareness model only; the richer context engine is deliberately frozen until
  Phase-1 clears — a Phase-1 result tests the chassis, not the finished vehicle.
- **Honesty limit:** n is approximately 1. A single pass is "first hurdle cleared," not "validated"; many clean
  episodes are required.

## What moves the published state
Only a pre-registered falsifier. Never review volume, votes, or narrative. Challenges are logged and dispositioned
against frozen constraints; the state does not move on argument count.

*Informational research only; not investment advice.*
