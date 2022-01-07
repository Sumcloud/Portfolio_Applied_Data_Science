import math
import numpy as np
import matplotlib.pyplot as plt
import datetime

def criteria_bar_plotter(RNN_result: list, KNN_result: list, LOCF_result: list, Hot_deck_result: list, criteria: str,
                         feature: str, gap_indicators: list):
    if criteria == "Mean squared error":
        KNN_result = list(math.sqrt(i) for i in KNN_result)
        RNN_result = list(math.sqrt(i) for i in RNN_result)
        LOCF_result = list(math.sqrt(i) for i in LOCF_result)
        Hot_deck_result = list(math.sqrt(i) for i in Hot_deck_result)
        criteria = criteria.replace(criteria, "Root " + criteria)
    if criteria == "Variance error":
        KNN_result = list(np.abs(i) for i in KNN_result)
        RNN_result = list(np.abs(i) for i in RNN_result)
        LOCF_result = list(np.abs(i) for i in LOCF_result)
        Hot_deck_result = list(np.abs(i) for i in Hot_deck_result)
        criteria = criteria.replace(criteria, "Absolute " + criteria)

    x = np.arange(len(gap_indicators))
    fig, ax = plt.subplots(figsize=(12, 8))
    bar_width = 0.25

    bar1 = x
    bar2 = [i + bar_width for i in bar1]
    bar3 = [i + bar_width for i in bar2]
    bar4 = [i + bar_width for i in bar3]

    method_1 = ax.bar(bar1, KNN_result, bar_width, label='KNN', hatch='/')
    method_2 = ax.bar(bar2, LOCF_result, bar_width, label='LOCF', hatch='\\')
    method_3 = ax.bar(bar3, RNN_result, bar_width, label='RNN', hatch='|')
    method_4 = ax.bar(bar4, Hot_deck_result, bar_width, label='Hot Deck', hatch='-')

    ax.set_ylabel(criteria + ' scores')
    ax.set_title(criteria + ' score per gap size ' + feature)
    ax.set_xticks(x, gap_indicators)
    ax.legend()

    ax.bar_label(method_1, padding=3)
    ax.bar_label(method_2, padding=3)
    ax.bar_label(method_3, padding=3)
    ax.bar_label(method_4, padding=3)

    fig.tight_layout()
    plt.grid(visible=True, axis='y')
    time = datetime.datetime.now()
    plt.savefig(
        criteria + '_per_gap_' + feature + "_" + f"{time.day}_{time.hour}_{time.minute}_{time.second}" + ".png")
    plt.show()