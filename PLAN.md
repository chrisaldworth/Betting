# Project Plan — Daily Football Research, Recommendations & Auto-Settlement

Goal: a daily system that researches the day's football, recommends **one accumulator and one bet builder** (bet365), tracks every bet, checks results automatically, records the payout, and evolves its rules from evidence. Target: profit — measured honestly, over a real sample.

This builds on the existing `STRATEGY.md` and `BETTING_LOG.md`. Nothing there is thrown away; the rules that already exist (max 3 legs, one bet per game, write-it-down-before-placing, weekly cap formula) were earned with real money and carry forward.

---

## Where we actually are (honest baseline)

- Bankroll: **~£10** (started ~£100 of stakes lifetime, peaked +£87, wiped on 22 Aug — almost entirely by unplanned side bets, not the researched system).
- The standing weekly cap formula (`min(£40, 25% of bankroll)`, reset Mondays) currently allows **~£2.50/week**. A "new project" doesn't reset that number by itself — see **Decision 1** at the bottom.
- The one robust finding so far: **planned, researched bets are net positive (+£33.40); unplanned bets are net −£40**. The system's biggest edge is stopping bets, not picking them.

## What we're building

### Phase 1 — Structured tracking (the foundation)

Move from prose tables to a structured record so settlement and analytics can be automated:

- `data/bets.json` — every bet as a record: id, date, type (acca/builder/single), legs (market, selection, odds, fixture, kickoff), stake, combined odds, boosts/promos, status (`recommended` → `placed` → `won/lost/void/cashed-out`), actual return from the slip, conditions (team-sheet, promo).
- `data/bankroll.json` — running balance, weekly cap state, deposits/withdrawals (each with a written reason).
- `BETTING_LOG.md` — regenerated from the data by a script, so the human-readable log never drifts from the numbers.
- `picks/YYYY-MM-DD.md` — the daily research note: fixtures scanned, games ruled out and why, the recommended acca + builder with reasoning, prices, and conditions.

### Phase 2 — The daily loop (two scheduled runs)

