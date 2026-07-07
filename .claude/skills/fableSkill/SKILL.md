---
name: fableSkill
description: Use when starting any non-trivial task or deliverable, when the request is vague about where or how the result will be used, and again before handing results to the user — reports, dashboards, single-file HTML, scripts, or multi-step builds that may be opened on phones, chat previews, or email.
---

# Fable Skill — Attacking Problems

## Overview

A structured loop for going from a vague request to a delivered, verified result.

**Core principle:** Work is not done when it works for you — it's done when it works where the user will actually use it.

## The Attack Loop

```
SCOPE → GROUND → INCREMENT → VERIFY → SHIP
              ↑___________________|  (loop until a FRESH check is clean)
```

### 1. SCOPE — before touching anything

- Restate the real deliverable in one sentence. Not the task — the thing the user will hold.
- **REQUIRED — fill the consumption slot:** who consumes the result, on what device/channel (phone chat preview? email attachment? browser? CI?), with what constraints (no sign-in, no JavaScript, offline, file-size, language).
  - If unstated: assume the most restrictive plausible context, design for it, and state the assumption in your reply.
  - Ask ONE question only if the answer would change the architecture.
- List knowns / unknowns / risks. Pick the smallest path that ships value.

### 2. GROUND — never operate on assumed state

- Read the file / image / current state BEFORE recording or editing it.
- Keep ONE source of truth (a registry file, a data file, a build script) and update it on every step.
- Fresh tool output beats memory; memory beats guessing; guessing gets labeled as a guess.

### 3. INCREMENT

- Smallest verifiable step first; confirm it landed before taking the next.
- After the second manual patch on the same artifact, stop: consolidate every step into one reproducible script and rebuild from scratch with it.

### 4. VERIFY — loops before answering

- Run it. Render it. **Look at the output with your own eyes** (screenshot); never infer behavior from reading the code.
- Simulate the consumer's environment from the SCOPE slot: mobile viewport, JavaScript disabled, dark AND light mode, the actual click path the user will take.
- Compute what is computable (validators, asserts, counts) instead of eyeballing it.
- Found a bug → fix → re-run the FULL check fresh. The loop ends when a fresh run is clean, not when a fix "should work".
- **REQUIRED BACKGROUND:** superpowers:verification-before-completion (no claims without fresh evidence). For any bug found: superpowers:systematic-debugging.

### 5. SHIP

- Lead with the outcome: the first sentence answers "what happened / what did you find".
- State what you verified AND what you did NOT check — name the unchecked risks explicitly.
- Label best-effort or uncertain parts (mappings, orderings, guesses) and invite correction.
- Deliver in a form the consumer can open with zero setup and zero sign-in.

## When Blocked

A tool or approach fails twice → switch to an alternative path, tell the user what failed, and keep the goal moving. Never go quiet, never claim partial success as full success.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Verified only in your own environment | Test the consumer's context: no-JS preview, phone viewport, mail client |
| Content that only exists after JavaScript runs | Pre-render content as static HTML; JS only enhances |
| Claiming done from reading the code | Run it and read the fresh output |
| QA log omits the delivery channel as a risk | The consumption slot is REQUIRED in scope and in the ship note |
| Uncertainty hidden to sound confident | Label the guess, invite correction |
| Third manual patch on the same artifact | One rebuild script, then rebuild |
| Answer buries the outcome under process narration | First sentence = result; detail after |
