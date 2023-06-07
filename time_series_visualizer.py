import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('./fcc-forum-pageviews.csv', 
                 sep=',', 
                 parse_dates=[0],
                 index_col=[0]
                )

# Clean data
df = df[ (df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975)) ]

#print(df, len(df))

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(25, 9))
    plt.plot(df.index.to_numpy(), df['value'].to_numpy())
    plt.xlabel('Date', {'size': 16} )
    plt.ylabel('Page Views', {'size': 16})
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', {'size': 20 })

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month
    df_bar = df_bar.groupby(by=['year', 'month']).mean()
    
    df_bar = df_bar.unstack()
    # Draw bar plot
    #fig = plt.figure(figsize=(11, 9))
    fig = df_bar.plot(kind ="bar", figsize=(12,9)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 
              'November', 'December' ]
    plt.legend(labels=months, loc=0, title='Months', borderpad=1)
    
    """
    plot = sns.catplot(data=df_bar, x='year', y='value', hue='month', kind='bar', palette="pastel", edgecolor=".6", 
                     hue_order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 
                                'November', 'December' ], facet_kws={'legend_out': True} )
    
    #plot.set_axis_labels("Years", "Average Page Views")
    plot._legend.set_title('Months')
    plot.set(title='Monthly freeCodeCamp Forum Page Views 5/2016-12/2019',
             xlabel='Years',
             ylabel='Average Page Views')
    #plot.legend(title='Months')
    #plot._legend.set_text(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 
    #                            'November', 'December' ])
    fig = plot._figure
    """

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    # Draw box plots (using Seaborn)
    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 
              'Nov', 'Dec' ]
    plt.rcParams.update({'font.size': 20})
    fig, ax = plt.subplots(1, 2)
    
    fig.set_figheight(11)
    fig.set_figwidth(30)
    sns.boxplot(data=df_box, x='year', y='value', ax=ax[0])
    sns.boxplot(data=df_box, x='month', y='value', ax=ax[1], order=order )
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
