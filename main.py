import pandas as pd
from models.wacc   import calculate_wacc
from models.dcf    import dcf_valuation
from models.comps  import comps_valuation
from visuals.charts import plot_bridge, plot_sensitivity, plot_dcf_vs_comps

# ── Load Data ─────────────────────────────────────────────────────────────────
df = pd.read_csv("data/financials.csv")

all_companies  = []
all_dcf_values = []
all_comps_values = []

print("=" * 55)
print("       ACQUISITION VALUATION MODEL")
print("=" * 55)

for _, row in df.iterrows():
    company = row["Company"]
    print(f"\n📊 {company}")
    print("-" * 40)

    # ── Inputs ────────────────────────────────────────────
    fcf_base    = row["FCF_Y3"]          # Latest FCF as base
    ebitda      = row["EBITDA_Y3"]
    beta        = row["Beta"]
    debt        = row["Debt"]
    shares      = row["Shares"]

    # Estimate market equity value (simplified: shares * assumed price $50)
    equity = shares * 50 / 1000          # Convert to $Bn

    growth_rate = (row["FCF_Y3"] - row["FCF_Y1"]) / row["FCF_Y1"] / 2   # 2yr CAGR

    # ── WACC ──────────────────────────────────────────────
    wacc = calculate_wacc(beta, debt, equity)
    print(f"  WACC            : {wacc*100:.2f}%")
    print(f"  FCF Growth Rate : {growth_rate*100:.2f}%")

    # ── DCF ───────────────────────────────────────────────
    ev_dcf, pv_fcfs, pv_terminal = dcf_valuation(fcf_base, growth_rate, wacc)
    print(f"  DCF Value (EV)  : ${ev_dcf}Bn")

    # ── Comps ─────────────────────────────────────────────
    ev_comps = comps_valuation(company, ebitda)
    print(f"  Comps Value(EV) : ${ev_comps}Bn")

    # ── Charts ────────────────────────────────────────────
    plot_bridge(company, pv_fcfs, pv_terminal)
    plot_sensitivity(company, fcf_base, growth_rate)

    # ── Collect for comparison chart ──────────────────────
    all_companies.append(company)
    all_dcf_values.append(ev_dcf)
    all_comps_values.append(ev_comps)

# ── Final Comparison Chart ────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  Generating DCF vs Comps comparison chart...")
plot_dcf_vs_comps(all_companies, all_dcf_values, all_comps_values)

print("\n✅ All valuations complete!")