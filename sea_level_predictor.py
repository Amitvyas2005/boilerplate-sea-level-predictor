import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create scatter plot
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.7)
    
    # Create first line of best fit using all data
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = list(df['Year']) + list(range(2014, 2051))
    line1_y = [slope1 * year + intercept1 for year in years_extended]
    ax.plot(years_extended, line1_y, color='red', label='Best fit (1880-2013)')
    
    # Create second line of best fit using data from 2000 onwards
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_2000_to_2050 = list(df_2000['Year']) + list(range(df_2000['Year'].max() + 1, 2051))
    line2_y = [slope2 * year + intercept2 for year in years_2000_to_2050]
    ax.plot(years_2000_to_2050, line2_y, color='green', label='Best fit (2000-2050)')
    
    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return ax
