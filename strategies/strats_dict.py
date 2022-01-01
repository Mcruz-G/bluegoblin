from .ema_crossover_h import ema_crossover_h
from .ema_crossover_m import ema_crossover_m
from .macd_crossover_h import macd_crossover_h
from .macd_crossover_m import macd_crossover_m

strategies = {
    "ema_crossover_m" : ema_crossover_m,
    "macd_crossover_m" : macd_crossover_m,
}