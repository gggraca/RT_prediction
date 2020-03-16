import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.metrics import r2_score
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.patches as mpatches
matplotlib.style.use('ggplot')

#legend for lipid class
colors = ['pink', 'violet', 'cornflowerblue', 'darkturquoise','limegreen','darkorange','chocolate','firebrick','red']
labels = [ "Sterol Lipids [ST]","Sphingolipids [SP]","Glycerolipids [GL]","Glycerophospholipids [GP]"
    ,"Fatty Acyls [FA]","Amino acid derivative","Xenobiotic","Porphyrin metabolite","Vitamin"]
patches = [ mpatches.Patch(color=colors[i], label="{:s}".format(labels[i]) ) for i in range(len(colors)) ]

#color list for different lipid class
color_list = {
    "Sterol Lipids [ST]":"pink",
    "Sphingolipids [SP]":"violet",
    "Glycerolipids [GL]":"cornflowerblue",
    "Glycerophospholipids [GP]":"darkturquoise",
    "Fatty Acyls [FA]":"limegreen",
    "Amino acid derivative":"darkorange",
    "Xenobiotic":"chocolate",
    "Porphyrin metabolite":"firebrick",
    "Vitamin":"red"
}
data = pd.read_csv("svr_result_scaler.csv")
name = data['metabolite']
class1 = list(data['metabolite class'])
xs = data['Time']
ys = data['mean']
error=data['std']

'''
for i in range(140):
    plt.scatter(xs[i] ,ys[i] ,s=70, c = color_list[class1[i]],marker='.')
    plt.errorbar(xs[i], ys[i], yerr=error[i],ecolor="black",elinewidth=0.5)
plt.plot((700,0),(700,0),lw=0.3,c='black')
plt.xlabel("experimental retention time(seconds)")
plt.ylabel("predicted retention time(seconds)")

plt.legend(handles=patches,loc="lower right")
plt.show()
'''
print(r2_score(xs,ys))