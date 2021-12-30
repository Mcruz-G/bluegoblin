import streamlit as st
import pandas as pd
import datetime as dt
import numpy as np 
from sqlalchemy import create_engine

engine = create_engine("sqlite:///CryptoDB.db")
symbols = pd.read_sql('SELECT name FROM sqlite_master WHERE type="table"', engine).name.to_list()

st.title("Welcome to the live TA platform")

def apply_technical_indicators(df):
    df["SMA_7"] = df.c.rolling(7).mean()
    df["SMA_25"] = df.c.rolling(25).mean()
    df.dropna(inplace=True)

