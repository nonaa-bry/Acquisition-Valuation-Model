# EV/EBITDA multiples from public market data
COMPS_MULTIPLES = {
    "Blackstone": 20,
    "BlackRock":  18,
    "Apollo":     16,
    "KKR":        17,
    "Ares":       19
}

def comps_valuation(company, ebitda):
    multiple = COMPS_MULTIPLES.get(company)
    if not multiple:
        return None
    ev = ebitda * multiple
    return round(ev, 2)