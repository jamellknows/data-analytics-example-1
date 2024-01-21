# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Generate synthetic data
np.random.seed(42)
data_a = np.random.normal(loc=30, scale=10, size=100)
data_b = np.random.normal(loc=35, scale=12, size=100)

# Create a Pandas DataFrame
df = pd.DataFrame({'Group_A': data_a, 'Group_B': data_b})

# Display the first few rows of the DataFrame
print("DataFrame Head:")
print(df.head())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Data Visualization using Matplotlib and Seaborn
plt.figure(figsize=(10, 6))
sns.histplot(data=df, kde=True)
plt.title('Distribution of Data for Group A and Group B')
plt.xlabel('Values')
plt.ylabel('Frequency')

# Save the plot as an image
plt.savefig('distribution_plot.png')
plt.show()

# Boxplot to compare the two groups
plt.figure(figsize=(8, 5))
sns.boxplot(data=df)
plt.title('Boxplot Comparison of Group A and Group B')
plt.ylabel('Values')

# Save the boxplot as an image
plt.savefig('boxplot_comparison.png')
plt.show()

# Save the DataFrame to a CSV file
df.to_csv('data_analysis_results.csv', index=False)

# Statistical testing using SciPy
t_stat, p_value = ttest_ind(df['Group_A'], df['Group_B'])
print("\nIndependent t-test:")
print(f'T-statistic: {t_stat}')
print(f'P-value: {p_value}')

# Display a conclusion based on the p-value
alpha = 0.05
if p_value < alpha:
    print("\nReject the null hypothesis. There is a significant difference between the groups.")
else:
    print("\nFail to reject the null hypothesis. There is no significant difference between the groups.")
