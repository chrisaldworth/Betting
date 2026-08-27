#!/usr/bin/env python3
"""Generate dashboard.html — a self-contained, theme-aware view of the ledger.

Reads data/bets.json + data/bankroll.json. Run via generate_log.py (which calls
this) or directly:  python3 scripts/generate_dashboard.py
"""

import html
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SETTLED = {"won", "lost", "void", "cashed_out"}
OPEN = {"recommended", "placed"}

CSS = """
:root {
  --bg: #F7F5F1; --surface: #FFFFFF; --ink: #26221B; --ink-2: #5C5548;
  --ink-3: #8A8272; --line: #E4DFD4; --accent: #7E6423; --accent-soft: #F0E9D8;
  --mark-era1: #2E6FB8; --mark-era2: #9A7B2D;
  --win: #2E7D4F; --win-bg: #E3F0E8; --loss: #B3423A; --loss-bg: #F6E5E3;
  --pend: #6E6759; --pend-bg: #EFEBE2;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #16140F; --surface: #1F1C16; --ink: #EDE8DC; --ink-2: #B5AC9B;
    --ink-3: #8A8272; --line: #332F26; --accent: #D3B054; --accent-soft: #2C2617;
    --mark-era1: #4E8BD4; --mark-era2: #AC8628;
    --win: #5CB585; --win-bg: #1E3328; --loss: #DE8177; --loss-bg: #3A2422;
    --pend: #A79D8A; --pend-bg: #2A2620;
  }
}
:root[data-theme="dark"] {
  --bg: #16140F; --surface: #1F1C16; --ink: #EDE8DC; --ink-2: #B5AC9B;
  --ink-3: #8A8272; --line: #332F26; --accent: #D3B054; --accent-soft: #2C2617;
  --mark-era1: #4E8BD4; --mark-era2: #AC8628;
  --win: #5CB585; --win-bg: #1E3328; --loss: #DE8177; --loss-bg: #3A2422;
  --pend: #A79D8A; --pend-bg: #2A2620;
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--ink);
  font-family: "Libre Franklin", "Helvetica Neue", Arial, sans-serif;
  font-size: 15px; line-height: 1.55;
}
.wrap { max-width: 960px; margin: 0 auto; padding: 40px 20px 64px; }
.eyebrow {
  font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--accent); font-weight: 600; margin: 0 0 10px;
}
.hero-num {
  font-family: "Fraunces", Georgia, serif; font-weight: 600;
  font-size: clamp(44px, 9vw, 72px); line-height: 1.02; margin: 0;
  font-variant-numeric: tabular-nums; letter-spacing: -0.01em;
}
.hero-num.pos { color: var(--win); } .hero-num.neg { color: var(--loss); }
.hero-sub { color: var(--ink-2); margin: 10px 0 0; font-size: 14px; }
.hero-sub strong { color: var(--ink); font-weight: 600; }
.tiles { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 10px; margin: 28px 0 0; }
.tile { background: var(--surface); border: 1px solid var(--line); border-radius: 6px; padding: 12px 14px; }
.tile .k { font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--ink-3); font-weight: 600; }
.tile .v { font-family: "Spline Sans Mono", ui-monospace, monospace; font-size: 19px; margin-top: 4px; font-variant-numeric: tabular-nums; }
.tile .v small { font-size: 12px; color: var(--ink-3); font-family: "Libre Franklin", sans-serif; }
h2 {
  font-family: "Fraunces", Georgia, serif; font-weight: 600; font-size: 21px;
  margin: 44px 0 4px; text-wrap: balance;
}
.sec-note { color: var(--ink-3); font-size: 13px; margin: 0 0 14px; }
.cards { display: grid; gap: 12px; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
.bet-card { background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 16px 18px; }
.bet-card .top { display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; margin-bottom: 8px; }
.tag { font-size: 10px; letter-spacing: 0.12em; text-transform: uppercase; font-weight: 700; color: var(--accent); background: var(--accent-soft); border-radius: 3px; padding: 2px 7px; }
.tag.paper { color: var(--pend); background: var(--pend-bg); }
.bet-card .game { font-weight: 600; }
.bet-card ol { margin: 6px 0 10px; padding-left: 20px; color: var(--ink-2); }
.bet-card ol li { margin: 3px 0; }
.bet-card .odds { font-family: "Spline Sans Mono", ui-monospace, monospace; color: var(--ink); font-variant-numeric: tabular-nums; }
.bet-card .cond { font-size: 13px; color: var(--ink-3); border-top: 1px solid var(--line); padding-top: 9px; margin-top: 4px; }
.chart-box { background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 18px 18px 8px; position: relative; }
.legend { display: flex; gap: 18px; font-size: 12.5px; color: var(--ink-2); margin: 0 0 6px; }
.legend .sw { display: inline-block; width: 14px; height: 3px; border-radius: 2px; vertical-align: middle; margin-right: 6px; }
svg text { font-family: "Spline Sans Mono", ui-monospace, monospace; font-size: 10.5px; fill: var(--ink-3); }
svg .dlabel { font-weight: 600; font-size: 11px; }
#tip {
  position: absolute; pointer-events: none; display: none; z-index: 3;
  background: var(--surface); border: 1px solid var(--line); border-radius: 6px;
  box-shadow: 0 4px 14px rgba(0,0,0,0.12); padding: 8px 11px; font-size: 12.5px;
  max-width: 240px; color: var(--ink-2);
}
#tip .t1 { color: var(--ink); font-weight: 600; }
#tip .mono { font-family: "Spline Sans Mono", ui-monospace, monospace; font-variant-numeric: tabular-nums; }
.table-scroll { overflow-x: auto; border: 1px solid var(--line); border-radius: 8px; background: var(--surface); }
table { border-collapse: collapse; width: 100%; min-width: 720px; font-size: 13.5px; }
th { text-align: left; font-size: 10.5px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--ink-3); font-weight: 600; padding: 10px 12px; border-bottom: 1px solid var(--line); }
td { padding: 9px 12px; border-bottom: 1px solid var(--line); vertical-align: top; color: var(--ink-2); }
tr:last-child td { border-bottom: none; }
td.num, th.num { text-align: right; font-family: "Spline Sans Mono", ui-monospace, monospace; font-variant-numeric: tabular-nums; white-space: nowrap; }
td.desc { min-width: 260px; color: var(--ink); }
td .sub { color: var(--ink-3); font-size: 12px; }
.pill { display: inline-block; font-size: 10.5px; font-weight: 700; letter-spacing: 0.06em; border-radius: 999px; padding: 2px 9px; white-space: nowrap; }
.pill.won { color: var(--win); background: var(--win-bg); }
.pill.lost { color: var(--loss); background: var(--loss-bg); }
.pill.other { color: var(--pend); background: var(--pend-bg); }
.pill.openb { color: var(--accent); background: var(--accent-soft); }
.chip { display: inline-block; font-size: 10px; font-weight: 600; letter-spacing: 0.05em; color: var(--loss); border: 1px solid var(--loss); border-radius: 3px; padding: 0 5px; margin-left: 6px; }
.chip.paper { color: var(--pend); border-color: var(--pend); }
td .pl-pos { color: var(--win); } td .pl-neg { color: var(--loss); }
footer { margin-top: 48px; border-top: 1px solid var(--line); padding-top: 18px; color: var(--ink-3); font-size: 12.5px; }
footer p { margin: 4px 0; }
@media (prefers-reduced-motion: no-preference) { .bet-card, .tile { transition: border-color 120ms ease; } }
"""

