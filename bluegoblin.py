import streamlit as st
import pandas as pd
from data_warehouse.data_warehouse import update_data
from webapp.buttons import build_everyone_op_button, build_close_to_support_button, build_close_to_resistance_button, build_high_check_button, build_low_check_button
from webapp.multiselect import build_multiselect


if __name__ == "__main__":

    st.title("Welcome to BlueGoblin, Ailyn. It is good to see you again.")
    st.header("Pick a strategy and look at the crypto signals or select many strategies to get the interception of their signals...")
    
    build_multiselect()

    st.subheader("")
    st.subheader("")
    st.subheader("")
    st.subheader("")
    st.header("Or do some quick analytics on our crypto universe with just a click.")
    
    build_everyone_op_button()
    build_close_to_support_button()
    build_close_to_resistance_button()
    build_high_check_button()
    build_low_check_button()


    st.subheader("... Talk to our admin if you'd like to add any functionality :)")
    
    update_data()
