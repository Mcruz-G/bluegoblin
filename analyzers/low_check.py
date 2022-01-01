import numpy as np 
from scipy.signal import savgol_filter
from .utils import load_m_data, symbols, regression_ceof, local_min_max
from datetime import date, datetime, timedelta

def apply_rule(data):
    rule = False
    today = datetime.utcnow()
    yesterday = datetime.strftime(today.date() - timedelta(days=1), )
    today = datetime.strftime(today.date())
    yesterday_data = data[data["DATE"] >= yesterday]
    yesterday_data = yesterday_data[ yesterday_data["DATE"] < today] 
    today_data = data[data["DATE"] >= today]

    if min(yesterday_data["LOW"]) > min(today_data["LOW"]):
        rule = True
    
    return rule 

def low_check():
    selected_symbols = {"SYMBOL" : [], "PRICE" : [], "L_T" : [], "L_Y" : []}

    for symbol in symbols:
        data = load_m_data(symbol)
        rule = apply_rule(data)
        if rule:
            selected_symbols["SYMBOL"] += [symbol]
            selected_symbols["PRICE"] += [data.CLOSE.iloc[-1]]
            selected_symbols["L_T"] += [data.L_T.iloc[-1]]
            selected_symbols["L_Y"] += [data.L_Y.iloc[-1]]

    return selected_symbols



if __name__ == "__main__":
    low_check()