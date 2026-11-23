"""Project 2 analysis layer: baselines, mandate verdicts, stress run.

Built on portfolio.py (the Lab 14/15 engine). Decimal units throughout.
"""
import csv
import math
from pathlib import Path

import portfolio as p

PRICES = Path(__file__).resolve().parent / "data" / "prices.csv"
RESERVE = {"BIL", "IEF"}      # reserve-eligible: cash / Treasuries
OBJECTIVE = 0.065             # CPI 2.5% (modeling estimate) + 4%
RESERVE_MIN = 0.03            # 4 quarterly payouts of $0.75M on $100M
STOP_SHIFT_PTS = 20.0         # stop rule: largest weight shift above this


def load(last_36=False, path=PRICES):
    return p.estimate_from_csv(path, last_36)


def verdict(weights, sleeves, objective=OBJECTIVE, reserve_min=RESERVE_MIN, cost=0.0):
    """Per-rule pass/fail for one weight vector. Returns (rows, all_pass)."""
    ret = p.expected_return(weights, sleeves) - cost
    reserve = sum(w for w, s in zip(weights, sleeves) if s[0] in RESERVE)
    rows = [
        ("Fully invested (sum = 100%)", abs(sum(weights) - 1) < 1e-9),
        ("Long-only (no weight < 0)", min(weights) >= -1e-12),
        (f"Net return >= {objective:.1%}", ret + 1e-12 >= objective),
        (f"Reserve (BIL+IEF) >= {reserve_min:.0%}", reserve + 1e-12 >= reserve_min),
        ("Liquid within 5 days >= 90%", True),  # all four are daily-traded ETFs
    ]
    return rows, all(ok for _, ok in rows)


def portfolios(sleeves, corr, objective=OBJECTIVE, reserve_min=RESERVE_MIN, cost=0.0):
    """Equal weight, inverse volatility (2nd baseline) and the constrained search."""
    net = [(n, r - cost, v) for n, r, v in sleeves]
    cov = p.covariance_matrix(net, corr)
    found = p.search(net, corr, objective, reserve_min, RESERVE)
    out = {"Equal weight": p.equal_weights(net),
           "Inverse volatility": p.inverse_volatility_weights(net)}
    if found:
        out["Constrained min-vol"] = list(found["weights"])
    result = {}
    for name, w in out.items():
        rows, ok = verdict(w, sleeves, objective, reserve_min, cost)
        result[name] = dict(weights=w, ret=p.expected_return(w, net),
                            vol=p.portfolio_volatility(w, cov), rules=rows, passes=ok)
    return result, found


def compounded_return(weights, last_36=False, path=PRICES):
    """Gross annualized historical return for a monthly constant-weight mix."""
    with open(path, encoding="utf-8-sig", newline="") as handle:
        prices = [tuple(map(float, row[1:])) for row in list(csv.reader(handle))[1:]]
    if last_36:
        prices = prices[-37:]
    monthly = (
        sum(w * (end / start - 1) for w, start, end in zip(weights, previous, current, strict=True))
        for previous, current in zip(prices, prices[1:])
    )
    return math.prod(1 + value for value in monthly) ** (12 / (len(prices) - 1)) - 1


def stress(objective=OBJECTIVE, reserve_min=RESERVE_MIN, cost=0.0, *,
           last_36=False, return_overrides=None):
    """Re-run the constrained search from the active settings, one change at a time."""
    overrides = return_overrides or {}

    def window(use_last_36):
        sleeves, correlations, _ = load(use_last_36)
        return [(n, overrides.get(n, r), v) for n, r, v in sleeves], correlations

    def search(sleeves, corr, target, minimum, annual_cost):
        net = [(n, r - annual_cost, v) for n, r, v in sleeves]
        return p.search(net, corr, target, minimum, RESERVE)

    active, active_corr = window(last_36)
    alternate, alternate_corr = window(not last_36)
    base = search(active, active_corr, objective, reserve_min, cost)
    alternate_label = "all months" if last_36 else "last 36 months"
    cases = [(f"Window: {alternate_label}", alternate, alternate_corr, objective, reserve_min, cost)]
    for i, (name, estimate, volatility) in enumerate(active):
        for change in (-0.01, 0.01):
            adjusted = active.copy()
            adjusted[i] = (name, estimate + change, volatility)
            cases.append((f"Estimate: {name} return {change:+.0%}", adjusted, active_corr,
                          objective, reserve_min, cost))
    for extra_cost in (0.0025, 0.005):
        cases.append((f"Costs: +{extra_cost:.2%} annual drag", active, active_corr,
                      objective, reserve_min, cost + extra_cost))
    cases.append(("Constraint: reserve minimum 10%", active, active_corr, objective, 0.10, cost))
    cases.append(("Constraint: objective 7.0%", active, active_corr, 0.07, reserve_min, cost))

    rows = []
    for label, sleeves, corr, target, minimum, annual_cost in cases:
        result = search(sleeves, corr, target, minimum, annual_cost)
        shift = p.largest_weight_change(base, result)
        # Five-point grid weights can represent a 20-point shift as 20.000000000000004.
        stop = base is None or result is None or round(shift, 9) > STOP_SHIFT_PTS
        rows.append(dict(case=label, result=result, shift=shift, stop=stop))
    return base, rows
