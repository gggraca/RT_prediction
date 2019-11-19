import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.metrics import mean_squared_error
from sklearn.cross_decomposition import PLSRegression
from sklearn.preprocessing import StandardScaler


'''
my_train_test_split function is based on pandas library
input: length: amount of data
       fold_num: number of folding
       full_data : panda dataframe 
'''


def my_train_test_split(length, fold_num, full_data):
    test_size = length // fold_num
    index_list = np.arange(test_size * fold_num).reshape(test_size, fold_num)
    for i in range(fold_num):
        np.random.shuffle(index_list[i, :])

    for y in range(fold_num):
        test_data = DataFrame()
        train_data = DataFrame()
        for x in range(test_size):
            test_data = test_data.append(full_data.iloc[index_list[x, y]], ignore_index=True)

        train_data = full_data.drop(index_list[:, y])
        test_data.to_csv("test/test_%s.csv" % y)
        train_data.to_csv("train/train_%s.csv" % y)

    print("the data is successfully divided.")


'''
my_cross_validation function 
input: model:machine learning model
       num_fold: number of folding
output:RMSE score for ten times
'''
def my_cross_validation(model,num_fold):
    score_list = list()
    for index in range(num_fold):
        # read the full data
        test_data = pd.read_csv('test/test_%s.csv' % index)
        test_data['Time'] = test_data['Time'] * 60
        test_data_p = test_data.drop("Time", axis=1)
        test_data_p = test_data_p.drop("Name", axis=1)
        test_data_p = test_data_p.drop("metabolite class", axis=1)
        # read data
        train_data = pd.read_csv('train/train_%s.csv' % index)
        train_data['Time'] = train_data['Time'] * 60
        train_data_p = train_data.drop("Time", axis=1)
        train_data_p = train_data_p.drop("Name", axis=1)
        train_data_p = train_data_p.drop("metabolite class", axis=1)

        scaler1 = StandardScaler()
        scaler1.fit(test_data_p)
        test_data_p = scaler1.transform(test_data_p)

        scaler2 = StandardScaler()
        scaler2.fit(train_data_p)
        train_data_p = scaler2.transform(train_data_p)

        model.fit(train_data_p, train_data['Time'])
        pre_data = model.predict(test_data_p)
        score_list.append(np.sqrt(mean_squared_error(test_data['Time'], pre_data)))

    return score_list


full_data1 = pd.read_csv('full_list_property.csv')
length1 = len(full_data1['Time'])
fold_num1 = 10
my_train_test_split(length1,fold_num1,full_data1)

model1 = PLSRegression(n_components=3)
score = (my_cross_validation(model1,10))
print(score)
