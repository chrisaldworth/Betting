# Betting Strategy

Living document — update after each settled bet with what worked, what didn't, and why. The goal is to make decisions by written rules, not by feel, and to evolve the rules deliberately.

## Bankroll & staking (v3 — daily-stake era, from 27 Aug 2026)

- **Staking plan (user decision, 27 Aug 2026): up to £10 on the day's recommended accumulator and up to £10 on the day's recommended bet builder.** These are **ceilings, not quotas** — a NO BET day stakes £0, and a day with edge in only one structure stakes only that one. Maximum possible exposure is £20/day; the honest expectation is that most weekdays are thin cards and stake far less.
- **This is a written restart, not an erased record.** Era 1 (15–24 Aug) closed at net −£6.60 across £130.55 staked, with the pot wiped to ~£10 mainly by unplanned side bets. That record stays permanent in `data/` and `logs/`. The new era's P/L starts from £0 and is measured on its own.
- **The two £10s are the entire day's budget.** No side bets, no second builders, no in-play additions, no horse racing. Era 1's data is unambiguous: planned bets +£33.40, unplanned bets −£40.00. Any bet outside the day's written card is a rule break regardless of result.
- **Never increase stakes because of a winning streak.** Wins don't change the next bet's probability. Equally, never chase after a losing day — the next day's card is the same two ceilings whatever yesterday did.
- **Circuit breaker: if the new era's running P/L reaches −£100, betting pauses for a written review week** (paper picks continue so the sample keeps building). Resumption and any staking change happen in writing here, between betting days, never mid-day.
- **Stake changes only by written amendment to this section**, dated, with the reason — the audit-trail practice from era 1 continues. In-the-moment requests to raise a stake get logged and declined by default (see audit trail below).

## Bet selection rules

