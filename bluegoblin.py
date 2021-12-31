import streamlit as st
from data_warehouse.data_warehouse import update_data
from data_warehouse.update_db import update_db
from strategies.ema_crossover_h import ema_crossover_h
from strategies.macd_crossover_h import macd_crossover_h

def on_click_ema():
    ema_crossover_cryptos = ema_crossover_h()
    st.write("EMA Crossover strategic selection:")
    for symbol in ema_crossover_cryptos:
        st.write(symbol)

def on_click_macd():
    macd_crossover_cryptos = macd_crossover_h()
    st.write("MACD Crossover strategic selection:")
    for symbol in macd_crossover_cryptos:
        st.write(symbol)


if __name__ == "__main__":
    update_db("1h")
    st.title("Welcome to BlueGoblin, Ailyn. It is good to see you again.")
    ema_button  = st.button("Get EMA Crossover")
    macd_button = st.button("Get MACD Crossover")

    if ema_button:
        on_click_ema()
    
    if macd_button:
        on_click_macd()
