import numpy as np 
from scipy.signal import savgol_filter
from .utils import load_m_data, symbols, regression_ceof, local_min_max
from datetime import date, datetime, timedelta



def apply_rule(data):
    rule = False
    today = datetime.utcnow()
    yesterday = datetime.strftime(today.date() - timedelta(days=1), "%Y-%m-%d")
    today = datetime.strftime(today.date(), "%Y-%m-%d")
    yesterday_data = data[data["DATE"] >= yesterday]
    yesterday_data = yesterday_data[ yesterday_data["DATE"] < today] 
    today_data = data[data["DATE"] >= today]
    l_t, l_y = min(today_data["LOW"]), min(yesterday_data["LOW"])
    if l_t < l_y:
        rule = True

    return rule, l_t, l_y 

def low_check():
    selected_symbols = {"SYMBOL" : [], "PRICE" : [], "L_T" : [], "L_Y" : []}

    for symbol in symbols:
        data = load_m_data(symbol)
        rule, l_t, l_y = apply_rule(data)
        if rule:
            selected_symbols["SYMBOL"] += [symbol]
            selected_symbols["PRICE"] += [data.CLOSE.iloc[-1]]
            selected_symbols["L_T"] += [l_t]
            selected_symbols["L_Y"] += [l_y]

    return selected_symbols



if __name__ == "__main__":
    low_check()
