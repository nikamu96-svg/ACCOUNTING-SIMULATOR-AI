import pandas as pd

def init_financials():
    return {
        "cash": 10000000,
        "revenue": 0,
        "expense": 0
    }

def record_sale(financials, amount):
    financials["cash"] += amount
    financials["revenue"] += amount

def record_expense(financials, amount):
    financials["cash"] -= amount
    financials["expense"] += amount

def profit_loss(financials):
    return financials["revenue"] - financials["expense"]
