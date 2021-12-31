import os
import pandas as pd
from sqlalchemy import create_engine

def load_h_data(symbol, parse_dates=False):
    databases_path = os.environ["BG_DATAWAREHOUSE"] + "databases/"
    db_name = f"sqlite:///{databases_path}crypto_h_data.db"
    engine = create_engine(db_name)
    if parse_dates:
        data = pd.read_sql(symbol, engine, parse_dates=["DATE"])
    else:
        data = pd.read_sql(symbol, engine)
    return data

symbols = ("BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "ADAUSDT", 

        "XRPUSDT", "LUNAUSDT", "DOGEUSDT", "AVAXUSDT",

        "SHIBUSDT", "MATICUSDT", "LTCUSDT", "UNIUSDT",

        "ALGOUSDT", "TRXUSDT", "LINKUSDT", "MANAUSDT",

        "ATOMUSDT", "VETUSDT")
