import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv', delimiter=',')

# 2
IBM = df['weight'] / (df['height']/100)**2
df['overweight'] = (IBM > 25).astype('int')

# 3
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7
    cat_plot = sns.catplot(df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar')
    cat_plot.set_axis_labels('variable','total')

    # 8
    fig = cat_plot.fig
    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():

    height_low = df['height'].quantile(0.025)
    height_high = df['height'].quantile(0.975)
    weight_low = df['weight'].quantile(0.025)
    weight_high = df['weight'].quantile(0.975)
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= height_low) &
        (df['height'] <= height_high) &
        (df['weight'] >= weight_low) &
        (df['weight'] <= weight_high)
    ]
    # 12
    corr = df_heat.corr().round(1).astype(float)
    # 13
    mask = np.triu(np.ones_like(corr, dtype='bool'), k=0)

    # 14
    fig, ax = plt.subplots(figsize = (12, 10))

    # 15

    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, linewidths=0.5, ax=ax)

    # 16
    fig.savefig('heatmap.png')
    
    return fig

