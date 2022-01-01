import os
import pandas as pd
from datetime import date, datetime
from binance.client import Client
from sqlalchemy import create_engine
from .populate_db import populate_db

def check_last_date(symbol, engine):
    data = pd.read_sql(symbol, engine)
    last_date = data["DATE"].iloc[-1].to_pydatetime()
    return last_date

def update_db(resolution):
    client = Client()
    res = resolution.replace("1","")
    database_path = os.environ["BG_DATAWAREHOUSE"] + "databases/"
    db_name = f"sqlite:///{database_path}crypto_{res}_data.db"
    engine = create_engine(db_name)
    symbols = ("BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "ADAUSDT", 

        "XRPUSDT", "LUNAUSDT", "DOGEUSDT", "AVAXUSDT",

        "SHIBUSDT", "MATICUSDT", "LTCUSDT", "UNIUSDT",

        "ALGOUSDT", "TRXUSDT", "LINKUSDT", "MANAUSDT",

        "ATOMUSDT", "VETUSDT")

    for symbol in symbols:
        now = datetime.utcnow()
        last_date = check_last_date(symbol, engine)
        time_diff = now - last_date

        if res == "h":
            hours = time_diff.seconds // 3600
            if hours > 0:
                print(f"Loading new {symbol} data to {db_name}")
                populate_db(engine, client, [symbol], lookback="1", resolution=resolution)
            else:
                print("Updated DataBase. There's no available data to add.")

        elif res == "m":
            mins = time_diff.seconds // 60
            if mins > 15:
                print(f"Loading new {symbol} data to {db_name}")
                populate_db(engine, client, [symbol], lookback="1", resolution=resolution)
            else:
                print("Updated DataBase. There's no available data to add.")

if __name__ == "__main__":
    update_db("1h")
        