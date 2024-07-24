import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    years_predicted_1 = np.arange(df['Year'].min(), 2051)
    years_predicted_2 = np.arange(2000, 2051)
    # Create scatter plot
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)
    # Create first line of best fit
    slope, intercep, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    sea_levels_predicted = slope*(years_predicted_1) + intercep
    plt.plot(years_predicted_1, sea_levels_predicted)

    # Create second line of best fit
    slope2, intercep2, r_value2, p_value2, std_err2 = linregress(df[(df['Year'] >= 2000) & (df['Year'] <= df['Year'].max())]['Year'], df[(df['Year'] >= 2000) & (df['Year'] <= df['Year'].max())]['CSIRO Adjusted Sea Level'])
    sea_levels_predicted_2 = slope2*years_predicted_2 + intercep2
    plt.plot(years_predicted_2, sea_levels_predicted_2)

    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()