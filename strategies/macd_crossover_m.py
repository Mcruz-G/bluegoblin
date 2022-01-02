
import pandas_ta as ta
import numpy as np
from .utils import load_m_data, symbols


def apply_techincals(data, macd_periods):

    fast_macd_period = macd_periods[0]
    slow_macd_period = macd_periods[1]
    data["EMA_50"] = ta.ema(data["CLOSE"], 50 * 60)
    data[["MACD", "S_MACD"]] = ta.macd(data["CLOSE"], fast=fast_macd_period, slow=slow_macd_period, signal= 9*6).loc[:,[f"MACD_{fast_macd_period}_{slow_macd_period}_{9*6}", f"MACDs_{fast_macd_period}_{slow_macd_period}_{9*6}"]]
    data["METRIC"] = (abs(data["MACD"] - data["S_MACD"])) / (abs(data["MACD"] + data["S_MACD"]))
    
    return data

def apply_rule(data, treshold):
    data["RULE"] = data["CLOSE"] > data["EMA_50"]
    data["RULE"] = np.logical_and(data["RULE"], data["METRIC"] > 0)
    data["RULE"] = np.logical_and(data["RULE"], data["METRIC"] < treshold) 
    rule = data.RULE.iloc[-1]

    return rule

def macd_crossover_m():
    macd_periods = (12 * 60, 48 * 60)
    selected_symbols = {"SYMBOL": [], "PRICE" : []}


    for symbol in symbols:
        data = load_m_data(symbol, parse_dates=True)
        data = apply_techincals(data, macd_periods)
        rule = apply_rule(data, treshold=0.1)

        if rule:
            selected_symbols["SYMBOL"] += [symbol]
            selected_symbols["PRICE"] += [data.CLOSE.iloc[-1]]
    return selected_symbols
if __name__ == "__main__":
    macd_crossover_m()