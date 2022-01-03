import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def grouped_RMSE_histogram_per_gap(KNN_MSE,RNN_MSE,FFIL_MSE,Hot_Deck_MSE,Imputed_column):
    """ENTER THE MSE's FROM RESULTS IN ORDER OF GAPTYPE I.E. 1,2,3 FOR ONE COLUMN SO MAX 5"""
    KNN_RMSE = list(math.sqrt(i) for i in KNN_MSE)
    RNN_RMSE = list(math.sqrt(i) for i in RNN_MSE)
    FFIL_RMSE = list(math.sqrt(i) for i in FFIL_MSE)
    Hot_Deck_RMSE = list(math.sqrt(i) for i in Hot_Deck_MSE)

    gap_labels = ['Size 1', 'Size 2', 'Size 3', 'Size 4', 'Size 5']
    fig, ax = plt.subplots(figsize=(12, 8))

    x = np.arange(len(gap_labels))
    bar_width = 0.25
    bar1 = x
    bar2 = [i+bar_width for i in bar1]
    bar3 = [i+bar_width for i in bar2]
    bar4 = [i+bar_width for i in bar3]

    method_1 = ax.bar(bar1, KNN_RMSE, bar_width, label='KNN', hatch='/')
    method_2 = ax.bar(bar2, FFIL_RMSE, bar_width, label='FFIL', hatch='\\')
    method_3 = ax.bar(bar3, RNN_RMSE, bar_width, label='RNN',hatch='|')
    method_4 = ax.bar(bar4, Hot_Deck_RMSE, bar_width, label='Hot Deck', hatch='-')

    ax.set_ylabel('RMSE scores')
    ax.set_title('RMSE score per gap size ' + Imputed_column)
    ax.set_xticks(x, gap_labels)
    ax.legend()

    ax.bar_label(method_1, padding=3)
    ax.bar_label(method_2, padding=3)
    ax.bar_label(method_3, padding=3)
    ax.bar_label(method_4, padding=3)

    fig.tight_layout()
    plt.grid(visible=True,axis='both')
    plt.savefig("RMSE_per_gap_type_for_" + Imputed_column)
    plt.show()