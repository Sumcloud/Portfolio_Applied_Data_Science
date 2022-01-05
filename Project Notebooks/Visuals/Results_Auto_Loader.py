import datetime
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import openpyxl
import math


def open_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path, delimiter=',')


def grouped_RMSE_histogram_per_gap(criteria:str,KNN_results, FFIL_results, Hot_Deck_results, Imputed_column, RNN_results=[0.0, 0.0, 0.0, 0.0, 0.0]):
    """ENTER THE MSE's FROM RESULTS IN ORDER OF GAPTYPE I.E. 1,2,3 FOR ONE COLUMN SO MAX 5"""
    if criteria == "Mean squared error":
        KNN_results = list(math.sqrt(i) for i in KNN_results)
        RNN_results = list(math.sqrt(i) for i in RNN_results)
        FFIL_results = list(math.sqrt(i) for i in FFIL_results)
        Hot_Deck_results = list(math.sqrt(i) for i in Hot_Deck_results)
        criteria = criteria.replace(criteria, "Root" + criteria)

    gap_labels = ['Size 1', 'Size 2', 'Size 3', 'Size 4', 'Size 5']
    fig, ax = plt.subplots(figsize=(12, 8))

    x = np.arange(len(gap_labels))
    bar_width = 0.25
    bar1 = x
    bar2 = [i + bar_width for i in bar1]
    bar3 = [i + bar_width for i in bar2]
    bar4 = [i + bar_width for i in bar3]

    method_1 = ax.bar(bar1, KNN_results, bar_width, label='KNN', hatch='/')
    method_2 = ax.bar(bar2, FFIL_results, bar_width, label='FFIL', hatch='\\')
    method_3 = ax.bar(bar3, RNN_results, bar_width, label='RNN', hatch='|')
    method_4 = ax.bar(bar4, Hot_Deck_results, bar_width, label='Hot Deck', hatch='-')

    ax.set_ylabel(criteria + ' scores')
    ax.set_title(criteria + ' score per gap size ' + Imputed_column)
    ax.set_xticks(x, gap_labels)
    ax.legend()

    ax.bar_label(method_1, padding=3)
    ax.bar_label(method_2, padding=3)
    ax.bar_label(method_3, padding=3)
    ax.bar_label(method_4, padding=3)

    fig.tight_layout()
    plt.grid(visible=True, axis='y')
    time = datetime.datetime.now()
    plt.savefig("RMSE_per_gap_type_for_" + Imputed_column +"_"+ f"{time.day}_{time.hour}_{time.minute}_{time.second}"+".png")
    plt.show()


def RMSE_loader_Fac_Zero(df: pd.DataFrame, columns:list, criteria="Mean squared error"):

    gap_size_indicators = ['gap type 1', 'gap type 2', 'gap type 3', 'gap type 4',
                           'gap type 5']  # Are all the gape types
    for column in columns:
        knn_result = []  # Empty list for each column to reset
        rnn_result = []
        ffil_result = []
        hot_deck_result = []
        for gap_size in gap_size_indicators:
            sub_df = df[
                (df['column'] == column) & (df['gap type'] == gap_size)]  # Subset the df for every column and gap

            knn_result.append(float(sub_df.loc[df["method"] == 'K-Nearest-Neighbors imputation'][criteria].values[0]))
            # rnn_result.append(float(sub_df.loc[df["method"]=='RNN'][criteria].values[0]))
            ffil_result.append(float(sub_df.loc[df["method"] == 'fillna'][criteria].values[0]))
            hot_deck_result.append(float(sub_df.loc[df["method"] == 'Hot deck'][criteria].values[0]))

        grouped_RMSE_histogram_per_gap(criteria=criteria,KNN_results=knn_result, FFIL_results=ffil_result, Hot_Deck_results=hot_deck_result,
                                       Imputed_column=column) # TODO RNN needs to be added here !!!


