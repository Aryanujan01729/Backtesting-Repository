
import yfinance as yf
import pandas as pd
from pathlib import Path

def get_data(symbol: str, start: str , end: str=None, save: bool=True)-> pd.Series:
    """Download adjusted close data from Yahoo Finance"""
    path=Path("data")/ f"{symbol}.csv"
    if path.exists():
        data=pd.read_csv(path,index_col=0,parse_dates=True)
    else:
        data=yf.download(symbol,start=start,end=end, progress=False)
        if save:
            path.parent.mkdir(exist_ok=True)
            data.to_csv(path)
    print(data.head())
    print("*******")
    price = data["Close"]
    price = pd.to_numeric(price, errors="coerce")
    price.dropna(inplace=True)

    return price