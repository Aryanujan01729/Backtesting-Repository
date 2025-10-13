import matplotlib.pyplot as plt

def plot_equity(df, title="Equity Curve"):
    (1+df['return']).cumprod().plot(label="Buy & Sell")
    (1+df['strat_ret']).cumprod().plot(label="Strategy")
    plt.legend()
    plt.title(title)
    plt.grid(True)
    plt.show()

    