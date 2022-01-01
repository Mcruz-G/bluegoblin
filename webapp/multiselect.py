import os, sys
import streamlit as st

bg_path = os.environ["BG_PATH"]
path = f"{bg_path}strategies/"
sys.path.insert(1, path)

from strategies.strats_dict import strategies
from strategies.utils import symbols, load_m_data

def build_multiselect():
    multiselect = st.multiselect("",["EMA Crossover", "MACD Crossover"])

    selected_symbols = set(symbols)
    for strategy in multiselect:
        if strategy == "EMA Crossover":
            selected_symbols = selected_symbols.intersection(set(strategies["ema_crossover_m"]()["SYMBOL"]))
        elif strategy == "MACD Crossover":
            selected_symbols = selected_symbols.intersection(set(strategies["macd_crossover_m"]()["SYMBOL"]))

    if len(selected_symbols) > 0 and len(multiselect) > 0:
        for symbol in selected_symbols:
            price = load_m_data(symbol)["CLOSE"].iloc[-1]
            ret = round(100 * load_m_data(symbol)["CLOSE"].pct_change(60).iloc[-1], 2)
            value = f"{symbol}, {price}$ USD"
            delta = f"{ret} %"
            st.metric(label="Crypto Signal", value=value, delta=delta)

