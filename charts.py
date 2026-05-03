import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ── 1. Valuation Bridge (Waterfall) ──────────────────────────────────────────
def plot_bridge(company, pv_fcfs, pv_terminal):
    labels = [f"FCF Y{i+1}" for i in range(len(pv_fcfs))] + ["Terminal Value"]
    values = pv_fcfs + [pv_terminal]
    colors = ["steelblue"] * len(pv_fcfs) + ["darkorange"]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, values, color=colors)
    plt.title(f"{company} — DCF Valuation Bridge ($Bn)")
    plt.ylabel("Value ($Bn)")
    plt.tight_layout()
    plt.savefig(f"visuals/{company}_bridge.png")
    plt.show()
    print(f"  Saved: visuals/{company}_bridge.png")


# ── 2. Sensitivity Heatmap ────────────────────────────────────────────────────
def plot_sensitivity(company, fcf_base, growth_rate):
    from models.dcf import dcf_valuation

    wacc_range   = [0.08, 0.09, 0.10, 0.11, 0.12]
    growth_range = [0.02, 0.025, 0.03, 0.035, 0.04]

    table = pd.DataFrame(index=wacc_range, columns=growth_range)

    for w in wacc_range:
        for g in growth_range:
            ev, _, _ = dcf_valuation(fcf_base, growth_rate, w, g)
            table.loc[w, g] = round(ev, 1)

    table = table.astype(float)

    plt.figure(figsize=(8, 5))
    plt.imshow(table.values, cmap="RdYlGn", aspect="auto")
    plt.colorbar(label="EV ($Bn)")
    plt.xticks(range(len(growth_range)), [f"{g*100:.1f}%" for g in growth_range])
    plt.yticks(range(len(wacc_range)),   [f"{w*100:.1f}%" for w in wacc_range])
    plt.xlabel("Terminal Growth Rate")
    plt.ylabel("WACC")
    plt.title(f"{company} — Sensitivity: WACC vs Terminal Growth")
    plt.tight_layout()
    plt.savefig(f"visuals/{company}_sensitivity.png")
    plt.show()
    print(f"  Saved: visuals/{company}_sensitivity.png")


# ── 3. DCF vs Comps Comparison Bar Chart ─────────────────────────────────────
def plot_dcf_vs_comps(companies, dcf_values, comps_values):
    x = np.arange(len(companies))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar(x - width/2, dcf_values,   width, label="DCF Value",   color="steelblue")
    plt.bar(x + width/2, comps_values, width, label="Comps Value", color="darkorange")

    plt.xticks(x, companies)
    plt.ylabel("Enterprise Value ($Bn)")
    plt.title("DCF vs Trading Comps — All Companies")
    plt.legend()
    plt.tight_layout()
    plt.savefig("visuals/dcf_vs_comps.png")
    plt.show()
    print("  Saved: visuals/dcf_vs_comps.png")