JS = """
(function () {
  var box = document.getElementById('chartbox');
  var svg = document.getElementById('ledger');
  var tip = document.getElementById('tip');
  var cross = document.getElementById('cross');
  var pts = JSON.parse(document.getElementById('pts').textContent);
  if (!svg || !pts.length) return;
  function show(p, clientX, clientY) {
    tip.innerHTML = '<div class="t1">' + p.t + '</div>' + p.d +
      ' &middot; P/L <span class="mono">' + p.pl + '</span><br>Running: <span class="mono">' + p.cum + '</span>';
    tip.style.display = 'block';
    var r = box.getBoundingClientRect();
    var x = clientX - r.left + 14, y = clientY - r.top - 10;
    if (x + 250 > r.width) x -= 270;
    tip.style.left = x + 'px'; tip.style.top = y + 'px';
    cross.setAttribute('x1', p.x); cross.setAttribute('x2', p.x);
    cross.style.display = 'block';
  }
  svg.addEventListener('mousemove', function (ev) {
    var r = svg.getBoundingClientRect();
    var vx = (ev.clientX - r.left) / r.width * SVG_W;
    var best = pts[0], bd = 1e9;
    for (var i = 0; i < pts.length; i++) {
      var d = Math.abs(pts[i].x - vx);
      if (d < bd) { bd = d; best = pts[i]; }
    }
    show(best, ev.clientX, ev.clientY);
  });
  svg.addEventListener('mouseleave', function () {
    tip.style.display = 'none'; cross.style.display = 'none';
  });
})();
"""

