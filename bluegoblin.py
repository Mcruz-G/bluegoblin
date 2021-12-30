from data_warehouse.data_warehouse import update_data
from data_warehouse.update_db import update_db
from strategies.ema_crossover_h import ema_crossover_h

if __name__ == "__main__":
    update_db("1h")
    ema_crossover_cryptos = ema_crossover_h()
    print(ema_crossover_cryptos)