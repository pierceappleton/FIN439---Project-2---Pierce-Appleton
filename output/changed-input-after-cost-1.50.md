# Changed-input test: annual cost allowance 1.50%

Education, not investment advice. Run date 2026-11-22.

Settings: objective 8.50%, reserve minimum 1.00%, annual cost allowance 1.50%, last 36 months (36 monthly returns, 2023-09-01 to 2026-09-01).

Weights order: BIL / IEF / LQD / VT (%).

| Portfolio | Weights | Net return | Volatility | Mandate |
|---|---|---:|---:|---|
| Equal weight | 25.0 / 25.0 / 25.0 / 25.0 | 6.63% | 5.88% | FAIL: Net return >= 8.5% |
| Inverse volatility | 92.8 / 3.0 / 2.5 / 1.7 | 3.11% | 0.61% | FAIL: Net return >= 8.5% |
| Constrained min-vol | 60.0 / 0.0 / 0.0 / 40.0 | 9.22% | 4.70% | PASS |

PASS covers the modeled checks. The calendar-year loss limit (S9) requires CIO clarification.

The constrained mix's gross compounded historical return was 11.14% annualized, using constant weights reset monthly and multiplying monthly portfolio growth factors. This illustration excludes costs and differs from the tool's annual rebalancing mandate. The optimizer uses arithmetic annualization (12 × mean monthly return) less the annual cost allowance. The compounded figure does not determine the mandate verdict.

## Stress run (constrained min-vol, one change at a time)

| Case | Weights | Shift (pts) | Stop? |
|---|---|---:|---|
| Base (last 36 months) | 60 / 0 / 0 / 40 | 0 | no |
| Window: all months | 10 / 0 / 0 / 90 | 50 | STOP |
| Estimate: BIL return -1% | 60 / 0 / 0 / 40 | 0 | no |
| Estimate: BIL return +1% | 65 / 0 / 0 / 35 | 5 | no |
| Estimate: IEF return -1% | 60 / 0 / 0 / 40 | 0 | no |
| Estimate: IEF return +1% | 60 / 0 / 0 / 40 | 0 | no |
| Estimate: LQD return -1% | 60 / 0 / 0 / 40 | 0 | no |
| Estimate: LQD return +1% | 55 / 0 / 10 / 35 | 10 | no |
| Estimate: VT return -1% | 60 / 0 / 0 / 40 | 0 | no |
| Estimate: VT return +1% | 65 / 0 / 0 / 35 | 5 | no |
| Costs: +0.25% annual drag | 60 / 0 / 0 / 40 | 0 | no |
| Costs: +0.50% annual drag | 60 / 0 / 0 / 40 | 0 | no |
| Constraint: reserve minimum 10% | 60 / 0 / 0 / 40 | 0 | no |
| Constraint: objective 7.0% | 70 / 0 / 0 / 30 | 10 | no |

Cost shocks add to the stated annual allowance. The window case re-estimates returns and risk, holding the objective, reserve minimum and cost allowance fixed.

Stop if the base or a scenario is infeasible, or any weight moves more than 20 points under one change.
