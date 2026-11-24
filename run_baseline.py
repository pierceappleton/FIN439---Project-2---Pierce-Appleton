"""Write reproducible baseline and changed-input reports under output/."""
import argparse
from datetime import date
from pathlib import Path

import analysis as a

OUTPUT = Path(__file__).resolve().parent / "output"
NAMES = ("BIL", "IEF", "LQD", "VT")


def fmt_w(weights, decimals=0):
    return " / ".join(f"{value * 100:.{decimals}f}" for value in weights)


def report(title, *, objective, reserve_min, cost, last_36):
    sleeves, corr, meta = a.load(last_36)
    portfolios, found = a.portfolios(sleeves, corr, objective, reserve_min, cost)
    window = "last 36 months" if last_36 else "all months"
    out = [f"# {title}", "",
           f"Education, not investment advice. Run date {date.today()}.", "",
           f"Settings: objective {objective:.2%}, reserve minimum {reserve_min:.2%}, "
           f"annual cost allowance {cost:.2%}, {window} "
           f"({meta['returns']} monthly returns, {meta['start']} to {meta['end']}).", "",
           f"Weights order: {' / '.join(NAMES)} (%).", "",
           "| Portfolio | Weights | Net return | Volatility | Mandate |",
           "|---|---|---:|---:|---|"]
    for name, result in portfolios.items():
        failed = [rule for rule, ok in result["rules"] if not ok]
        mandate = "PASS" if result["passes"] else "FAIL: " + ", ".join(failed)
        out.append(f"| {name} | {fmt_w(result['weights'], 1)} | {result['ret']:.2%} | "
                   f"{result['vol']:.2%} | {mandate} |")
    out += ["", "PASS covers the modeled checks. The calendar-year loss limit (S9) "
                "requires CIO clarification.", ""]
    if found is not None:
        gross = a.compounded_return(found["weights"], last_36)
        out += [f"The constrained mix's gross compounded historical return was {gross:.2%} "
                "annualized, using constant weights reset monthly and multiplying monthly "
                "portfolio growth factors. This illustration excludes costs and differs "
                "from the tool's annual rebalancing mandate. The optimizer uses arithmetic "
                "annualization (12 × mean monthly return) less the annual cost allowance. "
                "The compounded figure does not determine the mandate verdict.", ""]
    out += ["## Stress run (constrained min-vol, one change at a time)", "",
            "| Case | Weights | Shift (pts) | Stop? |", "|---|---|---:|---|"]
    base, rows = a.stress(objective, reserve_min, cost, last_36=last_36)
    weights = fmt_w(base["weights"]) if base else "infeasible"
    out.append(f"| Base ({window}) | {weights} | {'0' if base else 'n/a'} | {'no' if base else 'STOP'} |")
    for row in rows:
        weights = fmt_w(row["result"]["weights"]) if row["result"] else "infeasible"
        shift = "n/a" if row["shift"] is None else f"{row['shift']:.0f}"
        out.append(f"| {row['case']} | {weights} | {shift} | {'STOP' if row['stop'] else 'no'} |")
    out += ["", "Cost shocks add to the stated annual allowance. The window case re-estimates "
                "returns and risk, holding the objective, reserve minimum and cost allowance fixed.", "",
            f"Stop if the base or a scenario is infeasible, or any weight moves more than "
            f"{a.STOP_SHIFT_PTS:.0f} points under one change."]
    return "\n".join(out) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--changed-input", action="store_true",
                        help="regenerate both locked cost-comparison reports")
    if parser.parse_args().changed_input:
        for label, cost in (("before", 0.01), ("after", 0.015)):
            output = OUTPUT / f"changed-input-{label}-cost-{cost * 100:.2f}.md"
            text = report(f"Changed-input test: annual cost allowance {cost:.2%}",
                          objective=0.085, reserve_min=0.01, cost=cost, last_36=True)
            output.write_text(text, encoding="utf-8")
            print(output.relative_to(OUTPUT.parent))
        return
    text = report("Baseline output", objective=a.OBJECTIVE, reserve_min=a.RESERVE_MIN,
                  cost=0.0, last_36=False)
    (OUTPUT / "baseline-output.md").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
