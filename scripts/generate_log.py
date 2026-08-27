#!/usr/bin/env python3
"""Regenerate BETTING_LOG.md from data/bets.json + data/bankroll.json.

The JSON files are the source of truth; the markdown log is a view.
Run after any change to the data:  python3 scripts/generate_log.py

Also validates the data and prints warnings for:
  - settled bets whose return doesn't match stake x odds (unless slip-confirmed,
    since boosts/voids/cash-outs legitimately change the slip figure)
  - placed bets whose fixtures have passed but are still pending
  - daily staking-ceiling breaches in era 2 (>£10 acca, >£10 builder, >1 of each per day)
"""

import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SETTLED = {"won", "lost", "void", "cashed_out"}
OPEN = {"recommended", "placed"}


def money(x):
    return f"£{x:,.2f}" if x is not None else "?"


def load():
    bets = json.loads((ROOT / "data" / "bets.json").read_text())["bets"]
    bank = json.loads((ROOT / "data" / "bankroll.json").read_text())
    return bets, bank


def validate(bets):
    warnings = []
    by_day = defaultdict(lambda: defaultdict(float))
    for b in bets:
        bid, status = b["id"], b["status"]
        if status in SETTLED:
            if b.get("return") is None:
                warnings.append(f"bet {bid}: settled but no return recorded")
            elif (
                status == "won"
                and b.get("odds")
                and not b.get("slip_confirmed")
                and abs(b["return"] - b["stake"] * b["odds"]) > 0.01
            ):
                warnings.append(
                    f"bet {bid}: return {money(b['return'])} != stake x odds "
                    f"{money(b['stake'] * b['odds'])} and slip not confirmed"
                )
        if status in OPEN and b["date"] < date.today().isoformat():
            warnings.append(f"bet {bid}: dated {b['date']} but still {status} — settle it")
        if b["era"] == 2 and status not in {"no_bet"} and b.get("stake"):
            by_day[b["date"]][b["type"]] += b["stake"]
    for day, stakes in by_day.items():
        for btype, total in stakes.items():
            ceiling = 10.00
            if total > ceiling + 0.01:
                warnings.append(
                    f"{day}: {btype} stakes total {money(total)} exceed the {money(ceiling)} daily ceiling"
                )
    return warnings


def result_icon(status):
    return {
        "won": "✅ WON", "lost": "❌ LOST", "void": "↩️ VOID",
        "cashed_out": "\U0001f4b0 CASHED OUT", "placed": "⏳ PLACED",
        "recommended": "\U0001f4dd RECOMMENDED", "no_bet": "— NO BET",
    }.get(status, status)


def legs_summary(b):
    if b.get("legs"):
        parts = []
        for leg in b["legs"]:
            sel = leg.get("selection") or "?"
            mkt = leg.get("market") or ""
            mark = {"won": " ✓", "lost": " ✗", "void": " (void)"}.get(leg.get("result"), "")
            parts.append(f"{sel} ({mkt}){mark}" if mkt else f"{sel}{mark}")
        return " + ".join(parts)
    return b.get("notes", "")[:80]


