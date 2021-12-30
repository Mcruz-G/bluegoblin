import random
from .utils import load_h_data, symbols

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
        data["RULE"] = data["RULE"] * data["EMA_50"] <= data[f"EMA_{period}"]
        data["RULE"] = data["RULE"] * data["EMA_8"] >= data[f"EMA_{period}"]
    rule = data.RULE.iloc[-1]
    return rule

def ema_crossover_h():
    ema_periods = [8, 16, 24, 36, 50]
    selected_symbols = []

    for symbol in symbols:
        data = load_h_data(symbol)
        data = apply_techincals(data, ema_periods)
        rule = apply_rule(data, ema_periods)
        if rule:
            selected_symbols.append(symbol)
    return selected_symbols

if __name__ == "__main__":
    print(ema_crossover_h())