import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():

    # Read data from file
    df = pd.read_csv('/Users/bayusedana/Documents/GitHub/Python-Projects/Projects/Sea Level Predictor/epa-sea-level.csv')
    
    # Scatter plot
    years = df['Year']
    sea_levels = df['CSIRO Adjusted Sea Level']

    plt.figure(figsize=(10, 6))
    plt.scatter(years, sea_levels, label='Data', color='blue', alpha=0.7)

    # First line of best fit (all data)
    slope, intercept, _, _, _ = linregress(years, sea_levels)
    all_years = np.arange(1880, 2051)
    all_predicted_sea_levels = slope * all_years + intercept
    plt.plot(all_years, all_predicted_sea_levels, color='red', label='Best Fit (All Data)')

    # Second line of best fit (data from 2000 onwards)
    df_2000 = df[df['Year'] >= 2000]
    years_post_2000 = df_2000['Year']
    sea_levels_post_2000 = df_2000['CSIRO Adjusted Sea Level']

    slope_2000, intercept_2000, _, _, _ = linregress(years_post_2000, sea_levels_post_2000)
    future_years_2000 = np.arange(2000, 2051)
    future_predicted_sea_levels_2000 = slope_2000 * future_years_2000 + intercept_2000
    plt.plot(future_years_2000, future_predicted_sea_levels_2000, color='green', label='Best Fit (2000 Onwards)')

    # Labels, legend, grid, and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True)

    # Save plot and show
    plt.tight_layout()
    plt.savefig('sea_level_plot.png')
    plt.show()

    # Return plot axes for testing
    return plt.gca()

draw_plot()
