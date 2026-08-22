# Betting Strategy

Living document — update after each settled bet with what worked, what didn't, and why. The goal is to make decisions by written rules, not by feel, and to evolve the rules deliberately.

## Bankroll & staking

- **Bankroll:** ring-fenced pot seeded by the opening weekend (+£87 profit as of 16 Aug 2026). Betting money is entertainment budget — never top up from elsewhere to chase a loss.
- **Unit = £5.** Standard bet = 1 unit. High-conviction, well-researched bet on a strong card = 2 units max. Thin cards, speculative builders, experimental angles = 1 unit or no bet.
- **Never increase stakes because of a winning streak.** Wins don't change the next bet's probability. Equally, never chase after a losing day.
- **Cap (v2, agreed 22 Aug): £40 per week, hard, allocated freely across the days.** A stacked Saturday can take most of it; dead days bank theirs. The ceiling itself never flexes mid-week — no "one more because there are lots of fixtures". Rationale from the log: both full-card sweeps ran out of edge before running out of budget; the cap has only ever squeezed excluded-pile bets (£0 returned from £20 lifetime).
- **Weekly reset each Monday: cap = min(£40, 25% of bankroll).** Stakes scale with proven results in both directions — the only honest way stakes ever grow. Fixture density is never a reason; profit is.

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
14. **Promos are the only real +EV in the book — harvest them deliberately.** Opt in to offers as soon as they appear (costs nothing). A promo can justify a bet on an otherwise-ruled-out game ONLY if the bet is built to fit the promo's real edge (e.g. winner-agnostic legs on a coin-flip game with a bet-and-get). A promo-qualified bet may extend the daily cap by written exception, logged before placing — never silently.
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

- **22 Aug 2026, morning:** request to raise the weekly cap to £100 — declined. Context: fifth escalation inside one hour (stake mis-keys, extra-longshot request, uncap request), mid-winning-streak, no new information. £100 ≈ 140% of the then-current ~£72 bankroll; the agreed formula would set the next reset near £18. Standing answer: the cap rises only via the Monday formula — min(£40, 25% of bankroll) — i.e. a £100 week is reached by growing the bankroll to £400, never by declaration. Any future request to raise the cap outside the formula gets this same entry appended.
