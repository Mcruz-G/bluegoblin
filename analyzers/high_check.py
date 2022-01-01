import numpy as np 
from scipy.signal import savgol_filter
from .utils import load_m_data, symbols, regression_ceof, local_min_max
from datetime import datetime, timedelta

def apply_rule(data):
    rule = False
    today = datetime.utcnow()
    yesterday = datetime.strftime(today.date() - timedelta(days=1), "%Y-%m-%d")
    today = datetime.strftime(today.date(), "%Y-%m-%d")
    yesterday_data = data[data["DATE"] >= yesterday]
    yesterday_data = yesterday_data[ yesterday_data["DATE"] < today] 
    today_data = data[data["DATE"] >= today]
    h_t, h_y = max(today_data["HIGH"]), max(yesterday_data["HIGH"])
    if h_t > h_y:
        rule = True

    return rule, h_t, h_y 

def high_check():
    selected_symbols = {"SYMBOL" : [], "PRICE" : [], "H_T" : [], "H_Y" : []}

    for symbol in symbols:
        data = load_m_data(symbol)
        rule, h_t, h_y = apply_rule(data)
        if rule:
            selected_symbols["SYMBOL"] += [symbol]
            selected_symbols["PRICE"] += [data.CLOSE.iloc[-1]]
            selected_symbols["H_T"] += [h_t]
            selected_symbols["H_Y"] += [h_y]

    return selected_symbols



if __name__ == "__main__":
    high_check()