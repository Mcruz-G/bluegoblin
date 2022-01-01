import os, sys
import pandas as pd
import streamlit as st
from .utils import build_crypto_signal_display, build_high_check_display, build_support_display, build_resistance_display

bg_path = os.environ["BG_PATH"]
strats_path = f"{bg_path}strategies/"
analyzers_path = f"{bg_path}analyzers/"
sys.path.insert(1, strats_path)
sys.path.insert(1, analyzers_path)

from strategies.strats_dict import strategies
from strategies.utils import symbols, load_m_data
from analyzers.analyzers_dict import analyzers

def build_everyone_op_button():
    everyone_op_button = st.button("Get Everyone's opinion")
    if everyone_op_button:
        on_click_everyone_op()

def build_close_to_support_button():
    close_to_support_button = st.button("Get Cryptos close to support estimate")
    if close_to_support_button:
        on_click_close_to_support()

def build_close_to_resistance_button():
    close_to_resistance_button = st.button("Get Cryptos close to resistance estimate")
    if close_to_resistance_button:
        on_click_close_to_resistance()

def build_high_check_button():
    high_check_button = st.button("Get Cryptos whose high check is positive")
    if high_check_button:
        on_click_high_check()

def build_low_check_button():
    low_check_button = st.button("Get Cryptos whose low check is positive")
    if low_check_button:
        on_click_low_check()

def on_click_everyone_op():
    selected_symbols = set(symbols)
    for strategy in list(strategies.values()):
        selected_symbols = selected_symbols.intersection(set(strategy()["SYMBOL"]))
    if len(selected_symbols) > 0:
        build_crypto_signal_display(selected_symbols)
    else:
        st.write("There are not selected cryptos for this set of strategies. For more detail, look at the individual selection of each strategy.")

def on_click_close_to_support():
    selected_cryptos = analyzers["close_to_support"](treshold=0.01)
    
    if len(selected_cryptos["SYMBOL"]) > 0:
        build_support_display(selected_cryptos)
       
    else:
        st.write("There's no crypto coin close to support")

def on_click_close_to_resistance():
    selected_cryptos = analyzers["close_to_resistance"](treshold=0.01)
    
    if len(selected_cryptos["SYMBOL"]) > 0:
        build_resistance_display(selected_cryptos)
    else:
        st.write("There's no crypto coin close to resistance")

def on_click_high_check():
    selected_cryptos = analyzers["high_check"]()

    if len(selected_cryptos["SYMBOL"]) > 0:
        build_high_check_display(selected_cryptos)
    else:
        st.write("There's no crypto coin whose current highest high is higher than yesterday's")

def on_click_low_check():
    selected_cryptos = analyzers["low_check"]()


    if len(selected_cryptos["SYMBOL"]) > 0:
        build_low_check_display(selected_cryptos)
    else:
        st.write("There's no crypto coin whose current highest high is higher than yesterday's")
