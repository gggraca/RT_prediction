from __future__ import division
import numpy as np
import scipy.optimize as opt
import pandas as pd
from sklearn.metrics import mean_absolute_error,median_absolute_error,r2_score,mean_squared_error


def sigmoid_fitting(train_data,test_data,score_function="RMSE"):
    # sigmoid function
    def sigmoid(x, a, b, c, d):
        return a / (1. + np.exp(-c * (x - d))) + b

    time_train = train_data['Time']
    time_train = np.array(time_train)
    hydrophobicity_train = train_data['MolLogP']
    hydrophobicity_train = np.array(hydrophobicity_train)
    (a1, b1, c1, d1), _ = opt.curve_fit(sigmoid, hydrophobicity_train, time_train)

    time_test = test_data['Time']
    time_test = np.array(time_test)
    hydrophobicity_test = test_data['MolLogP']
    hydrophobicity_test = np.array(hydrophobicity_test)

    pre_data = sigmoid(hydrophobicity_test, a1, b1, c1, d1)

    if score_function == "RMSE":
        return np.sqrt(mean_squared_error(time_test * 60, pre_data * 60))
    elif score_function == "MAE":
        return median_absolute_error(time_test*60,pre_data*60)
    elif score_function == "r2_score":
        return r2_score(time_test*60,pre_data*60)
    elif score_function == "MAE_normalized":
        return median_absolute_error(time_test*60,pre_data*60)/max(time_test)


