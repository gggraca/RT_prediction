import pandas as pd
from scipy import stats
import numpy as np


def pearson_selection(input_data,threhold):
    first = 0
    while first < len(list(input_data.columns)):
        variable = list(input_data.columns)
        # print(variable)
        value_list = []
        for i in range(1 + first, len(variable)):
            if stats.pearsonr(input_data[variable[first]], input_data[variable[i]])[0] >= threhold:
                value_list.append(variable[i])

        for value in value_list:
            input_data = input_data.drop(value, axis=1)
        print(value_list)
        first = first + 1

    return input_data


def std_selection(input_data1,threhold1):
    variable1 = list(input_data1.columns)
    # print(variable)
    value_list1 = []
    for i in range(len(variable1)):
        if np.std(input_data1[variable1[i]]) <= threhold1:
            value_list1.append(variable1[i])

    for value in value_list1:
        input_data1 = input_data1.drop(value, axis=1)
    print(value_list1)

    return input_data1




