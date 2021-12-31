
import pandas_ta as ta
import numpy as np
from .utils import load_h_data, symbols


def apply_techincals(data, macd_periods):

    fast_macd_period = macd_periods[0]
    slow_macd_period = macd_periods[1]

    data["EMA_50"] = ta.ema(data["CLOSE"], 50)
    data[["MACD", "S_MACD"]] = ta.macd(data["CLOSE"]).loc[:,["MACD_12_26_9", "MACDs_12_26_9"]]
    return data

def apply_rule(data, macd_periods):
    data["RULE"] = data["CLOSE"] > data["EMA_50"]
    data["RULE"] = np.logical_and(data["RULE"], data["MACD"] > data["S_MACD"]) 
    rule = data.RULE.iloc[-1]

    return rule

def macd_crossover_h():
    macd_periods = (12, 48)
    selected_symbols = []

    for symbol in symbols:
        data = load_h_data(symbol, parse_dates=True)
        data = apply_techincals(data, macd_periods)
        rule = apply_rule(data, macd_periods)

        if rule:
            selected_symbols.append(symbol)
    return selected_symbols

if __name__ == "__main__":
    print(macd_crossover_h())