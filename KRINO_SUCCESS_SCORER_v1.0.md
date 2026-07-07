# KRINO — SUCCESS SCORER v1.0  (FROZEN · pre-registered 2026-07-06)
**FROZEN.** This is the pre-registered mechanical adjudicator for the Phase-1 falsification test. It exists,
frozen, **before** the first graded episode (Aug-7) — the whole point of pre-registration. Any change requires a
**new versioned pre-registration** (v1.1, re-hashed); it is never edited silently. The canonical pre-registration
sha256 is recorded in the Forward Test Log.

## Scope (read first)
**This scorer evaluates the Phase-1 awareness model ONLY. It does NOT constitute a test of the full KRINO
architecture, as WIDEN / exogenous retrieval remains frozen until Phase-1 validation.** A Phase-1 fail tests the
chassis, not the final vehicle (see Layer 2 context-failure, and the honest limits).

## Why it exists
The falsification condition was prose-adjudicated ("was the read *better than naive*?" with no mechanical rule),
so a SUCCESS could be reached by generous reading (DL80 at project scale). This replaces the prose bar with a
frozen mechanical verdict. It removes the *softness*, not the *n*.

## What it grades
Two legs: **(A) awareness** — the read beats a naive baseline; **(B) deployment** — a mechanical deployment beats
a dumb staged rule. FAILED iff BOTH fail; SUCCESS iff EITHER wins. **Near-term: the deployment model is
unbuilt/out of scope, so the live scorer grades LEG A only; LEG B is DEFINED-BUT-DORMANT.** Since SUCCESS =
either leg, grading awareness alone fully tests the near-term null.

## Episode trigger
An evaluation episode begins when **any** of (frozen list, no post-hoc additions):
1. **S&P 500 drawdown ≥ 10%** from a recent peak **within ≤ 20 trading days** (fast-stress — a slow drift off a
   52-week high does NOT qualify), OR
2. **VIX daily close ≥ 30**, OR
3. **StressState transition** — into STRESS **or** out of STRESS, OR
4. **InflationState transition** — into REGIME **or** out of REGIME.
Grade dates are **not** triggers — they are the scheduled evaluation points for an already-defined read.
**Each episode is tagged EPISODE-TYPE = onset** (into a worse regime) **or recovery** (out of a worse regime),
stored as an explicit field in the Forward Test Log, so the dataset later shows whether KRINO was graded on
detecting danger or detecting normalization. Direction labels differ by type:
- **onset:** "did KRINO detect worsening conditions early?"
- **recovery:** "did KRINO identify improving conditions *without prematurely declaring safety*?"
The episode window (start → grade date) is fixed at trigger time and hashed.

## Naive baseline (what LEG A must beat)
**Pure persistence:** tomorrow resembles today. **No AI, no VIX, no additional indicators.** The baseline changes
only when the same episode trigger confirms a state transition. This is deliberately **independent of KRINO's own
panel inputs** — so KRINO's win must come from its *interpretation* calling the move before the trigger confirms,
not from re-using a shared signal like VIX.

## LEG A — the awareness test (two layers)
**Layer 1 = the SCORE (binary). Layer 2 = the DIAGNOSIS (separate — it does NOT change the score).**

### Layer 1 — Performance (this IS the verdict)
Ground-truth is fixed mechanically **before** the outcome (the realized state per the panel's measured-state
definition; no hindsight re-definition). KRINO **passes** iff **all three**:
1. **Correct directional regime call** — matches the realized ground-truth (labels per episode-type, above).
2. **Timing** — **either** a ≥ 5 trading-day lead over the baseline **or** the baseline misses the transition
   entirely.
3. **Confidence discipline** — a **High-confidence wrong call fails automatically** (no calibration *penalty*
   until enough episodes exist to compute one; the overconfidence veto always applies).
Anti-gaming: the read **and** this scorer are hash-committed before the episode resolves; forced-symmetry (the
opposing read is scored too, so a read that would have "confirmed" either way does not pass).

