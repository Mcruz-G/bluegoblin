import os, sys
import streamlit as st

bg_path = os.environ["BG_PATH"]
strats_path = f"{bg_path}strategies/"
analyzers_path = f"{bg_path}analyzers/"
sys.path.insert(1, strats_path)
sys.path.insert(1, analyzers_path)

from strategies.utils import load_m_data
from analyzers.analyzers_dict import analyzers

def build_crypto_signal_display(selected_symbols):
    for symbol in selected_symbols:
            price = load_m_data(symbol)["CLOSE"].iloc[-1]
            ret = round(100 * load_m_data(symbol)["CLOSE"].pct_change(60).iloc[-1], 3)
            value = f"{symbol}, Price: {price}$ USD"
            delta = f"{ret} %"
            st.metric(label="Crypto Signal", value=value, delta=delta)

def build_support_display(selected_cryptos):
    symbols, prices, supports = selected_cryptos["SYMBOL"], selected_cryptos["PRICE"], selected_cryptos["SUPPORT"]
    for i in range(len(symbols)):
        ret = round(100 * load_m_data(symbols[i])["CLOSE"].pct_change(60).iloc[-1], 3)
        value = f"{symbols[i]}, P: {prices[i]}$ USD, S: {round(supports[i], 3)}$ USD"
        delta = f"{ret} %"
        st.metric(label="Support Alert", value=value, delta=delta)

def build_resistance_display(selected_cryptos):
    symbols, prices, resistances = selected_cryptos["SYMBOL"], selected_cryptos["PRICE"], selected_cryptos["RESISTANCE"]
    for i in range(len(symbols)):
        ret = round(100 * load_m_data(symbols[i])["CLOSE"].pct_change(60).iloc[-1], 3)
        value = f"{symbols[i]}, P: {prices[i]}$ USD, R: {round(resistances[i], 3)}$ USD"
        delta = f"{ret} %"
        st.metric(label="Resistance Alert", value=value, delta=delta)

def build_high_check_display(selected_cryptos):
    symbols, ht, hy = selected_cryptos["SYMBOL"], selected_cryptos["H_T"], selected_cryptos["H_Y"]
    for i in range(len(symbols)):
        ret = round(100 * load_m_data(symbols[i])["CLOSE"].pct_change(60).iloc[-1], 3)
        value = f"{symbols[i]}, H_T: {ht[i]}$ USD, H_Y: {round(hy[i], 3)}$ USD"
        delta = f"{ret} %"
        st.metric(label="Higher Highs Alert", value=value, delta=delta)

def build_low_check_display(selected_cryptos):
    symbols, lt, ly = selected_cryptos["SYMBOL"], selected_cryptos["L_T"], selected_cryptos["L_Y"]
    for i in range(len(symbols)):
        ret = round(100 * load_m_data(symbols[i])["CLOSE"].pct_change(60).iloc[-1], 3)
        value = f"{symbols[i]}, L_T: {lt[i]}$ USD, L_Y: {round(ly[i], 3)}$ USD"
        delta = f"{ret} %"
        st.metric(label="Lower Lows Alert", value=value, delta=delta)