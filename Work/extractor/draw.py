# draw
# Created by JKChang
# 2019-03-05, 09:44
# Tag:
# Description: draw pie chart

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def func(pct, allvals):
    absolute = int(pct / 100. * np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)


def drawSimpleGraph(dataFrame, title):
    col = dataFrame.columns
    fig1, ax = plt.subplots()
    explode = (0, 0.1)
    wedges, texts, autotexts = ax.pie(dataFrame[col[1]], labels=dataFrame[col[0]], wedgeprops=dict(width=0.7),
                                      startangle=-20,
                                      autopct=lambda pct: func(pct, dataFrame[col[1]]))

    ax.axis('equal')
    ax.set_title(title)
    plt.show()


df = pd.read_csv('./DEM.tsv', sep='\t')
df = df['1D/2D'].value_counts().to_frame().reset_index()
df.columns = ['NMR 1D/2D', 'Count']
drawSimpleGraph(df, 'NMR Techniques')
