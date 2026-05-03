def dcf_valuation(fcf_base, growth_rate, wacc, terminal_growth=0.03, years=5):
    # Project FCFs for 5 years
    fcfs = [fcf_base * (1 + growth_rate)**i for i in range(1, years + 1)]

    # Discount each FCF back to present value
    pv_fcfs = [fcf / (1 + wacc)**i for i, fcf in enumerate(fcfs, 1)]

    # Terminal Value using Gordon Growth Model
    terminal_value = fcfs[-1] * (1 + terminal_growth) / (wacc - terminal_growth)
    pv_terminal = terminal_value / (1 + wacc)**years

    enterprise_value = sum(pv_fcfs) + pv_terminal

    return round(enterprise_value, 2), [round(x, 2) for x in pv_fcfs], round(pv_terminal, 2)