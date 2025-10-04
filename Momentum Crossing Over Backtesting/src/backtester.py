import sys
import pandas as pd 
from math import sqrt
import sys, os
sys.path.append(os.path.abspath("../src/"))
import import_ipynb
from performance import compute_performance

def run_backtest(df: pd.DataFrame,fee:float =0.0005)->tuple[pd.DataFrame,dict]:
    """ Run vectorized backtest"""
    df=df.copy()
    df['ret']=df['price'].pct_change()
    df['trade']=df['position'].diff().abs()
    df['strat_ret']=df['position']*df['ret']-df['trade']*fee
    df.dropna(inplace=True)
    perf=compute_performance(df['strat_ret'])
    return df, perf