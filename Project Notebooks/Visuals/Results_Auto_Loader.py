import math
import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


def load_csv(path: str, delimiter):
    return pd.read_csv(path, delimiter=delimiter)


def get_result_per_column_and_gap_criteria(df: pd.DataFrame, criterias: list):
    features = df['Target field'].unique()
    for criteria in criterias:
        for feature in features:
            gap_indicators = df[df['Target field'] == feature]['Gap type'].unique()
            KNN_result = []
            RNN_result = []
            LOCF_result = []
            Hot_deck_result = []
            for gap_indicator in gap_indicators:
                sub_df = df[(df['Target field'] == feature) & (df['Gap type'] == gap_indicator)]
                KNN_result.append(float(sub_df.loc[df['Method'] == 'KNN k=10'][criteria].values[0]))
                RNN_result.append(float(sub_df.loc[df['Method'] == 'RNN'][criteria].values[0]))
                LOCF_result.append(float(sub_df.loc[df['Method'] == 'forward_fill'][criteria].values[0]))
                Hot_deck_result.append(float(sub_df.loc[df['Method'] == 'Hot deck'][criteria].values[0]))
            criteria_bar_plotter(KNN_result=KNN_result, RNN_result=RNN_result, LOCF_result=LOCF_result,
                                 Hot_deck_result=Hot_deck_result, criteria=criteria, feature=feature,
                                 gap_indicators=gap_indicators)


if __name__ == "__main__":
    df = load_csv('Results_Updated_Hot_deck.csv', delimiter=';')
    criteria_list = ['Mean squared error','Variance error','Kurtosis error','Skewness error','Percent bias','Maximum error','Mean error','Median error']
    get_result_per_column_and_gap_criteria(df, criterias=criteria_list)
