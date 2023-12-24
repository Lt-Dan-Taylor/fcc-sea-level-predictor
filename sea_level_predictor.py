import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  plt.figure(figsize=(10, 8))

  plt.scatter(df['Year'],
              df['CSIRO Adjusted Sea Level'],
              color='royalblue',
              alpha=0.6,
              s=70)

  # Create first line of best fit
  lin_reg = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
  to_2050 = range(df['Year'].min(), 2051)

  plt.plot(to_2050,
           lin_reg.slope * to_2050 + lin_reg.intercept,
           color='darkorange',
           linewidth=4)

  # Create second line of best fit
  df_2000 = df[df['Year'] >= 2000]

  lin_reg_2000 = linregress(x=df_2000['Year'],
                            y=df_2000['CSIRO Adjusted Sea Level'])
  _2000_to_2050 = range(df_2000['Year'].min(), 2051)

  plt.plot(_2000_to_2050,
           lin_reg_2000.slope * _2000_to_2050 + lin_reg_2000.intercept,
           color='crimson',
           linewidth=4,
           linestyle='dashed')

  # Add labels and title
  plt.xlabel('Year', fontsize=15, labelpad=5)
  plt.ylabel('Sea Level (inches)', fontsize=15, labelpad=5)
  plt.title('Rise in Sea Level', fontsize=20, pad=5)
  plt.tick_params(axis='both', which='both', labelsize=12, pad=5, width=1.5)

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
