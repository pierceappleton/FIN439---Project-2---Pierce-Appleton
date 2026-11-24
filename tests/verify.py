"""Run from the repository root: python tests/verify.py."""
from io import StringIO
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import analysis as a
import portfolio as p


class PortfolioChecks(unittest.TestCase):
    def test_portfolio_volatility_by_hand(self):
        sleeves = (("A", 0.04, 0.10), ("B", 0.07, 0.20))
        covariance = p.covariance_matrix(sleeves, ((1.0, 0.5), (0.5, 1.0)))
        # Variance = 0.5² × 0.01 + 0.5² × 0.04 + 2 × 0.5² × 0.01 = 0.0175.
        self.assertAlmostEqual(p.portfolio_volatility((0.5, 0.5), covariance),
                               0.13228756555322954)

    def test_no_mix_meets_return_objective(self):
        sleeves = (("BIL", 0.02, 0.01), ("IEF", 0.03, 0.08), ("VT", 0.05, 0.15))
        correlations = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        result, found = a.portfolios(sleeves, correlations, objective=0.06)
        self.assertIsNone(found)
        self.assertNotIn("Constrained min-vol", result)

    def test_rejects_asymmetric_correlation(self):
        sleeves = (("A", 0.04, 0.10), ("B", 0.07, 0.20))
        with self.assertRaisesRegex(ValueError, "must be symmetric"):
            p.covariance_matrix(sleeves, ((1.0, 0.2), (0.5, 1.0)))

    def test_rejects_nonpositive_price(self):
        prices = StringIO("Date,BIL,IEF,VT\n2026-01-01,10,20,30\n2026-02-01,0,21,31\n"
                          "2026-03-01,12,20,32\n")
        with self.assertRaisesRegex(ValueError, "Prices must be positive and finite"):
            p.estimate_from_csv(prices)


def verify_saved_results():
    sleeves, corr, meta = a.load()
    res, found = a.portfolios(sleeves, corr)
    assert meta["prices"] == 60 and meta["returns"] == 59, meta
    assert [round(w * 100) for w in found["weights"]] == [60, 0, 0, 40]
    assert res["Constrained min-vol"]["passes"]
    assert not res["Equal weight"]["passes"] and not res["Inverse volatility"]["passes"]
    _, rows = a.stress()
    last = next(row for row in rows if row["case"] == "Window: last 36 months")
    assert round(last["shift"]) == 25 and last["stop"]

    sleeves, corr, _ = a.load(True)
    for cost, shift in ((0.01, 45), (0.015, 50)):
        _, found = a.portfolios(sleeves, corr, 0.085, 0.01, cost)
        base, rows = a.stress(0.085, 0.01, cost, last_36=True)
        assert base == found
        assert rows[0]["case"] == "Window: all months"
        assert round(rows[0]["shift"]) == shift and rows[0]["stop"]


if __name__ == "__main__":
    verify_saved_results()
    program = unittest.main(exit=False)
    if not program.result.wasSuccessful():
        raise SystemExit(1)
    print("All checks passed.")
