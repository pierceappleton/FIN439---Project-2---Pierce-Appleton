# Data Card

| Item | Entry |
|---|---|
| Price data | Yahoo monthly adjusted close, BIL, IEF, LQD, VT. Downloaded 2026-10-20. See [prices-sources.json](../data/prices-sources.json). |
| Price data limitations | The provider can revise adjusted prices. First-of-month dates label monthly observations. The price file is a single download, so historical price revisions cannot be reconstructed. |
| Point-in-time signal | Lab 17 series **GS10**, monthly 10-year U.S. Treasury constant-maturity yield, percent, not seasonally adjusted. Source is the Federal Reserve Board's H.15 release via [ALFRED](https://alfred.stlouisfed.org/release?et=&pageID=1&rd=2026-10-02&rid=18&t=). |
| Observation | September 2026 (series label 2026-09-01), **4.99%**. The date labels the monthly average. |
| As-of date and vintage | As of the close of **2026-10-02**, using the archived H.15 snapshot dated **2026-10-02**. Use only observations published by the review cutoff. The September monthly yield could not be used for a decision dated September 1. |
| Retrieval timestamp | 2026-11-22 at 21:26 UTC, from the dated ALFRED release. |
| Decision rule | As a one-input sensitivity check, enter the latest GS10 value available in the dated vintage as the gross IEF return assumption. Hold risk estimates and all other inputs fixed. Keep the allocation on hold if this makes the grid infeasible or moves any weight more than 20 percentage points. GS10 is a yield proxy for this check. IEF's total return also depends on rate moves, duration and expenses. |
| Result for this snapshot | At the default settings (all months, 6.50% objective, 3.00% reserve, 0.00% cost), entering 4.99% for IEF leaves the allocation at 60% BIL and 40% VT, a zero-point shift. The window sensitivity still triggers a stop. |
