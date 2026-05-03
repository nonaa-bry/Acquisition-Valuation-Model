def calculate_wacc(beta, debt, equity, tax_rate=0.21):
    risk_free_rate = 0.045       # 10yr US Treasury (~4.5%)
    equity_risk_premium = 0.055  # Damodaran ERP

    cost_of_equity = risk_free_rate + beta * equity_risk_premium
    cost_of_debt = 0.06          # Assumed 6% borrowing rate
    total = equity + debt

    wacc = (equity / total * cost_of_equity) + (debt / total * cost_of_debt * (1 - tax_rate))
    return round(wacc, 4)