# Validation and AI Use

## AI-use record

Every AI output was reviewed by me and occasionally cross-referenced with the other AI models used (Codex/Claude Code).

| *Tool* | *Use* |
| ----- | ----- |
| Claude Code | Helped scaffold the original code and drafts, which I subsequently reviewed, and described what the prediction record should contain. |
| ChatGPT (Codex) | Helped revise the stress code, reports, tests, memo, and disclosure, and compared the rerun results with the locked prediction. I checked the dated GS10 value against ALFRED. |

## Checked AI output

The Claude-assisted cost comparison showed a 40-point window stress in both cost reports. For this revision, I verified the window case directly by solving the full-history and 36-month portfolios at each cost, holding the 8.50% objective and 1.00% reserve fixed. At 1.00% cost, the BIL weight moves from 65% to 20%, a 45-point shift. At 1.50% cost it moves from 60% to 10%, a 50-point shift. The original stress calculation used a zero-cost, full-history starting point. The corrected reports use each run's active settings and still trigger STOP.

**Disposition.** I rejected the original 40-point result for both runs. After checking each run with its own cost and window settings, I accepted the corrected shifts of 45 percentage points at 1.00% cost and 50 percentage points at 1.50% cost. Both trigger the STOP rule.

## Baseline and mandate check

Run `python run_baseline.py` to reproduce the [saved baseline](../output/baseline-output.md). Regenerate both cost reports with `python run_baseline.py --changed-input`. Checks: `python tests/verify.py`.

## Stress run

Each report varies the price window, each asset's return estimate by ±1 point, annual costs by +0.25 or +0.50 points, the reserve minimum, and the objective one at a time. The window case recalculates historical estimates and risk for the alternate window and retains any manual expected-return assumptions. Stop if the base or any scenario is infeasible or a weight moves more than 20 points.

## Locked Changed-Input Record

## Original prediction

*Changed-Input Prediction Commitment:*
- Scenario Tested: Increasing the annual cost allowance from 1.00% to 1.50% per year, holding the 8.50% objective, 1.00% reserve minimum, last-36-month window, and asset return estimates unchanged.
- Expected Impact on Allocation: Allocation will remain unchanged because the annual cost allowance applies a uniform annual return deduction across all asset classes without introducing separate trading transaction costs or altering the relative covariance and return structure that drives the optimizer's weights.
- Expected Impact on Performance & Mandate Verdicts: Estimated net return will decrease (referring to the new allocation selected by the optimizer), while volatility will stay roughly unchanged due to fixed underlying asset proportions and risk parameters.
- Recommendation Verdict: Recommendation will remain to reject live allocation because this cost sensitivity test measures fee drag rather than resolving the core governance gaps, missing mandate rules (like the undefined calendar-year loss limit), lack of CIO sign-off, or the previously triggered stress stop.

| *Field* | *Entry* |
| ----- | ----- |
| Timestamp / commit | Prediction committed 2026-11-17 18:20 -05:00 in [commit 55a397a](https://github.com/pierceappleton/FIN439-Project-2/commit/55a397a04466f99d0c90e736cf4d85fd4425166e), before the rerun |
| Load-bearing input | Annual cost allowance |
| Old value -> new value, with units | 1.00% per year -> 1.50% per year (objective 8.50%, reserve minimum 1.00%, last-36-month window held fixed) |
| Expected direction of decision numbers | See the prediction above: allocation unchanged, net return down, volatility roughly unchanged |
| Expected effect on the decision | Recommendation stays reject |

## After the run

**AI-Closed:** The before and after outputs below were generated directly by the deterministic engine (`python run_baseline.py --changed-input`) on November 22 from the same analysis functions the app uses—no AI regeneration was used to produce this record's run outputs. The initial settings for both runs were the last 36 months, an 8.50% objective and a 1.00% reserve minimum. Only the starting cost allowance changed. Each report's stress cases then changed one input relative to its own starting settings.

- Before output: [output/changed-input-before-cost-1.00.md](../output/changed-input-before-cost-1.00.md)
- After output: [output/changed-input-after-cost-1.50.md](../output/changed-input-after-cost-1.50.md)

| *Constrained min-vol* | *Before (1.00%)* | *After (1.50%)* |
| ----- | ----- | ----- |
| Weights BIL / IEF / LQD / VT (%) | 65 / 0 / 0 / 35 | 60 / 0 / 0 / 40 |
| Net return | 8.42% | 9.22% |
| Volatility | 4.12% | 4.70% |
| Mandate | PASS | PASS |

Equal weight (7.13% -> 6.63%) and inverse volatility (3.61% -> 3.11%) still FAIL on return.

| *Field* | *Entry* |
| ----- | ----- |
| Decision changed? | No. The recommendation stays reject live allocation. The constrained mix still passes the modeled return and reserve rules. The calendar-year loss limit still needs a definition, and switching to all months still triggers the stop rule at both cost levels. |
| Why prediction matched or not | The reject verdict matched. The allocation, net return and volatility predictions were wrong. Allocation moved 5 points from BIL into VT, net return rose from 8.92% to 9.22%, and volatility rose from 4.12% to 4.70%. |

*Why.* The net-return constraint binds. At 1.50% cost, the old 65/35 mix nets 8.42% and falls short of the 8.50% objective. The optimizer moves one five-point grid step into VT, landing at 60/40 with a 9.22% net estimate and higher volatility. The larger VT weight raises the estimate enough to offset the additional cost. The prediction assumed the cost increase would leave the allocation fixed.

## Second baseline

Inverse volatility gives lower-volatility sleeves more weight using only each sleeve's standalone risk estimate. It is a comparison for the constrained search, which also accounts for covariance and screens against the mandate. Here the inverse-volatility mix meets the modeled reserve rule and misses the return objective.
