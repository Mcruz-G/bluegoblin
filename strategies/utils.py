import os
import pandas as pd
from sqlalchemy import create_engine

def load_h_data(symbol):
    databases_path = os.environ["BG_DATAWAREHOUSE"] + "databases/"
    db_name = f"sqlite:///{databases_path}crypto_h_data.db"
    engine = create_engine(db_name)
    data = pd.read_sql("BTCUSDT", engine)
    return data

symbols = ("BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "ADAUSDT", 

        "XRPUSDT", "LUNAUSDT", "DOGEUSDT", "AVAXUSDT",

        "SHIBUSDT", "MATICUSDT", "LTCUSDT", "UNIUSDT",

        "ALGOUSDT", "TRXUSDT", "LINKUSDT", "MANAUSDT",

        "ATOMUSDT", "VETUSDT")