def grouped_RMSE_histogram_per_gap_KNMI(criteria:str,KNN_results, FFIL_results, Hot_Deck_results, Imputed_column, RNN_results=[0.0, 0.0, 0.0, 0.0]):
    """ENTER THE MSE's FROM RESULTS IN ORDER OF GAPTYPE I.E. 1,2,3 FOR ONE COLUMN SO MAX 5"""
    if criteria == "Mean squared error":
        KNN_results = list(math.sqrt(i) for i in KNN_results)
        RNN_results = list(math.sqrt(i) for i in RNN_results)
        FFIL_results = list(math.sqrt(i) for i in FFIL_results)
        Hot_Deck_results = list(math.sqrt(i) for i in Hot_Deck_results)
        criteria = criteria.replace(criteria,"Root" + criteria)

    gap_labels = ['Size 1', 'Size 2', 'Size 3', 'Size 4']
    fig, ax = plt.subplots(figsize=(12, 8))

    x = np.arange(len(gap_labels))
    bar_width = 0.25
    bar1 = x
    bar2 = [i + bar_width for i in bar1]
    bar3 = [i + bar_width for i in bar2]
    bar4 = [i + bar_width for i in bar3]

    method_1 = ax.bar(bar1, KNN_results, bar_width, label='KNN', hatch='/')
    method_2 = ax.bar(bar2, FFIL_results, bar_width, label='FFIL', hatch='\\')
    method_3 = ax.bar(bar3, RNN_results, bar_width, label='RNN', hatch='|')
    method_4 = ax.bar(bar4, Hot_Deck_results, bar_width, label='Hot Deck', hatch='-')

    ax.set_ylabel(criteria +' scores')
    ax.set_title(criteria + ' per gap size ' + Imputed_column)
    ax.set_xticks(x, gap_labels)
    ax.legend()

    ax.bar_label(method_1, padding=3)
    ax.bar_label(method_2, padding=3)
    ax.bar_label(method_3, padding=3)
    ax.bar_label(method_4, padding=3)

    fig.tight_layout()
    plt.grid(visible=True, axis='y')
    time = datetime.datetime.now()
    plt.savefig("RMSE_per_gap_type_for_" + Imputed_column +"_"+ f"{time.day}_{time.hour}_{time.minute}_{time.second}"+".png")
    plt.show()



def RMSE_loader_KNMI(df: pd.DataFrame,columns:list, criteria="Mean squared error"):
    gap_size_indicators = ['gap type 1', 'gap type 2', 'gap type 3', 'gap type 4']  # Are all the gape types
    for column in columns:
        knn_result = []  # Empty list for each column to reset
        rnn_result = []
        ffil_result = []
        hot_deck_result = []
        for gap_size in gap_size_indicators:
            sub_df = df[
                (df['column'] == column) & (df['gap type'] == gap_size)]  # Subset the df for every column and gap

            knn_result.append(float(sub_df.loc[df["method"] == 'K-Nearest-Neighbors imputation'][criteria].values[0]))
            # rnn_result.append(float(sub_df.loc[df["method"]=='RNN'][criteria].values[0]))
            ffil_result.append(float(sub_df.loc[df["method"] == 'fillna'][criteria].values[0]))
            hot_deck_result.append(float(sub_df.loc[df["method"] == 'Hot deck'][criteria].values[0]))

        grouped_RMSE_histogram_per_gap_KNMI(criteria= criteria, KNN_results=knn_result, FFIL_results=ffil_result, Hot_Deck_results=hot_deck_result,
                                       Imputed_column=column) # TODO ADD RNN HERE WHEN NEEDED!



if __name__ == "__main__":

    df = open_csv("Results.csv")
    columns = pd.unique(df['column'])  # Get all the unique column names

    RMSE_loader_Fac_Zero(df=df,criteria="Mean squared error",columns=columns[:4])
    RMSE_loader_KNMI(df=df,criteria="Mean squared error",columns=columns[4:len(columns)])
