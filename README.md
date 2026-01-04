# Sea Level Predictor

## Project Objective

This project analyzes global sea level change data since 1880 and predicts future sea level rise through the year 2050. Using data science techniques, we create visualizations and predictive models to understand historical trends and project future changes.

## Tools & Libraries Used

- **Pandas**: Data loading and manipulation from CSV files
- **Matplotlib**: Data visualization and plotting
- **SciPy (linregress)**: Linear regression analysis for trend lines
- **NumPy**: Numerical computations via Pandas/SciPy

## Key Tasks Performed

1. **Data Import**: Loaded EPA sea level data from `epa-sea-level.csv` using Pandas
2. **Visualization**: Created scatter plot of historical sea level measurements (1880-2013)
3. **Linear Regression Analysis**: 
   - Calculated line of best fit using all available data (1880-2013)
   - Calculated separate line of best fit using only recent data (2000-2013)
4. **Predictions**: Extended both regression lines to the year 2050 to show projected sea level rise
5. **Plot Formatting**: Added proper labels, title, and axis ticks for clarity

## Dataset Source

Global Average Absolute Sea Level Change (1880-2014) from datahub.io/core/sea-level-rise

- **Source**: US Environmental Protection Agency (EPA)
- **Data Providers**: CSIRO (2015), NOAA (2015)
- **Time Range**: 1880-2013
- **Unit**: Inches (relative to 1993 baseline)

## Installation

pip install -r requirements.txt

## Testing

python main.py
