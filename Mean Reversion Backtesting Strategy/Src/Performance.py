import numpy as np
import pandas as pd
from math import sqrt
import sys, os

def compute_performance(ret: pd.Series, period_per_year: int =252 )-> dict:
    cumulative= (1+ret).cumprod()
    total_ret=cumulative.iloc[-1]-1
    n_year=len(ret)/period_per_year
    cagr=(1+total_ret)**(1/n_year)-1
    vol= ret.std()* sqrt(period_per_year)
    if vol:
        sharpe=(ret.mean()*period_per_year)/(vol)
    else:
        sharpe=np.nan
    peak=cumulative.cummax()
    drawdown=(cumulative-peak)/peak
    max_dd=drawdown.min()
    return {
        'Total_return': float(total_ret),
        'CAGR':float(cagr),
        'Voltality':float(vol),
        'Sharpe':float(sharpe),
        'Max Drawdown':float(max_dd)
    }
    
    
    
    