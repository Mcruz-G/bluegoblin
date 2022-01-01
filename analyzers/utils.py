import os
import pandas as pd
import numpy as np 
from math import sqrt
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression


def load_h_data(symbol, parse_dates=False):
    databases_path = os.environ["BG_DATAWAREHOUSE"] + "databases/"
    db_name = f"sqlite:///{databases_path}crypto_h_data.db"
    engine = create_engine(db_name)
    if parse_dates:
        data = pd.read_sql(symbol, engine, parse_dates=["DATE"])
    else:
        data = pd.read_sql(symbol, engine)
    return data

def load_m_data(symbol, parse_dates=False):
    databases_path = os.environ["BG_DATAWAREHOUSE"] + "databases/"
    db_name = f"sqlite:///{databases_path}crypto_m_data.db"
    engine = create_engine(db_name)
    if parse_dates:
        data = pd.read_sql(symbol, engine, parse_dates=["DATE"])
    else:
        data = pd.read_sql(symbol, engine)
    return data


def pythag(pt1, pt2):
    a_sq = (pt2[0] - pt1[0]) ** 2
    b_sq = (pt2[1] - pt1[1]) ** 2
    return sqrt(a_sq + b_sq)

def local_min_max(pts):
    local_min = []
    local_max = []
    prev_pts = [(0, pts[0]), (1, pts[1])]
    for i in range(1, len(pts) - 1):
        append_to = ''
        if pts[i-1] > pts[i] < pts[i+1]:
            append_to = 'min'
        elif pts[i-1] < pts[i] > pts[i+1]:
            append_to = 'max'
        if append_to:
            if local_min or local_max:
                prev_distance = pythag(prev_pts[0], prev_pts[1]) * 0.5
                curr_distance = pythag(prev_pts[1], (i, pts[i]))
                if curr_distance >= prev_distance:
                    prev_pts[0] = prev_pts[1]
                    prev_pts[1] = (i, pts[i])
                    if append_to == 'min':
                        local_min.append((i, pts[i]))
                    else:
                        local_max.append((i, pts[i]))
            else:
                prev_pts[0] = prev_pts[1]
                prev_pts[1] = (i, pts[i])
                if append_to == 'min':
                    local_min.append((i, pts[i]))
                else:
                    local_max.append((i, pts[i]))
    return local_min, local_max

def regression_ceof(pts):
    X = np.array([pt[0] for pt in pts]).reshape(-1, 1)
    y = np.array([pt[1] for pt in pts])
    model = LinearRegression()
    model.fit(X, y)
    return model.coef_[0], model.intercept_

symbols = ("BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "ADAUSDT", 

        "XRPUSDT", "LUNAUSDT", "DOGEUSDT", "AVAXUSDT",

        "SHIBUSDT", "MATICUSDT", "LTCUSDT", "UNIUSDT",

        "ALGOUSDT", "TRXUSDT", "LINKUSDT", "MANAUSDT",

        "ATOMUSDT", "VETUSDT")
