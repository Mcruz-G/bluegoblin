import numpy as np 
from scipy.signal import savgol_filter
from .utils import load_m_data, symbols, regression_ceof, local_min_max


def apply_techincals(data):
    smooth_factor = 5
    data["SMOOTHED"] = savgol_filter(data["CLOSE"], smooth_factor, 3)
    _, local_max = local_min_max(list(data["SMOOTHED"].values))
    local_max_slope, local_max_int = regression_ceof(local_max)
    t = np.array(data["SMOOTHED"].index)
    data["RESISTANCE"] = (local_max_slope * t) + local_max_int
    data["METRIC"] = abs(np.log(data["RESISTANCE"]/data["CLOSE"]))

    return data

def apply_rule(data, treshold):
    data["RULE"] = data["METRIC"] <= treshold
    rule = data.RULE.iloc[-1]
    return rule

def close_to_resistance(treshold):
    selected_symbols = {"SYMBOL" : [], "PRICE" : [], "RESISTANCE" : []}

    for symbol in symbols:
        data = load_m_data(symbol)
        data = apply_techincals(data)
        rule = apply_rule(data, treshold)
        if rule:
            selected_symbols["SYMBOL"] += [symbol]
            selected_symbols["PRICE"] += [data.CLOSE.iloc[-1]]
            selected_symbols["RESISTANCE"] += [data.RESISTANCE.iloc[-1]]
    return selected_symbols





if __name__ == "__main__":
    close_to_resistance()