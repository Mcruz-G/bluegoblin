import pandas as pd
from tqdm import tqdm
from datetime import datetime
from binance.client import Client
from sqlalchemy import create_engine

def get_data(client, symbol, lookback, resolution):
    frame = pd.DataFrame(client.get_historical_klines(symbol, resolution, 
                    lookback + " days ago UTC"))
    frame = frame.iloc[:,:5]
    frame.columns = ["DATE", "OPEN", "HIGH", "LOW", "CLOSE"]
    frame[["OPEN", "HIGH", "LOW", "CLOSE"]] = frame[["OPEN", "HIGH", "LOW", "CLOSE"]].astype(float)
    frame.DATE = pd.to_datetime(frame.DATE, unit="ms")
    return frame

def populate_db(db_engine, client, symbols, lookback, resolution="1m"):
    for symbol in tqdm(symbols):
        db_data = pd.read_sql(symbol, db_engine)
        last_date = db_data["DATE"].iloc[-1].to_pydatetime()
        
        data = get_data(client, symbol, lookback, resolution)
        data = data[data["DATE"] > last_date]
        data.to_sql(symbol, db_engine, index=False, if_exists="append")

if __name__ == "__main__":
    lookback = "120"
    resolution = "1h"
    db_name = "sqlite:///crypto_h_data.db"
    engine = create_engine(db_name)
    symbols = ("BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "ADAUSDT", 
        "XRPUSDT", "LUNAUSDT", "DOGEUSDT", "AVAXUSDT",
        "SHIBUSDT", "MATICUSDT", "LTCUSDT", "UNIUSDT",
        "ALGOUSDT", "TRXUSDT", "LINKUSDT", "MANAUSDT",
        "ATOMUSDT", "VETUSDT")

    client = Client()

    # populate_db(engine, client, symbols, lookback, resolution)
    # query_data = pd.read_sql("ETHUSDT", engine)
    # print(query_data)
    # print(datetime.utcnow())