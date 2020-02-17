from __future__ import division
import numpy as np
import scipy.optimize as opt


class SigmoidFitting:
    def __init__(self):

        self.a1 = None
        self.b1 = None
        self.c1 = None
        self.d1 = None

    def fit(self, x, y):
        def sigmoid(x, a, b, c, d):
            return a / (1. + np.exp(-c * (x - d))) + b
        y = np.array(y)
        x = np.array(x)
        (self.a1, self.b1, self.c1, self.d1), _ = opt.curve_fit(sigmoid, x, y)

    def predict(self, x):

        x = np.array(x)
        pre_data =self.a1 / (1. + np.exp(-self.c1 * (x - self.d1))) + self.b1
        return pre_data

