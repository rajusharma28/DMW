# 🎯 Title: Feature Selection using Variance Threshold and Correlation Analysis

import pandas as pd
from sklearn.feature_selection import VarianceThreshold

# Step 1: Create Sample Data
data = pd.DataFrame({
    'A': [1, 1, 1, 1, 1],     # Low variance
    'B': [2, 3, 4, 5, 6],
    'C': [10, 20, 30, 40, 50]
})

print("Original Data:")
print(data)

# Step 2: Apply Variance Threshold
selector = VarianceThreshold(threshold=0.1)
new_data = selector.fit_transform(data)

# Get column names that remain after removing low variance columns
remaining_columns = data.columns[selector.get_support()]
data_low_variance = pd.DataFrame(new_data, columns=remaining_columns)

print("\nAfter Removing Low Variance Columns:")
print(data_low_variance)

# Step 3: Correlation Analysis
print("\nCorrelation between columns:")
print(data_low_variance.corr())


# (In this small dataset, B and C are highly correlated)
data_low_variance.drop('B', axis=1, inplace=True)

print("\nAfter Removing Correlated Column:")
print(data_low_variance)
