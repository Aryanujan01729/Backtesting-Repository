import sys
import os
import pandas as pd
sys.path.append(os.path.abspath("../src/"))
from Performance import compute_performance

def run_backtest(df: pd.DataFrame, fees: float=0.00005)-> tuple[pd.DataFrame,dict]:
    df=df.copy()
    df['return']=df['price'].pct_change()
    df['trade']=df['position'].diff().abs()
    df['strat_ret']=df['position']*df['return']-fees*df['trade']
    df.dropna(inplace=True)
    perform= compute_performance(df['strat_ret'])
    return df, perform