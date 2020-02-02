import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.style.use('ggplot')
from sklearn.decomposition import PCA


def distribution_plot(data,size,list):
    fig, axes = plt.subplots(size, size, figsize=(6, 4), sharex=False, sharey=False)
    num = 0
    for i in range(size):
        for j in range(size):
            #sns.kdeplot(data[list[num]], ax=axes[i, j])
            sns.distplot(data[list[num]], ax=axes[i, j])
            num = num + 1
    plt.savefig("result.png")


def pca_class(X,Y,num):

    pca = PCA(n_components=num)
    X_r = pca.fit(X).transform(X)

    plt.figure()
    target_names = set(Y)
    lw = 2

    for i, target_name in zip(target_names, target_names):
        plt.scatter(X_r[Y == i, 0], X_r[Y == i, 1], alpha=.8, lw=lw,
                    label=target_name)
    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.title('PCA of subgroup of lipids')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.savefig("PCA_class.png")