**Morning research run (~09:00 UK):**
1. Pull the day's fixture list (football-data.org free API covers PL, EFL via web, Champions League, top European leagues; web search fills gaps for team news).
2. Research: form, team news/injuries, motivation, rotation risk (European calendar check), venue quirks — per the existing selection rules.
3. Produce the day's card in `picks/YYYY-MM-DD.md`:
   - **Recommended acca** — max 3 legs, draw-no-bet/handicap preferred over straight wins above ~1.45, class-gap legs preferred over form reads.
   - **Recommended bet builder** — one deeply-researched game, correlated legs telling one story, mixed across result/player/texture dimensions (the log shows bet365's engine crushes same-direction stacks).
   - **Or NO BET** — thin-card discipline is a first-class output, not a failure. A day with no edge produces a written "no bet" with reasons.
4. Write both into the pending table with stakes and conditions. You place on bet365 and confirm back the **actual slip odds and stake** (the log's own rule: log from the slip, not the research estimate).

**Evening settlement run (~23:00 UK, or next morning):**
1. Fetch final scores for every fixture in pending bets (results API + web search).
2. Auto-settle what's mechanically checkable: match results, handicaps, over/unders, BTTS.
3. Player-prop legs (scorers, shots, fouls) settled from match stats via web search; where a boost, void, or partial cash-out makes the slip differ from the calculation, the computed payout is provisional until you confirm the slip figure.
4. Update `bets.json`, regenerate the log, recompute running P/L and bankroll, commit and push.

Both runs are scheduled sessions (this environment supports cron-style routines) that commit their output to this repo — so the record builds itself daily without either of us remembering to do it.

### Phase 3 — Evolution (how the system gets better)

- **Evidence table stays**, but backed by real splits the data now supports: builders vs accas, class-gap legs vs form legs, price bands, leg counts, promo bets vs standard.
- **Closing line value (CLV):** record the odds we take vs the closing odds. At small sample sizes, P/L is mostly noise — consistently beating the closing price is the earliest honest signal that the research has edge. If we can't beat the close, the picks process changes before the stakes do.
- **Weekly review (Mondays, automated):** rules-adherence check (rule-breaks matter more than results), evidence table update, cap reset by formula, and one concrete rule change proposal if the data supports it.
- Rule changes are made **in writing in STRATEGY.md, between betting days, never mid-day** — the existing audit-trail practice continues.

## Daily recommendation format

Each day's card will look like:

```
## Sat 30 Aug — Card

### Acca (1 unit)
1. Team A draw-no-bet @ 1.52 — [reasoning, 2-3 lines]
2. Team B −0.5 @ 1.70 — [reasoning]
3. Team C win @ 1.45 — [reasoning]
Combined ~3.75. Conditions: none / team-sheet on leg X.

### Bet builder (1 unit) — Game D v E
- D to win @ ~1.60
- Player X 2+ shots on target
- Over 8.5 D corners
~4.5 combined. Story: [why these legs are the same thesis].
Conditions: Player X starting, else bet is off.

### Ruled out today: [games + one-line reasons]
```

## Result-checking design (and its honest limits)

| Market type | Auto-settle source | Reliability |
|---|---|---|
| Match result, handicaps, O/U, BTTS | football-data.org / web scores | Fully automatic |
| Anytime scorer, assists | Match reports via web search | Automatic, high confidence |
| Shots, fouls, corners, cards | Stats sites via web search | Automatic, verify on odd cases |
| Actual payout (boosts, voids, cash-out) | **Your slip** | Computed provisionally; slip figure wins |

## Guardrails carried forward (non-negotiable)

- Every bet is written down **before** it's placed; a bet not in the log doesn't get placed.
- One bet per game; max 3 acca legs; no unplanned side bets — they are the documented profit leak.
- Stakes set by the written formula, never by streaks, fixture density, or requests mid-week (the cap-change audit trail continues).
- Daily recommendations do **not** mean daily bets. Expect "NO BET" days regularly — most weekdays have thin cards.
- Honest expectations stand: bookmaker margin makes long-run EV negative for nearly all recreational bettors. The goal is disciplined entertainment that's demonstrably better than undisciplined, with profit as the scoreboard — not an income plan. If it stops being fun: stop (GamCare 0808 8020 133).

---

## Decisions — RESOLVED 27 Aug 2026

- **Decision 1 (bankroll):** user chose a daily-stake restart — **up to £10/day on the acca + up to £10/day on the builder** (ceilings, not quotas). Encoded as staking v3 in STRATEGY.md with safeguards (NO BET days = £0, no bets outside the daily card, −£100 circuit breaker). Era 1's record stays permanent.
- **Decision 2 (schedule):** research daily ~09:00 UK, settlement ~23:00 UK (routines live; cron in UTC: 08:00 / 22:00).
- **Decision 3 (leagues):** default scope adopted — PL, EFL, European competitions, top-5 leagues on big cards.

**Build status:** Phases 1–2 built and live on 27 Aug — data schema (`data/`), settlement/log script (`scripts/generate_log.py`), first daily card (`picks/2026-08-27.md`, paper — produced after kickoff on build day), and both scheduled routines. Phase 3 (CLV capture, weekly review) runs inside the Monday morning routine.

<details><summary>Original decision list (pre-resolution)</summary>

## Decisions needed before build

**Decision 1 — the bankroll.** The current pot is ~£10 and the standing formula makes this a ~£2.50 week. A "new project" is a fresh system, but a fresh *pot* after a wipe-out is exactly what the strategy's founding rule ("never top up to keep betting") was written to prevent. Three honest options:
- **(a) Paper-trade first** *(recommended)*: run the full daily system with recorded but unplaced recommendations for 2–3 weeks. Costs nothing, builds the sample, proves (or disproves) the picks before money returns. Real stakes resume when the paper record earns it.
- **(b) Re-seed with a written restart**: a new ring-fenced pot (e.g. £50), logged as a deliberate restart with the old −£90 kept on the permanent record — a new season, not an erased one. Cap formula applies from the new number.
- **(c) Formula only**: keep betting from the £10 with ~£2.50 weeks until it grows or dies.

**Decision 2 — schedule times.** Proposed: research 09:00 UK, settlement 23:00 UK, weekly review Monday morning. Adjustable.

**Decision 3 — scope of leagues.** Proposed core: Premier League, EFL, Champions/Europa League, plus top-5 European leagues on big cards. Wider = more noise, thinner research per game.

## Build order (as executed)

1. `data/` schema + migration of the 14 historical bets into it.
2. Settlement script + log regeneration.
3. First manual daily card (prove the format).
4. Scheduled morning + evening routines.
5. Weekly review routine + CLV tracking.

</details>
