import matplotlib.pyplot as plt

def plot_equity(df, title= "Equity Curve"):
    (1+ df['strat_ret']).cumprod().plot(label='Strategy')
    (1+df['ret']).cumprod().plot(label='Buy & Hold')
    plt.legend()
    plt.title(title)
    plt.grid(True)
    plt.show()

    df['mom_s'].plot(label='short momentum')
    df['mom_l'].plot(label='long momentum')
    plt.legend()
    plt.title('compare')
    plt.grid(True)
    plt.show()
    