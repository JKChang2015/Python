# BBSRC
# Created by JKChang
# 2019-01-31, 21:26
# Tag:
# Description: split studyID in different rows

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('./resources/MTBLS Curation Status Log.csv')
df = df.dropna(subset=['StudySize'])
df_split = pd.DataFrame(columns=['ACC', 'StudySize', 'Status', 'Releasedate', 'SubmissionDate',
                                 'UserName', 'Technique', 'AccShort', 'StudyID', 'UpdateDate',
                                 'nmr_size', 'ms_size', 'Empty?', '150'])

# split the Techniques into different rows
for index, row in df.iterrows():
    try:
        temp = row.copy()
        techniques = row['Technique'].split(';')
        for technique in techniques:
            temp['Technique'] = technique
            df_split.loc[len(df_split)] = temp
    except:
        pass
# df_split.to_csv('splited.tsv', sep='\t', encoding='utf-8', index=False)

# count the Techniques
df_count = df_split['Technique'].value_counts()
df_count = df_count.to_frame().reset_index()
df_count.columns = ['Technique', 'Count']

# load full name of the techniques
names = pd.read_csv('./resources/full name.csv')
name_pair = dict(zip(names['Study type'], names['Full Name']))
df_count['Full Name'] = df_count['Technique'].map(name_pair)
# df_count.to_csv('counted.tsv', sep='\t', encoding='utf-8', index=False)

# group count
group = dict(zip(names['Study type'], names['Classify']))
temp = df_split['Technique'].map(group, na_action=None)
temp = temp.fillna(value='Uannotated')

df_group = temp.value_counts()
df_group = df_group.to_frame().reset_index()
df_group.columns = ['groupName', 'Count']

# # draw graph
#
drop_sum = df_group[df_group.Count < 0.03 * np.sum(df_group.Count)].sum()
df_group = df_group[df_group.Count >= 0.03 * np.sum(df_group.Count)]
new = {'groupName': 'Other', 'Count': drop_sum[1]}
df_group.loc[len(df_group)] = new

fig, ax = plt.subplots(figsize=(18, 18), subplot_kw=dict(aspect="equal"))


def func(pct, allvals):
    absolute = int(round(pct / 100. * np.sum(allvals)))
    return "{:.1f}%\n({:d})".format(pct, absolute)


wedges, texts, autotexts = ax.pie(df_group['Count'], wedgeprops=dict(width=0.5), startangle=-40,
                                  autopct=lambda pct: func(pct, df_group['Count']), textprops={'fontsize': 16})

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center", fontsize='12')

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1) / 2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(df_group['groupName'][i], xy=(x, y), xytext=(1.1 * np.sign(x), 1.1 * y),
                horizontalalignment=horizontalalignment, **kw)

ax.set_title("Metabolights Study Techniques", fontsize=26)

plt.show()
