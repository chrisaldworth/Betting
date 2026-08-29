# Betting Log

**Generated from `data/bets.json` — edit the data, not this file** (then run `python3 scripts/generate_log.py`).

All stakes with bet365. Returns are logged from the actual slip, never from research estimates.

## Era 2: Daily-stake era (2026-08-27 → ongoing)

**Staking:** Ceilings, not quotas: up to £10/day on the recommended acca + up to £10/day on the recommended builder. NO BET days stake £0. No bets outside the daily card. Circuit breaker: pause + written review at era P/L of -£100.

### Settled

| # | Date | Bet | Type | Stake | Odds | Result | Return | P/L | Running |
|---|------|-----|------|-------|------|--------|--------|-----|---------|
| 15 | 2026-08-27 | Chelsea (Match Result (90 mins)) ✓ + Fulham (Match Result (90 mins)) ✓ + Benfica (Match Result (90 mins)) ✓ | acca | £0.00 | 2.35 | ✅ WON | £0.00 | £0.00 | £0.00 |
| 16 | 2026-08-27 | Chelsea (Match Result (90 mins)) ✓ + Cole Palmer (Score or Assist) ✗ + Over (Chelsea Over 2.5 Goals) ✗ | builder | £0.00 | 3.8 | ❌ LOST | £0.00 | £0.00 | £0.00 |
| 18 | 2026-08-29 | Leverkusen (Match Result (Early Payout)) ✗ + Dortmund (Match Result (Early Payout)) ✓ | acca | £0.00 | 1.8 | ❌ LOST | £0.00 | £0.00 | £0.00 |
| 20 | 2026-08-29 | Dominik Szoboszlai (Player Shots on Target Over 0.5 (Super Boost 1.57 -> 2.00)) ✗ | single | £0.00 | 2.0 | ❌ LOST | £0.00 | £0.00 | £0.00 |
| 21 | 2026-08-29 | Leverkusen (Match Result) ✗ + Dortmund (Match Result) ✓ + Wolves (Match Result) ✓ + Liverpool (Match Result) ✗ | acca | £0.00 | 4.03 | ❌ LOST | £0.00 | £0.00 | £0.00 |

**Era 2 settled totals: staked £0.00 · returned £0.00 · net £0.00**

| Category | Bets | Staked | Returned | Net |
|----------|------|--------|----------|-----|
| Planned, researched | 5 | £0.00 | £0.00 | **£0.00** |

| Structure | Bets | Net |
|-----------|------|-----|
| acca | 3 | £0.00 |
| builder | 1 | £0.00 |
| single | 1 | £0.00 |

### No-bet days (discipline log)

- **2026-08-28** — NO BET both slots — thin Friday card (Palace v City only PL game; reputation-priced favourite with no est-prob edge; no third researchable leg). Full reasoning: picks/2026-08-28.md. Saturday is the first full live card.
- **2026-08-29** — SKIPPED AT THE TILL per pre-written condition: bet365 priced the builder 1.80 (slip screenshot, 08:30) vs our 2.0 minimum — the engine crushed the win/goals correlation (1.55 x 1.62 = 2.51 raw -> 1.80 offered). Rule fired exactly as designed. Pricing lesson: assume a harsher correlation crush on same-team result+goals pairs; our ~2.2 builder estimate was optimistic. Value spot: bet365 1.55 on Wolves vs ~1.42 consensus (top of market = positive expected CLV); Stoke conceded 5 in two straight defeats. Full reasoning: picks/2026-08-29.md

## Era 1: Weekly-cap era (2026-08-15 → 2026-08-24)

**Staking:** Unit £5; weekly cap min(£40, 25% of bankroll), reset Mondays

### Settled

