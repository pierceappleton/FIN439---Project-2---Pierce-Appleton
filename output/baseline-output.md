# Baseline output

Education, not investment advice. Run date 2026-11-22.

Settings: objective 6.50%, reserve minimum 3.00%, annual cost allowance 0.00%, all months (59 monthly returns, 2021-10-01 to 2026-09-01).

Weights order: BIL / IEF / LQD / VT (%).

| Portfolio | Weights | Net return | Volatility | Mandate |
|---|---|---:|---:|---|
| Equal weight | 25.0 / 25.0 / 25.0 / 25.0 | 3.01% | 7.55% | FAIL: Net return >= 6.5% |
| Inverse volatility | 87.2 / 5.5 / 4.3 / 2.9 | 3.37% | 1.37% | FAIL: Net return >= 6.5% |
| Constrained min-vol | 60.0 / 0.0 / 0.0 / 40.0 | 6.61% | 6.05% | PASS |

PASS covers the modeled checks. The calendar-year loss limit (S9) requires CIO clarification.

The constrained mix's gross compounded historical return was 6.63% annualized, using constant weights reset monthly and multiplying monthly portfolio growth factors. This illustration excludes costs and differs from the tool's annual rebalancing mandate. The optimizer uses arithmetic annualization (12 × mean monthly return) less the annual cost allowance. The compounded figure does not determine the mandate verdict.

## Stress run (constrained min-vol, one change at a time)

| Case | Weights | Shift (pts) | Stop? |
|---|---|---:|---|
| Base (all months) | 60 / 0 / 0 / 40 | 0 | no |
| Window: last 36 months | 85 / 0 / 0 / 15 | 25 | STOP |
| Estimate: BIL return -1% | 50 / 0 / 0 / 50 | 10 | no |
| Estimate: BIL return +1% | 70 / 0 / 0 / 30 | 10 | no |
| Estimate: IEF return -1% | 60 / 0 / 0 / 40 | 0 | no |
| Estimate: IEF return +1% | 60 / 0 / 0 / 40 | 0 | no |
| Estimate: LQD return -1% | 60 / 0 / 0 / 40 | 0 | no |
| Estimate: LQD return +1% | 60 / 0 / 0 / 40 | 0 | no |
| Estimate: VT return -1% | 55 / 0 / 0 / 45 | 5 | no |
| Estimate: VT return +1% | 65 / 0 / 0 / 35 | 5 | no |
| Costs: +0.25% annual drag | 55 / 0 / 0 / 45 | 5 | no |
| Costs: +0.50% annual drag | 50 / 0 / 0 / 50 | 10 | no |
| Constraint: reserve minimum 10% | 60 / 0 / 0 / 40 | 0 | no |
| Constraint: objective 7.0% | 50 / 0 / 0 / 50 | 10 | no |

Cost shocks add to the stated annual allowance. The window case re-estimates returns and risk, holding the objective, reserve minimum and cost allowance fixed.

Stop if the base or a scenario is infeasible, or any weight moves more than 20 points under one change.
