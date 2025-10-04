import numpy as np
import pandas as pd
from math import sqrt
import sys, os
sys.path.append(os.path.abspath("../src"))
import import_ipynb

def compute_performance(returns: pd.Series,periods_per_year=252)->dict:
    cumulative=(1+returns).cumprod()
    total_return= cumulative.iloc[-1]-1
    n_years=len(returns)/periods_per_year
    cagr=(1+total_return)**(1/n_years)-1
    vol=returns.std()*sqrt(periods_per_year)
    sharpe=(returns.mean()*periods_per_year)/(returns.std()*sqrt(periods_per_year)) if vol else np.nan
    peak=cumulative.cummax()
    drawdown=(cumulative-peak)/peak
    max_dd=drawdown.min()
    return {
        'total_return': float(total_return),
        'cagr':float(cagr),
        'annual_vol': float(vol),
        'sharpe': float(sharpe),
        'max_drawdown': float(max_dd)
    }