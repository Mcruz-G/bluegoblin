import numpy as np 
from scipy.signal import savgol_filter
from .utils import load_m_data, symbols, regression_ceof, local_min_max



def apply_techincals(data):
    smooth_factor = 5
    data["SMOOTHED"] = savgol_filter(data["CLOSE"], smooth_factor, 3)
    local_min, _ = local_min_max(list(data["SMOOTHED"].values))
    local_min_slope, local_min_int = regression_ceof(local_min)
    t = np.array(data["SMOOTHED"].index)
    data["SUPPORT"] = (local_min_slope * t) + local_min_int
    data["METRIC"] = abs(np.log(data["SUPPORT"]/data["CLOSE"]))
    return data

def apply_rule(data, treshold):
    treshold = np.quantile(data["METRIC"], treshold)
    data["RULE"] = data["METRIC"] <= treshold
    rule = data.RULE.iloc[-1]
    return rule

def close_to_support(treshold):
    selected_symbols = {"SYMBOL": [], "PRICE" : [], "SUPPORT" : []}
    for symbol in symbols:
        data = load_m_data(symbol)
        data = apply_techincals(data)
        rule = apply_rule(data, treshold)
        if rule:
            selected_symbols["SYMBOL"] += [symbol]
            selected_symbols["PRICE"] += [data.CLOSE.iloc[-1]]
            selected_symbols["SUPPORT"] += [data.SUPPORT.iloc[-1]]
    return selected_symbols





if __name__ == "__main__":
    close_to_support()