1. **Research before price.** Form the view first (form, team news, motivation, venue trends), then compare to the odds. Only bet when our estimated probability beats the implied probability.
2. **Prefer one deeply-researched game over many shallow legs.** The bet-builder-on-one-game structure (result + scorer + game state, all telling the same story) is our best performer. Correlated legs in one narrative > uncorrelated "bankers".
3. **Max 3 legs in any acca.** Every leg compounds ~5% bookmaker margin and multiplies failure ways. Three ~70% legs is only a ~34% bet — accas of favourites are less safe than they feel.
4. **Draws kill accas.** For any leg priced above ~1.45, consider draw-no-bet or −0.5 Asian handicap instead of the straight win, and accept the lower price.
5. **No opening-day/opening-week "form" reads in the top leagues.** Early-season form is noise; class gaps (promoted side vs established side, cup minnow vs giant) are signal.
6. **Trap check before every bet:** is the favourite priced on reputation rather than current reality? (Rangers 4/11 while winless vs in-form St Mirren was the template trap. When market hesitation appears on a "banker" — like PSV at 1.60 — listen to it.)
7. **Team-sheet condition on any player leg.** If the named player isn't starting, the bet is off. No substituting a different player on the fly at the counter/app.
8. **Cup ties settle on 90 minutes.** Extra time/penalties don't count for match result or scorer markets — price that risk or use "to qualify".
9. **European hangover check:** teams playing between two-legged European ties rotate. Check the calendar either side of the fixture.
10. **Check bet365 Bet Boosts before placing** — favourites trebles and popular builders sometimes come pre-boosted; free margin if it matches our picks.
11. **Write it down before placing it.** Every bet goes into BETTING_LOG.md's pending table first, with its conditions. A bet that isn't in the log doesn't get placed — this is the rule the slip audit showed we need most.
12. **One bet per game.** A second builder on the same match doubles exposure without new information.
13. **Cash-out policy:** default is let it ride (cash-out embeds extra margin). Exception: partial cash-out to lock the stake back once the bet is heavily winning is acceptable — it worked well in the Community Shield. Never cash out a losing position out of boredom.
14. **Promos are the only real +EV in the book — harvest them deliberately.** *(v3 addition, 29 Aug: Super Boosts qualify ONLY when the boosted price beats our honest fair price for the selection — not merely the pre-boost price — AND the selection passes the playbook checks (minutes security, sensible market). A qualifying Super Boost may fill an empty or vacated daily slot at up to that slot's £10, logged before placing; it never stacks as an extra bet on top of a full card. Boosted longshots and scorer multis are marketing, not value — the harvest is boosts that cross fair price on high-probability events.)* Opt in to offers as soon as they appear (costs nothing). A promo can justify a bet on an otherwise-ruled-out game ONLY if the bet is built to fit the promo's real edge (e.g. winner-agnostic legs on a coin-flip game with a bet-and-get). A promo-qualified bet may extend the daily cap by written exception, logged before placing — never silently.
15. **Never expand leg count for bigger returns — expand odds-per-leg instead.** Five 70% legs ≈ 17% with five failure points and five margins paid. Handicaps on three researched games reach the same payout with fewer ways to die. Max 3 legs stays absolute.

## What we know so far (evidence log)

| Insight | Evidence | Confidence |
|---------|----------|------------|
| Single-game builders outperform accas | Havertz builder won (6.00 after void); Sunday acca lost | Low — small n, and U3.5 landed on exactly 3 goals |
| Class-gap legs are the most reliable | All 3 legs of Sat treble landed (by 1, 4 and 2 goal margins) | Low-medium |
| Short-priced home "bankers" in the Eredivisie are overrated | Feyenoord & Ajax both drew at home | Low — could be opening-weeks noise |
| Ruling games OUT is as valuable as picking games in | Avoided Rangers trap, Burnley–West Ham coin flip, PSV wobble | Medium |
| Player-prop legs carry lineup risk; bet365 voids them (doesn't lose them) | Nunes didn't play → leg void, builder repriced 8/1 → 6.00 | High (it's a rule, now verified) |
| Unplanned side bets are the profit leak | Planned bets +£55.20; unplanned bets −£20.00 | Medium — the mechanism is structural, not luck |

Update this table as the sample grows. Nothing above is proven at n=3 — treat every insight as a hypothesis.

## Honest expectations

- Even well-researched bets at combined odds of 2/1–8/1 lose more often than they win. The current +£87 includes meaningful luck.
- The bookmaker margin means long-run expected value is negative for almost all recreational bettors. The realistic goal is: lose slowly, win occasionally, enjoy it, and never let stakes grow past entertainment level.
- If it stops being fun or stakes start creeping: stop. (Support: GamCare 0808 8020 133, gamcare.org.uk, or bet365's deposit-limit tools.)

## Cadence

- **Before betting:** research → write the planned bet + conditions into BETTING_LOG.md (pending table) → check team news → place or pass.
- **After settling:** record result and P/L in the log, add a one-line lesson, and update the evidence table here if a hypothesis gained or lost support.
- **Weekly:** review the week's bets — did we follow our own rules? Rule-breaks matter more than results.

## Cap-change requests (audit trail)

- **27 Aug 2026:** project relaunched as a daily research system (see PLAN.md). User set the staking plan: £10/day acca + £10/day builder, replacing the v2 weekly-cap formula (which, applied to the wiped ~£10 pot, allowed ~£2.50/week). Recorded honestly: this is a stake *increase* directly after the pot was wiped, which the v2 formula existed to prevent. Accepted as the owner's deliberate, written restart of a new era — not an in-the-moment escalation — with these safeguards encoded: ceilings-not-quotas, NO BET days stake £0, no bets outside the daily card, and a −£100 circuit breaker that pauses betting for a review week. Era 1's −£6.60 net stays on the permanent record.
- **29 Aug 2026, mid-morning:** request to add a daily live 4-fold — declined per rules 3/15 (max 3 legs, absolute) and the fixture-density principle; today's full-board sweep found only two value legs, and each extra leg compounds ~2.5-5% margin. Counter-offer accepted into the system instead: a daily PAPER 4-fold "stretch line" (stake £0, settled nightly like any bet) to test the hypothesis with evidence. Goes live only via a written rule change if the paper record earns it. Rule-15 alternative for bigger payouts stays: expand odds-per-leg (handicaps), not leg count.
- **22 Aug 2026, morning:** request to raise the weekly cap to £100 — declined. Context: fifth escalation inside one hour (stake mis-keys, extra-longshot request, uncap request), mid-winning-streak, no new information. £100 ≈ 140% of the then-current ~£72 bankroll; the agreed formula would set the next reset near £18. Standing answer: the cap rises only via the Monday formula — min(£40, 25% of bankroll) — i.e. a £100 week is reached by growing the bankroll to £400, never by declaration. Any future request to raise the cap outside the formula gets this same entry appended.
