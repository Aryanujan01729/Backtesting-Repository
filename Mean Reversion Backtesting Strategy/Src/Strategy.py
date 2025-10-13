import pandas as pd
import numpy as np

def Mean_Reversion_strategy(price : pd.Series , duration: int, exposure: float=1.0 )->pd.DataFrame:
    df=pd.DataFrame({'price':price})
    df['r_mean']=df['price'].rolling(window=duration).mean()
    df['r_std']=df['price'].rolling(window=duration).std()
    df['Z_score']= (df['price']-df['r_mean'])/df['r_std']
    df.dropna(subset=['Z_score'], inplace=True)
    df['signal']=0
    df.loc[df['Z_score']<-0.15,'signal']=-1
    df.loc[df['Z_score']>0.15,'signal']=1
    df.loc[df['Z_score']>3,'signal']=0
    df.loc[df['Z_score']<-3,'signal']=0
    df['position']=df['signal'].shift(1).fillna(0)*exposure
    df.dropna(subset=['Z_score'], inplace=True)

    return df