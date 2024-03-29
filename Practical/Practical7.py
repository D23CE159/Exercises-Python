import pandas as pd

# Load data into a DataFrame
data = pd.read_csv('titanic.csv')

# Display the first few rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(data.head())

# Display basic info about the DataFrame
print("\nInfo about the DataFrame:")
print(data.info())

# Summary statistics
print("\nSummary statistics of numeric columns:")
print(data.describe())

# Mean of a specific column
mean_value = data['column_name'].mean()
print("\nMean of a specific column:", mean_value)

# Median of a specific column
median_value = data['column_name'].median()
print("\nMedian of a specific column:", median_value)

# Mode of a specific column
mode_value = data['column_name'].mode()[0]  # mode() returns a Series, so we select the first value
print("\nMode of a specific column:", mode_value)

# Correlation matrix
correlation_matrix = data.corr()
print("\nCorrelation matrix:")
print(correlation_matrix)

# Plotting
import matplotlib.pyplot as plt

# Histogram of a numeric column
data['numeric_column'].plot(kind='hist', bins=20, figsize=(8, 6))
plt.title('Histogram of Numeric Column')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

