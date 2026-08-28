# Research Playbook

How the morning run forms views. STRATEGY.md says what we're allowed to bet; this says how to research it. The edge, if we have one, comes from selectivity, promos, and honest probability estimates — not from volume.

## Per-leg research checklist

1. **xG over results.** Form the form-read from last 5-6 games' expected goals (FBref/Understat via search), not W/D/L. A side winning while losing the xG battle is due regression — and often overpriced; the reverse is where value hides. Cite the xG read in the pick notes when it drives a leg.
2. **Base-rate anchor first.** Before game-specific reasoning, start est_prob from the league base rate (below), then adjust with named reasons. An estimate that ends up 15+ points above base rate needs an unusually strong story.
3. **Team news from two dated sources**, and for every player leg: **minutes security** (nailed starter in a central role, not a rotation candidate), penalty/set-piece duty for scorer legs. Heavy-rotation cup XIs → team-level legs, not named-player goal involvement (lesson from bet #16).
4. **Referee check for texture legs.** Cards/fouls markets track the referee more than the players. No ref confirmed, or a low-card ref → no cards/fouls leg.
5. **Congestion check, mechanically:** days since last match for both sides, European tie either side of the fixture, travel. Three days' rest + a big game coming = rotation risk on favourites.
6. **Motivation/game-state:** two-legged ties where a draw suits one side, dead rubbers, cup priorities. A "win" leg on a team that doesn't need to win is mispriced by default (Beşiktaş dead-rubber rule).
7. **Trap check** (rule 6): is the favourite priced on reputation? Market hesitation on a "banker" is information.

## Placement-time checks (user, on the app)

- **Odds movement since the morning card:** our price drifting OUT = sharp money against us — re-read the reasoning before placing; shortening toward us = confirmation. Note the direction in the log.
- **Prefer Early Payout markets** for acca match-result legs at equal price — 2-0 up pays the leg regardless of the final score; it's free insurance and one of the only pro-punter features on the book.
- **Check Bet Boosts / promos** (rule 10) — still the only reliably +EV product on the site.
- Team-sheet conditions checked when XIs drop (~1h before KO). Condition unmet = bet off.

## League base rates (starting anchors, season-typical; refine from our own data as it accrues)

| League | Home win | Draw | Away win | Over 2.5 | BTTS |
|--------|----------|------|----------|----------|------|
| Premier League | ~44% | ~24% | ~32% | ~55% | ~52% |
| Championship | ~43% | ~26% | ~31% | ~48% | ~50% |
| League One/Two | ~42% | ~27% | ~31% | ~47% | ~49% |
| La Liga | ~45% | ~25% | ~30% | ~48% | ~48% |
| Serie A | ~42% | ~26% | ~32% | ~52% | ~51% |
| Bundesliga | ~44% | ~24% | ~32% | ~58% | ~55% |
| Eredivisie | ~46% | ~23% | ~31% | ~62% | ~57% |
| Cup tie, 2-division gap, big side at home | ~75-80% (90 min) | — | — | varies with rotation | — |

Draws ~25% everywhere is why draws kill accas (rule 4). These are anchors, not answers.

## What we deliberately don't do

- No in-play betting, no cash-out (except the written partial rule), no tipsters, no leg-count expansion, no bets outside the daily card. These are margin leaks, not research gaps.
- No staking by edge (Kelly) yet: fixed ceilings until the calibration + CLV record earns anything else. If we can't beat the closing line on paper, more data won't fix the picks — the process changes instead.

## Future data work (when the sample justifies it)

- Backtest thesis tags against football-data.co.uk historical CSVs (results + closing odds, free): put a real number on "class-gap cup favourite wins in 90'", "new-manager bounce", etc.
- Thesis-level hit rates on the dashboard once ~20+ settled legs carry tags.