SVG_W, SVG_H = 880, 250
PAD_L, PAD_R, PAD_T, PAD_B = 46, 70, 16, 26


def money(x, signed=False):
    if x is None:
        return "?"
    sign = "−" if x < 0 else ("+" if signed and x > 0 else "")
    return f"{sign}£{abs(x):,.2f}"


def esc(s):
    return html.escape(str(s or ""))


def legs_lines(b):
    out = []
    for leg in b.get("legs", []):
        sel, mkt = leg.get("selection") or "?", leg.get("market") or ""
        odds = leg.get("odds")
        mark = {"won": " ✓", "lost": " ✗", "void": " (void)"}.get(leg.get("result"), "")
        odds_s = f' <span class="odds">@ {odds}</span>' if odds else ""
        out.append(f"{esc(sel)}{' — ' + esc(mkt) if mkt else ''}{odds_s}{mark}")
    return out


def short_desc(b):
    if b.get("fixture"):
        return b["fixture"]
    legs = b.get("legs", [])
    if legs:
        return " + ".join(leg.get("selection") or "?" for leg in legs)
    return (b.get("notes") or "")[:60]


def build_chart(bets):
    """Cumulative P/L per era, sequential x; returns (svg_html, points_json, table_rows)."""
    settled = sorted([b for b in bets if b["status"] in SETTLED], key=lambda b: (b["date"], b["id"]))
    series, table_rows = [], []
    for era, color_var in ((1, "--mark-era1"), (2, "--mark-era2")):
        cum, pts = 0.0, []
        for b in [x for x in settled if x["era"] == era]:
            pl = (b.get("return") or 0) - b["stake"]
            cum += pl
            pts.append({"bet": b, "pl": pl, "cum": cum})
            table_rows.append((b, pl, cum))
        if pts:
            series.append((era, color_var, pts))
    if not series:
        return "<p class='sec-note'>No settled bets yet.</p>", "[]", []

    n = sum(len(s[2]) for s in series)
    all_cum = [p["cum"] for s in series for p in s[2]] + [0.0]
    lo, hi = min(all_cum), max(all_cum)
    span = max(hi - lo, 10.0)
    lo, hi = lo - span * 0.12, hi + span * 0.12
    xw = SVG_W - PAD_L - PAD_R
    yh = SVG_H - PAD_T - PAD_B

    def X(i):
        return PAD_L + (i + 0.5) / max(n, 1) * xw

    def Y(v):
        return PAD_T + (hi - v) / (hi - lo) * yh

    grid, step = [], max(round(span / 3 / 10) * 10, 10)
    g = (int(lo // step)) * step
    while g <= hi:
        yy = Y(g)
        if PAD_T <= yy <= SVG_H - PAD_B:
            dash = "" if g == 0 else ' stroke-dasharray="2 4"'
            w = "1.4" if g == 0 else "1"
            op = "0.8" if g == 0 else "0.45"
            grid.append(
                f'<line x1="{PAD_L}" y1="{yy:.1f}" x2="{SVG_W - PAD_R}" y2="{yy:.1f}" '
                f'stroke="var(--line)" stroke-width="{w}" opacity="{op}"{dash}/>'
                f'<text x="{PAD_L - 8}" y="{yy + 3.5:.1f}" text-anchor="end">{("−" if g < 0 else "+") + "£" + str(abs(int(g))) if g else "£0"}</text>'
            )
        g += step

    idx, paths, dots, labels, js_pts, dividers = 0, [], [], [], [], []
    for era, cvar, pts in series:
        if idx > 0:
            dx = X(idx - 0.5)
            dividers.append(
                f'<line x1="{dx:.1f}" y1="{PAD_T}" x2="{dx:.1f}" y2="{SVG_H - PAD_B}" stroke="var(--ink-3)" stroke-width="1" stroke-dasharray="4 4" opacity="0.5"/>'
                f'<text x="{dx + 5:.1f}" y="{PAD_T + 10}" opacity="0.9">era {era}</text>'
            )
        d = f"M {X(idx) - 0.5 / max(n,1) * xw:.1f} {Y(0):.1f}"
        for j, p in enumerate(pts):
            x, y = X(idx + j), Y(p["cum"])
            d += f" H {x:.1f} V {y:.1f}"
            b = p["bet"]
            dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="var({cvar})" stroke="var(--surface)" stroke-width="2"/>')
            js_pts.append({
                "x": round(x, 1),
                "t": f"#{b['id']} · {esc(short_desc(b))}",
                "d": b["date"],
                "pl": money(p["pl"], signed=True),
                "cum": money(p["cum"], signed=True),
            })
        paths.append(f'<path d="{d}" fill="none" stroke="var({cvar})" stroke-width="2" stroke-linejoin="round"/>')
        end_x, end_y = X(idx + len(pts) - 1), Y(pts[-1]["cum"])
        labels.append(
            f'<text class="dlabel" x="{end_x + 10:.1f}" y="{end_y + 4:.1f}" fill="var({cvar})" style="fill:var({cvar})">{money(pts[-1]["cum"], signed=True)}</text>'
        )
        idx += len(pts)

    svg = (
        f'<svg id="ledger" viewBox="0 0 {SVG_W} {SVG_H}" width="100%" role="img" '
        f'aria-label="Cumulative profit and loss across settled bets, by era">'
        + "".join(grid) + "".join(dividers) + "".join(paths) + "".join(dots) + "".join(labels)
        + f'<line id="cross" x1="0" y1="{PAD_T}" x2="0" y2="{SVG_H - PAD_B}" stroke="var(--ink-3)" stroke-width="1" opacity="0.6" style="display:none"/>'
        + "</svg>"
    )
    return svg, json.dumps(js_pts), table_rows


def pill(b):
    s = b["status"]
    if s == "won":
        return '<span class="pill won">WON</span>'
    if s == "lost":
        return '<span class="pill lost">LOST</span>'
    if s in OPEN:
        return f'<span class="pill openb">{"PLACED" if s == "placed" else "RECOMMENDED"}</span>'
    return f'<span class="pill other">{s.replace("_", " ").upper()}</span>'


def render(bets, bank):
    era2 = next(e for e in bank["eras"] if e["era"] == 2)
    era1 = next(e for e in bank["eras"] if e["era"] == 1)
    e2_settled = [b for b in bets if b["era"] == 2 and b["status"] in SETTLED]
    e2_money = [b for b in e2_settled if b["stake"] > 0]
    e2_paper = [b for b in e2_settled if b["stake"] == 0]
    rec = lambda g: f"{sum(1 for b in g if b['status']=='won')}–{sum(1 for b in g if b['status']=='lost')}"
    net2 = era2["net"]
    hero_cls = "pos" if net2 > 0 else ("neg" if net2 < 0 else "")

    open_bets = [b for b in bets if b["status"] in OPEN]
    open_cards = []
    for b in open_bets:
        paper = b["stake"] == 0
        legs = "".join(f"<li>{l}</li>" for l in legs_lines(b))
        stake_line = ("PAPER — £0 staked" if paper else f"{money(b['stake'])} @ {b.get('odds') or '?'}")
        open_cards.append(
            f'<div class="bet-card"><div class="top"><span class="tag">{esc(b["type"])}</span>'
            + (f'<span class="tag paper">paper</span>' if paper else "")
            + f'<span class="game">{esc(short_desc(b))}</span>'
            + f'<span style="margin-left:auto" class="odds">{stake_line}</span></div>'
            + f"<ol>{legs}</ol>"
            + (f'<div class="cond">{esc(b.get("conditions"))}</div>' if b.get("conditions") else "")
            + "</div>"
        )
    open_html = "".join(open_cards) or '<p class="sec-note">No open bets. The next card lands with the morning research run (~9:00 UK).</p>'

    chart_svg, pts_json, hist = build_chart(bets)

    rows = []
    for b, pl, cum in sorted(hist, key=lambda r: (r[0]["date"], r[0]["id"]), reverse=True):
        chips = ""
        if not b.get("planned"):
            chips += '<span class="chip">unplanned</span>'
        if b["era"] == 2 and b["stake"] == 0:
            chips += '<span class="chip paper">paper</span>'
        pl_cls = "pl-pos" if pl > 0 else ("pl-neg" if pl < 0 else "")
        rows.append(
            f'<tr><td class="num">{b["id"]}</td><td class="num">{b["date"]}</td>'
            f'<td class="desc">{esc(short_desc(b))}{chips}<div class="sub">{esc(b["type"])} · era {b["era"]}</div></td>'
            f'<td class="num">{money(b["stake"])}</td><td class="num">{b.get("odds") or "?"}</td>'
            f'<td>{pill(b)}</td><td class="num">{money(b.get("return") or 0)}</td>'
            f'<td class="num"><span class="{pl_cls}">{money(pl, signed=True)}</span></td></tr>'
        )
    for b in open_bets:
        paper_chip = "" if b["stake"] else '<span class="chip paper">paper</span>'
        rows.insert(0,
            f'<tr><td class="num">{b["id"]}</td><td class="num">{b["date"]}</td>'
            f'<td class="desc">{esc(short_desc(b))}{paper_chip}<div class="sub">{esc(b["type"])} · era {b["era"]}</div></td>'
            f'<td class="num">{money(b["stake"])}</td><td class="num">{b.get("odds") or "?"}</td>'
            f'<td>{pill(b)}</td><td class="num">—</td><td class="num">—</td></tr>'
        )

    gen_at = datetime.now(timezone.utc).strftime("%d %b %Y, %H:%M UTC")
    free_bets = "".join(
        f"<p>Free bet: {money(fb['amount'])} — {esc(fb['source'])} — {esc(fb['status'])}</p>"
        for fb in bank.get("free_bets", [])
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Settling Room</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Libre+Franklin:wght@400;500;600;700&family=Spline+Sans+Mono:wght@400;500&display=swap">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
  <p class="eyebrow">The Settling Room · Era 2 · daily-stake era</p>
  <h1 class="hero-num {hero_cls}">{money(net2, signed=True)}</h1>
  <p class="hero-sub">Era-2 net since 27 Aug 2026 · staked <strong>{money(era2["staked"])}</strong> · returned <strong>{money(era2["returned"])}</strong> · money record <strong>{rec(e2_money)}</strong>{f' · paper record <strong>{rec(e2_paper)}</strong>' if e2_paper else ""}</p>
  <div class="tiles">
    <div class="tile"><div class="k">Daily ceilings</div><div class="v">£10 + £10 <small>acca / builder</small></div></div>
    <div class="tile"><div class="k">Circuit breaker</div><div class="v">−£100 <small>pause + review</small></div></div>
    <div class="tile"><div class="k">Era 1 (closed)</div><div class="v">{money(era1["net"], signed=True)} <small>15–24 Aug</small></div></div>
    <div class="tile"><div class="k">Era 1 planned bets</div><div class="v">+£33.40 <small>vs −£40 unplanned</small></div></div>
  </div>

  <h2>Today's card</h2>
  <p class="sec-note">Recommendations become live bets only when the slip is confirmed; conditions are binding.</p>
  <div class="cards">{open_html}</div>

  <h2>The ledger</h2>
  <p class="sec-note">Cumulative P/L per era — each era measured from its own £0. Hover for the bet behind each step.</p>
  <div class="chart-box" id="chartbox">
    <div class="legend">
      <span><span class="sw" style="background:var(--mark-era1)"></span>Era 1 · weekly caps</span>
      <span><span class="sw" style="background:var(--mark-era2)"></span>Era 2 · daily £10+£10</span>
    </div>
    {chart_svg}
    <div id="tip"></div>
  </div>

  <h2>Every bet</h2>
  <p class="sec-note">Newest first. Returns are slip figures where confirmed; paper picks carry £0 stakes.</p>
  <div class="table-scroll"><table>
    <thead><tr><th class="num">#</th><th class="num">Date</th><th>Bet</th><th class="num">Stake</th><th class="num">Odds</th><th>Result</th><th class="num">Return</th><th class="num">P/L</th></tr></thead>
    <tbody>{"".join(rows)}</tbody>
  </table></div>

  <footer>
    <p>Rules live in STRATEGY.md; daily reasoning in picks/. Regenerated automatically after every research and settlement run · last: {gen_at}.</p>
    {free_bets}
    <p>Ceilings are ceilings, not quotas — NO BET days stake £0. If it stops being fun, stop: GamCare 0808 8020 133 · gamcare.org.uk.</p>
  </footer>
</div>
<script type="application/json" id="pts">{pts_json}</script>
<script>var SVG_W = {SVG_W};{JS}</script>
</body>
</html>
"""


def main():
    bets = json.loads((ROOT / "data" / "bets.json").read_text())["bets"]
    bank = json.loads((ROOT / "data" / "bankroll.json").read_text())
    (ROOT / "dashboard.html").write_text(render(bets, bank))
    print("dashboard.html regenerated.")


if __name__ == "__main__":
    main()
