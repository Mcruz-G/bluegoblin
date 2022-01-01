from .close_to_resistance import close_to_resistance
from .close_to_support import close_to_support
from .high_check import high_check
from .low_check import low_check

analyzers = {
    "close_to_resistance" : close_to_resistance,
    "close_to_support" : close_to_support,
    "high_check" : high_check,
    "low_check" : low_check,
}