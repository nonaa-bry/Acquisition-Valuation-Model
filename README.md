# Acquisition Valuation Model

A Python-based acquisition valuation model for 5 major alternative asset managers:
**Blackstone, BlackRock, Apollo, KKR, and Ares Management**

## What It Does
- DCF Analysis: FCF projections, WACC estimation, Terminal Value
- Trading Comparables: EV/EBITDA multiples across peers
- Sensitivity Analysis: EV across different WACC & terminal growth assumptions
- Visual Outputs: Valuation bridges, sensitivity heatmaps, DCF vs Comps comparison chart

## Project Structure
acquisition-valuation-model/
├── data/
│   └── financials.csv       # Revenue, EBITDA, FCF historical data
├── models/
│   ├── wacc.py              # WACC calculator using CAPM
│   ├── dcf.py               # DCF engine with terminal value
│   └── comps.py             # Trading comparables (EV/EBITDA)
├── visuals/
│   └── charts.py            # Matplotlib visualisations
└── main.py                  # Main runner
## Tech Stack
- Python 3
- pandas- financial data structuring
- NumPy- WACC, NPV computations
- Matplotlib- valuation bridges, heatmaps, comparison charts

## How to Run
```bash
pip install pandas numpy matplotlib
python main.py
```

## Methodology

**WACC** is estimated using CAPM:
- Risk Free Rate: 4.5% (10yr US Treasury)
- Equity Risk Premium: 5.5% (Damodaran)
- Cost of Debt: 6%

**DCF** uses 5-year FCF projections with Gordon Growth Model terminal value

**Comps** uses EV/EBITDA multiples benchmarked against peer transactions

## Output
Each company generates:
- `_bridge.png` — DCF valuation bridge showing FCF + terminal value breakdown
- `_sensitivity.png` — EV sensitivity across WACC and terminal growth ranges
- `dcf_vs_comps.png` — Side by side DCF vs Trading Comps for all 5 companies

## Companies Covered
| Company | Sector |
|---|---|
| Blackstone | Alternative Asset Management |
| BlackRock | Asset Management |
| Apollo | Alternative Asset Management |
| KKR | Private Equity |
| Ares Management | Alternative Credit |
