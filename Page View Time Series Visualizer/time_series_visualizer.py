import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
from datetime import datetime
register_matplotlib_converters()

df = pd.read_csv('fcc-forum-pageviews.csv', delimiter=',', index_col='date', parse_dates=True)

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
    ]

def draw_line_plot():    
    fig, ax = plt.subplots(figsize = (12, 6))
    ax.plot(df.index, df['value'], color = 'red')

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['year'] = [d.year for d in df.index]
    df['month'] = [d.strftime('%B') for d in df.index]
    df['month'] = pd.Categorical(df['month'], categories=[
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], ordered=True)
    
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    fig, ax = plt.subplots(figsize = (12, 6))
    df_bar.plot(kind='bar', ax=ax)

    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    ax.legend(title='Months', labels = month_names)
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 6))
    sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    sns.boxplot(data=df_box, x='month', y='value', order=month_order, ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