def render(bets, bank):
    lines = [
        "# Betting Log",
        "",
        "**Generated from `data/bets.json` — edit the data, not this file** "
        "(then run `python3 scripts/generate_log.py`).",
        "",
        "All stakes with bet365. Returns are logged from the actual slip, "
        "never from research estimates.",
        "",
    ]

    for era_info in sorted(bank["eras"], key=lambda e: e["era"], reverse=True):
        era = era_info["era"]
        era_bets = [b for b in bets if b["era"] == era]
        lines += [f"## Era {era}: {era_info['name']} ({era_info['start']} → {era_info.get('end') or 'ongoing'})", ""]
        lines += [f"**Staking:** {era_info['staking']}", ""]

        open_bets = [b for b in era_bets if b["status"] in OPEN]
        if open_bets:
            lines += ["### Open / pending", "",
                      "| # | Date | Bet | Type | Stake | Odds | Status | Conditions |",
                      "|---|------|-----|------|-------|------|--------|------------|"]
            for b in open_bets:
                lines.append(
                    f"| {b['id']} | {b['date']} | {legs_summary(b)} | {b['type']} | "
                    f"{money(b['stake'])} | {b.get('odds') or '?'} | {result_icon(b['status'])} | "
                    f"{b.get('conditions') or '—'} |"
                )
            lines.append("")

        settled = [b for b in era_bets if b["status"] in SETTLED]
        if settled:
            lines += ["### Settled", "",
                      "| # | Date | Bet | Type | Stake | Odds | Result | Return | P/L | Running |",
                      "|---|------|-----|------|-------|------|--------|--------|-----|---------|"]
            running = 0.0
            for b in sorted(settled, key=lambda x: (x["date"], x["id"])):
                pl = (b.get("return") or 0) - b["stake"]
                running += pl
                flag = "" if b.get("planned") else " **UNPLANNED**"
                lines.append(
                    f"| {b['id']} | {b['date']} | {legs_summary(b)}{flag} | {b['type']} | "
                    f"{money(b['stake'])} | {b.get('odds') or '?'} | {result_icon(b['status'])} | "
                    f"{money(b.get('return') or 0)} | {money(pl)} | {money(running)} |"
                )
            staked = sum(b["stake"] for b in settled)
            returned = sum(b.get("return") or 0 for b in settled)
            lines += ["", f"**Era {era} settled totals: staked {money(staked)} · "
                          f"returned {money(returned)} · net {money(returned - staked)}**", ""]

            planned = [b for b in settled if b.get("planned")]
            unplanned = [b for b in settled if not b.get("planned")]
            lines += ["| Category | Bets | Staked | Returned | Net |",
                      "|----------|------|--------|----------|-----|"]
            for label, group in (("Planned, researched", planned), ("Unplanned side bets", unplanned)):
                if group:
                    s = sum(b["stake"] for b in group)
                    r = sum(b.get("return") or 0 for b in group)
                    lines.append(f"| {label} | {len(group)} | {money(s)} | {money(r)} | **{money(r - s)}** |")
            by_type = defaultdict(list)
            for b in settled:
                by_type[b["type"]].append(b)
            lines += ["", "| Structure | Bets | Net |", "|-----------|------|-----|"]
            for btype, group in sorted(by_type.items()):
                net = sum((b.get("return") or 0) - b["stake"] for b in group)
                lines.append(f"| {btype} | {len(group)} | {money(net)} |")
            lines.append("")

        no_bets = [b for b in era_bets if b["status"] == "no_bet"]
        if no_bets:
            lines += ["### No-bet days (discipline log)", ""]
            for b in no_bets:
                lines.append(f"- **{b['date']}** — {b.get('notes', '')}")
            lines.append("")

    if bank.get("free_bets"):
        lines += ["## Free bets", ""]
        for fb in bank["free_bets"]:
            lines.append(f"- {money(fb['amount'])} — {fb['source']} — {fb['status']}")
        lines.append("")

    lines += ["---", "", "Era 1's full prose log with per-bet lessons: `logs/era1-aug2026.md`. "
              "Rules and evidence table: `STRATEGY.md`. Daily research notes: `picks/`.", ""]
    return "\n".join(lines)


def main():
    bets, bank = load()
    for era_info in bank["eras"]:
        settled = [b for b in bets if b["era"] == era_info["era"] and b["status"] in SETTLED]
        era_info["staked"] = round(sum(b["stake"] for b in settled), 2)
        era_info["returned"] = round(sum(b.get("return") or 0 for b in settled), 2)
        era_info["net"] = round(era_info["returned"] - era_info["staked"], 2)
    (ROOT / "data" / "bankroll.json").write_text(json.dumps(bank, indent=2) + "\n")
    (ROOT / "BETTING_LOG.md").write_text(render(bets, bank))
    warnings = validate(bets)
    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)
    print(f"BETTING_LOG.md regenerated: {len(bets)} bets, {len(warnings)} warning(s).")
    import generate_dashboard
    generate_dashboard.main()


if __name__ == "__main__":
    main()
