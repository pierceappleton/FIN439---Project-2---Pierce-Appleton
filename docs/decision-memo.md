# Decision Memo: Meridian Foundation

**Education, not investment advice.**

The analysis and the decision are mine.

**To:** Meridian Foundation Investment Committee and Chief Investment Officer (CIO)

## Decision and committee ask

**Reject live allocation under the current process.** I ask the committee to defer funding and authorize a paper pilot because changing the estimation window shifts the allocation by 25 percentage points, exceeding our 20-point stop threshold. I also ask the CIO to specify the calendar-year loss limit and approve a realistic cost allowance before the committee reviews a live allocation.

For the paper pilot, use **60%–85% BIL and 15%–40% VT**, paired to sum to 100%, with IEF and LQD at 0%. These endpoints stem from the all-month and last-36-month runs at the 6.50% objective. Begin with 60% BIL and 40% VT as the all-month reference, and track the 85% BIL and 15% VT result alongside it.

## Evidence

| Portfolio | Weights BIL/IEF/LQD/VT (%) | Net return | Volatility | Modeled mandate checks |
| --- | --- | --- | --- | --- |
| Equal weight | 25.0 / 25.0 / 25.0 / 25.0 | 3.01% | 7.55% | Fail on return |
| Inverse volatility | 87.2 / 5.5 / 4.3 / 2.9 | 3.37% | 1.37% | Fail on return |
| Constrained min-vol | 60.0 / 0.0 / 0.0 / 40.0 | 6.61% | 6.05% | Pass |

The baseline uses 59 monthly returns from prices labeled October 2021 to September 2026, a 6.50% objective, a 3% reserve minimum, and zero modeled costs. Its 6.61% estimated return uses arithmetic annualization, and the gross compounded historical illustration is 6.63% annualized with monthly weight resets, whereas live allocations would rebalance annually.

Switching to the last 36 months under baseline assumptions creates a domino effect that moves 25 points from VT to BIL and triggers the stop rule. At the locked 8.50% objective and 1% reserve minimum, switching from the last 36 months to all months causes a 45-point shift at [suspicious link removed] and a 50-point shift at [suspicious link removed]. In the baseline, a 0.50-point cost increase moves 10 points into VT, and a one-point VT estimate change moves five points.

## Monitoring and reversal

| Monitor | Trigger and action |
| --- | --- |
| VT return estimate | If an independent forward-looking estimate differs by at least 1 percentage point from the model assumption, rerun the model with the independent estimate and reapply the stop rule. |
| Net return vs. CPI + 4% | Review the annualized net return over rolling five years as data become available. A shortfall triggers committee review of the assumptions and any pilot expansion. |
| Reserve | If BIL plus IEF falls below the mandate's 3% floor, pause expansion and bring the reserve back into compliance before reconsidering. |
| Costs and turnover | If expected annual costs exceed the CIO-approved allowance, rerun with the higher estimate and reapply the stop rule. |
| 10-year Treasury yield | At each review, apply the [dated GS10 check](data-card.md) to IEF. The 4.99% snapshot leaves the baseline weights unchanged. Hold the allocation if the check becomes infeasible or shifts any weight more than 20 points. |

Reverse the rejection only after the CIO defines the calendar-year loss limit, the candidate passes that test and the other mandate checks under approved costs, and every prescribed stress remains feasible with a maximum weight shift of 20 percentage points or less. Once we gather that missing data and confirm those outcomes, bring the results back to the committee for a funding vote.
