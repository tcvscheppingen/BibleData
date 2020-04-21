import pandas as pd
import matplotlib.pyplot as plt


def plot_corr(dataframe, fig_size_x, fig_size_y):
    # Plots a matrix of the correlation values of a dataframe.
    corr = dataframe.corr()

    fig = plt.figure(figsize=(fig_size_x, fig_size_y))
    plt.matshow(corr, cmap='RdBu', fignum=fig.number)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
    plt.yticks(range(len(corr.columns)), corr.columns)

    plt.show()

    return corr