| # | Date | Bet | Type | Stake | Odds | Result | Return | P/L | Running |
|---|------|-----|------|-------|------|--------|--------|-----|---------|
| 1 | 2026-08-15 | Middlesbrough (Match Result) ✓ + Celtic (Match Result (90 mins)) ✓ + Porto (Match Result) ✓ | acca | £10.00 | 2.83 | ✅ WON | £28.40 | £18.40 | £18.40 |
| 2 | 2026-08-15 | Middlesbrough (Match Result) ✓ + Bradford (Match Result) + ? + ? **UNPLANNED** | acca | £10.00 | ? | ❌ LOST | £0.00 | £-10.00 | £8.40 |
| 3 | 2026-08-16 | Havertz (Anytime Scorer) ✓ + Nunes (1+ Fouls Committed) (void) + Under (Under 3.5 Goals) ✓ | builder | £10.00 | 6.0 | ✅ WON | £56.80 | £46.80 | £55.20 |
| 4 | 2026-08-16 | UNPLANNED second builder on same game — rule 12 violation; doubled exposure with **UNPLANNED** | builder | £10.00 | ? | ❌ LOST | £0.00 | £-10.00 | £45.20 |
| 5 | 2026-08-16 | Feyenoord (Match Result) ✗ + Besiktas (Match Result) ✓ + Ajax (Match Result) ✗ | acca | £10.00 | 2.55 | ❌ LOST | £0.00 | £-10.00 | £35.20 |
| 6 | 2026-08-17 | Pavlidis (Anytime Scorer) ✓ + Benfica (Match Result) ✓ + Under (Under 3.5 Goals) ✗ | builder | £6.80 | 3.5 | ❌ LOST | £0.00 | £-6.80 | £28.40 |
| 7 | 2026-08-21 | Arsenal (Match Result) ✓ + Arsenal over 1 (Team Over 1 Goals) ✓ + Saka (3+ Shots) ✓ | builder | £10.00 | 2.25 | ✅ WON | £28.75 | £18.75 | £47.15 |
| 8 | 2026-08-22 | Man Utd (Match Result) ✗ + Mbeumo (Score or Assist) + McBurnie (2+ Fouls Committed) | builder | £10.00 | 4.2 | ❌ LOST | £0.00 | £-10.00 | £37.15 |
| 9 | 2026-08-22 | Leverkusen (Match Result (90 mins)) + Luton (Match Result) + Leicester (Match Result) | acca | £10.00 | 2.72 | ❌ LOST | £0.00 | £-10.00 | £27.15 |
| 10 | 2026-08-22 | Real Madrid -1 (Handicap Result -1) + Athletic (Match Result) + West Ham -1 (Handicap Result -1) | acca | £3.75 | 7.79 | ❌ LOST | £0.00 | £-3.75 | £23.40 |
| 11 | 2026-08-22 | Yes (BTTS) + Over (Over 1.5 Goals) | builder | £10.00 | 2.6 | ❌ LOST | £0.00 | £-10.00 | £13.40 |
| 12 | 2026-08-22 | UNPLANNED second builder on same game (rule 12 violation). Cashed out at stake. **UNPLANNED** | builder | £10.00 | ? | 💰 CASHED OUT | £10.00 | £0.00 | £13.40 |
| 13 | 2026-08-22 | Man Utd (Super Boost) ✗ **UNPLANNED** | single | £10.00 | 2.0 | ❌ LOST | £0.00 | £-10.00 | £3.40 |
| 14 | 2026-08-22 | Geryon (Win) ✗ **UNPLANNED** | single | £10.00 | ? | ❌ LOST | £0.00 | £-10.00 | £-6.60 |

**Era 1 settled totals: staked £130.55 · returned £123.95 · net £-6.60**

| Category | Bets | Staked | Returned | Net |
|----------|------|--------|----------|-----|
| Planned, researched | 9 | £80.55 | £113.95 | **£33.40** |
| Unplanned side bets | 5 | £50.00 | £10.00 | **£-40.00** |

| Structure | Bets | Net |
|-----------|------|-----|
| acca | 5 | £-15.35 |
| builder | 7 | £28.75 |
| single | 2 | £-20.00 |

## Free bets

- £5.00 — Brentford v Spurs Bet & Get promo (22 Aug) — unconfirmed — check bet365 account; expires per offer terms

---

Era 1's full prose log with per-bet lessons: `logs/era1-aug2026.md`. Rules and evidence table: `STRATEGY.md`. Daily research notes: `picks/`.
