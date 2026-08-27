# Betting Log

**Generated from `data/bets.json` — edit the data, not this file** (then run `python3 scripts/generate_log.py`).

All stakes with bet365. Returns are logged from the actual slip, never from research estimates.

## Era 2: Daily-stake era (2026-08-27 → ongoing)

**Staking:** Ceilings, not quotas: up to £10/day on the recommended acca + up to £10/day on the recommended builder. NO BET days stake £0. No bets outside the daily card. Circuit breaker: pause + written review at era P/L of -£100.

### Open / pending

| # | Date | Bet | Type | Stake | Odds | Status | Conditions |
|---|------|-----|------|-------|------|--------|------------|
| 15 | 2026-08-27 | Chelsea (Match Result (90 mins)) + Fulham (Match Result (90 mins)) + Benfica (Match Result (90 mins)) | acca | £0.00 | 2.35 | 📝 RECOMMENDED | PAPER PICK — card was finalized after kickoff on the system's build day; £0 staked. Settle for calibration only. Odds are research estimates until slip-confirmed. Place before ~19:00 UK. |
| 16 | 2026-08-27 | Chelsea (Match Result (90 mins)) + Cole Palmer (Score or Assist) + Over (Chelsea Over 2.5 Goals) | builder | £0.00 | 3.8 | 📝 RECOMMENDED | PAPER PICK — card was finalized after kickoff on the system's build day; £0 staked. Settle for calibration only. PALMER MUST START (team sheets ~18:30) — not starting means bet off, no substitute pick. One bet on this game, no in-play additions. |

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