### Layer 2 — Failure diagnosis (fires only on a FAIL; a learning output, NOT the score)
If Layer 1 = FAIL, classify **why** — but treat the classifier itself **as a detector, not a story**: its output is
*"this episode satisfies pre-committed criteria X/Y/Z for category C,"* never a free-text *"probably lacked context."*
Each category's criteria are **pre-registered BEFORE the outcome**; no retroactive category assignment. **The diagnosis
does not soften the score — a well-explained failure is still a failure.**
- **Detection failure** — the mechanical layer was wrong.
- **Interpretation failure** — signals right, reasoning wrong. **← DEFAULT: a fail is interpretation-failure unless another category clears its burden.**
- **Context failure** — *HIGHER BURDEN* (the likeliest refuge). Must clear **all**: (1) an external fact existed before the signal moved, (2) it was publicly discoverable, (3) it was causally central, (4) the panel's **hash-committed outputs at the time** could not distinguish it from alternatives — answered from the *recorded* state, not a post-hoc "we couldn't have known," (5) it would have changed the thesis ranking had it been available. Fail any → **default to interpretation failure**.
- **Timing failure** — right read, wrong horizon. · **Transmission failure** — right cause, wrong propagation. · **Overconfidence failure** — High evidence-strength on a wrong call (already a Layer-1 veto; recorded here).
**Use of the diagnosis:** a **context failure that clears its full burden** is the evidence that separately feeds the *un-gate-WIDEN* decision — it still does **not** move this episode's score. All other diagnoses feed the Defect Log / calibration record.

### Classify → correct (kept separate — no auto-modification)
A failure classification says *what happened*; it does **not** auto-trigger a change. Corrections run a separate,
pre-registered pipeline: **classify → evidence-review → correction-proposal → future-validation**, never
classify → auto-correct. A failure must never become an automatic justification for the system to modify itself
(mirrors `[STANCE]` escalation: a recurring class escalates to the operator for a guardrail, not a silent self-edit).

## LEG B — the deployment test (DORMANT — deployment not built yet)
**Deferred; does NOT run in the near-term scorer.** The deployment model is deliberately unbuilt and out of scope
pre-Phase-1 — no live account, nothing bought, nothing to score. Defined only so it is ready to switch on if/when a
live deployment exists: KRINO-guided staged deployment vs the dumb buy-in-thirds rule, on a pre-committed realized
metric. Until then, ignore it — the live test is LEG A.

## Verdict (mechanical)
**The score is Layer 1 only.** Near-term (deployment dormant): SUCCESS if **LEG A Layer-1 wins**; FAILED if it
fails. **Layer 2 never changes the verdict** — it is a separate learning output. (Full rule when deployment exists:
FAILED = both legs fail; SUCCESS = either wins.) Recorded to the Forward Test Log; the verdict follows the frozen
rule, no prose adjudication.

## Honest limits
- **n ≈ 1.** One passing episode is **weak** evidence — the scorer removes prose-softness, NOT the small-sample
  problem. A single SUCCESS is "first hurdle cleared," not "validated."
- **Residual judgment lives in the ground-truth definition** — pre-committing it *before* the outcome is the guard
  against motivated reading, not a claim of zero judgment.
- **A richer scorer does not reduce the n you need.** The two-layer diagnosis makes each episode more *informative* —
  and so makes a single well-diagnosed episode *feel* like a lot of evidence. It is not; 5–10+ clean episodes still
  govern "validated."

## Frozen parameters (resolved policy priors — changeable only via a new pre-registered version)
Equity trigger **10% within ≤ 20 trading days** · Volatility **VIX close ≥ 30** · State transitions **in/out of
STRESS, in/out of REGIME** · Timing lead **≥ 5 trading days** · Baseline **pure persistence**. Settled by judgment
(PARAM-AUDIT candour), operator-endorsed 2026-07-06. Any change = a new versioned pre-registration, never a silent edit.

---
**FROZEN v1.0 · pre-registered 2026-07-06, before the first graded episode. Canonical sha256 recorded in the
Forward Test Log. Supersedes draft v0.1.**
