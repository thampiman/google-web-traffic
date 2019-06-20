import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
sns.set(style='white')
sns.set_palette("bright")

def plot_value_counts_pc(df, col):
    df2 = df[col].value_counts() / len(df) * 100
    df2 = df2.reset_index()
    df2 = df2.rename(columns={col: 'pc', 'index': col})
    f, ax = plt.subplots()
    df2.plot(x=col, y='pc', kind='bar', ax=ax)
    ax.grid(True);
    ax.get_legend().remove()
    ax.set_ylabel('Proportion of Data (%)')
    return df2, f, ax
