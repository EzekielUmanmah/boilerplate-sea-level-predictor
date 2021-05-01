import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(14,8))
    df.plot(kind='scatter', x='Year', y='CSIRO Adjusted Sea Level', ax=ax)
    
    # Create first line of best fit
    years_extended = np.arange(x.min(), 2051)
    result = linregress(x, y)
    ax.plot(years_extended, result.intercept + result.slope*years_extended, 'g', label='line of best fit')
    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    x = df2['Year']
    y = df2['CSIRO Adjusted Sea Level']
    years_extended = np.arange(x.min(), 2051)
    result = linregress(x, y)
    ax.plot(years_extended, result.intercept + result.slope*years_extended, 'r', label='2nd line')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()