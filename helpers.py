"""Helper functions for WeWork IPO RCA analysis."""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_revenue_loss_data():
    return pd.DataFrame({
        'Period': ['2017','2018','H1 2019'],
        'Revenue_M': [886, 1820, 1540],
        'Net_Loss_M': [933, 1930, 904]
    })

def plot_revenue_vs_loss(df, save_path=None):
    x = np.arange(len(df))
    plt.figure()
    plt.plot(x, df['Revenue_M'], marker='o', label='Revenue ($M)')
    plt.plot(x, df['Net_Loss_M'], marker='o', label='Net Loss ($M)')
    plt.xticks(x, df['Period'])
    plt.title('WeWork Revenue vs Net Loss (2017–H1 2019)')
    plt.xlabel('Period')
    plt.ylabel('USD ($M)')
    plt.legend()
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    else:
        plt.show()

def load_valuation_data():
    return pd.DataFrame({
        'Point': ['2017','Jan-2019','Oct-2019'],
        'Valuation_M': [20000, 47000, 8000]
    })

def plot_valuation_trend(df, save_path=None):
    x = np.arange(len(df))
    plt.figure()
    plt.plot(x, df['Valuation_M'], marker='o', label='Valuation ($M)')
    plt.xticks(x, df['Point'])
    plt.title('WeWork Valuation Trend (2017–2019)')
    plt.xlabel('Point in Time')
    plt.ylabel('USD ($M)')
    plt.legend()
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    else:
        plt.show()
