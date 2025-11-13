
#Implement K-means clustering algorithm in python using scikit learn to group customers based on their purchasing behaviour.
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Create a sample dataset
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Annual_Income': [15, 16, 17, 18, 19, 40, 42, 43, 44, 45],
    'Spending_Score': [39, 81, 6, 77, 40, 76, 6, 94, 3, 72]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Select features for clustering
X = df[['Annual_Income', 'Spending_Score']]

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Display cluster results
print(df)

# Plot clusters
plt.scatter(df['Annual_Income'], df['Spending_Score'], c=df['Cluster'], cmap='rainbow')
plt.xlabel('Annual Income (in thousands)')
plt.ylabel('Spending Score (1–100)')
plt.title('Customer Segments based on Purchasing Behaviour')
plt.show()
