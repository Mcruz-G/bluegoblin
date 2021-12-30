from data_warehouse.data_warehouse import update_data
from data_warehouse.update_db import update_db
from strategies.ema_crossover_h import ema_crossover_h
from strategies.macd_crossover_h import macd_crossover_h

if __name__ == "__main__":
    update_db("1h")
    macd_crossover_cryptos = macd_crossover_h()
    print(f"macd CROSSOVER SELECTED CRYPTOS: {macd_crossover_cryptos}")
    ema_crossover_cryptos = ema_crossover_h()
    print(f"EMA CROSSOVER SELECTED CRYPTOS: {ema_crossover_cryptos}")
    