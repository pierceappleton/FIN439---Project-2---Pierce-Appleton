# Investment App for a Committee Adoption

## Repository Content

- Repository root: Contains `portfolio.py`, `analysis.py`, `app.py`, `run_baseline.py`, `requirements.txt`, and this README.
- `data/`: Holds the monthly adjusted prices for the funds (BIL, IEF, LQD, and VT) from Oct 2021 to Sep 2026, along with the source link and download date.
- `docs/`: Includes the decision memo, validation record, cold-run notes, and data card.
- `output/`: Stores the generated outputs from the app, such as the baseline report, cost-comparison reports, and stress run details.
- `tests/`: Contains the verification script.

## Usage Instructions (Windows)

Run these commands in PowerShell. Git and Python 3.10 or newer must be installed. The commands use the virtual environment directly, so activation is not required.

1. Clone the repository into a directory where you have write permissions, then enter the repository folder:

   ```powershell
   git clone https://github.com/pierceappleton/FIN439-Project-2.git
   cd FIN439-Project-2
   ```

2. Create the virtual environment:

   ```powershell
   python -m venv .venv
   ```

3. Install the required dependencies:

   ```powershell
   .\.venv\Scripts\python -m pip install -r requirements.txt
   ```

4. Run the baseline and cost-comparison reports:

   ```powershell
   .\.venv\Scripts\python run_baseline.py
   .\.venv\Scripts\python run_baseline.py --changed-input
   ```

5. Verify the calculations and saved results:

   ```powershell
   .\.venv\Scripts\python tests/verify.py
   ```

6. Start the Streamlit app:

   ```powershell
   .\.venv\Scripts\python -m streamlit run app.py
   ```

7. Open http://localhost:8501 to adjust the parameters and observe the results. Keep the terminal open while using the app.

## Files

| File | Role |
| --- | --- |
| `portfolio.py` | Risk engine that estimates returns, volatilities, and correlations, and performs a grid search for the lowest-volatility mix that meets the return objective and reserve minimum. |
| `analysis.py` | Generates the baseline portfolios (equal weight, inverse volatility, and constrained minimum variance) and checks each against the five rules: fully invested, long-only, net return, reserve, and liquidity. |
| `app.py` | Streamlit app that allows users to adjust parameters such as the objective, reserve minimum, cost allowance, 36-month window, and return estimates for each fund. It displays the portfolios' weights, returns, volatilities, and pass/fail verdicts per rule. |
| `run_baseline.py` | Single command to generate the baseline report. Adding `--changed-input` generates both cost-comparison files. |
| `tests/verify.py` | Performs four tests: verifying the volatility calculation, checking for infeasible mixes, verifying input validation, and ensuring reproducibility. |
| `data/prices.csv` | Contains the monthly adjusted prices for BIL, IEF, LQD, and VT from Oct 2021 to Sep 2026. The source link and download date are provided in `data/prices-sources.json`. |
| `docs/` | Includes the decision memo, validation record, cold-run notes, and data card. |

## Mandate

- Fictional education foundation with a $100M endowment.
- Seven-year horizon with annual rebalancing.
- Targeting a net return of CPI + 4% annually, modeled as a 6.5% nominal return and a CPI of 2.5%.
- Long-only and fully invested with at least 3% invested in BIL or IEF.
- 90% of the portfolio must be liquid within five days.
- The calendar-year loss limit is undefined, requiring CIO clarification, so it is never marked as pass.

## AI Policy Compliance

- AI is required and expected for this project.
- Both Claude Code and ChatGPT (Codex) were used to assist in writing, debugging, and testing code. The AI-use record is included in `docs/validation-and-ai-use.md`.
- The Locked Changed-Input Record prediction was written before running the app with AI closed. The app was run with AI closed as well.

## Known Gaps

- The calendar-year loss limit is undefined, requiring CIO clarification.

## Note

This investment app is meant for educational purposes and should not be used for actual investment decisions.
