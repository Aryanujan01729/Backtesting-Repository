import pandas as pd

def momentum_crossover(price:pd.Series, short: int, long:int)-> pd.DataFrame:
    """ Generate Momentum Crossing over Signals."""
    df=pd.DataFrame({'price': price})
    df['mom_s']=df['price']-df['price'].shift(short)
    df['mom_l']=df['price']-df['price'].shift(long)
    df['signal']=(df['mom_s']>df['mom_l']).astype(int)
    df['position']= df['signal'].shift(1).fillna(0)
    return df