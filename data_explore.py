from numpy import mean, median, ptp, var, std
from scipy.stats import mode
from matplotlib import pyplot as plt


def descriptive_statistcs(data, type):
    if type == "mean":
        return mean(data)
    elif type == "median":
        return median(data)
    elif type == "mode":
        return mode(data)
    elif type == "range":
        return ptp(data)
    elif type == "variance":
        return var(data)
    elif type == "standard_variance":
        return std(data)
    elif type == "variable_coefficient":
        return mean(data)/std(data)

#scattter graph
def scatter(data1, data2):
    plt.scatter(data1, data2)
    plt.show()
