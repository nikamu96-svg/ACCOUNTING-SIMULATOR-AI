from accounting import record_sale, record_expense

def make_decision(financials, decision, amount):
    if decision == "Penjualan":
        record_sale(financials, amount)
        message = f"Terjadi penjualan sebesar Rp{amount:,}"
    elif decision == "Biaya Operasional":
        record_expense(financials, amount)
        message = f"Terjadi biaya operasional sebesar Rp{amount:,}"
    else:
        message = "Keputusan tidak dikenali"
    return financials, message
