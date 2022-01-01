import numpy as np 
from .utils import load_m_data, symbols

def apply_emas(ema_periods, data):
    for period in ema_periods:
        data[f"EMA_{period}"] = data["CLOSE"].ewm(span=period, adjust=False).mean()
    return data

def apply_techincals(data, ema_periods):
    data = apply_emas(ema_periods, data)
    return data

def apply_rule(data, ema_periods):
    data["RULE"] = True
    for period in ema_periods:
        data["RULE"] = np.logical_and(data["RULE"], data[f"EMA_{ema_periods[-1]}"] <= data[f"EMA_{period}"])
        data["RULE"] = np.logical_and(data["RULE"], data[f"EMA_{ema_periods[0]}"] >= data[f"EMA_{period}"])
    rule = data.RULE.iloc[-1]
    return rule

def ema_crossover_m():
    ema_periods = [ 8 * 60, 16 * 60, 50 * 60]
    selected_symbols = {"SYMBOL": [], "PRICE" : []}


    for symbol in symbols:
        data = load_m_data(symbol)
        data = apply_techincals(data, ema_periods)
        rule = apply_rule(data, ema_periods)
        if rule:
            selected_symbols["SYMBOL"] += [symbol]
            selected_symbols["PRICE"] += [data.CLOSE.iloc[-1]]
    return selected_symbols

if __name__ == "__main__":
    ema_crossover_m()