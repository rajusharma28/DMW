from sklearn.feature_selection import VarianceThreshold

import pandas as pd
import numpy as np

# data =pd.DataFrame({
#     'A':[1,1,1,1,1],
#     'B':[2,3,4,5,6],
#     'c':[5,5,5,5,5],
#     'D':[10,15,20,25,30]
# })

# selector = VarianceThreshold(threshold=0.0)
# reduced_data =selector.fit_transform(data)

# print("Original Coliumns:" ,data.columns.tolist())
# print("Remaing features after Variance Thresholding:" ,data.columns[selector.get_support()].tolist())



# ___++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

data =pd.DataFrame({
    'Height':[150,160,170,180,190],
    'weight':[50,55,60,70,80],
    'Age':[25,30,35,40,45],
    'Income':[30,40,45,60,75]
})

# Compute correlation matrix
corr_matrix = data.corr()

print("Correlation Matrix:")
print(corr_matrix)


upper_tri =corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))


#find a colonums for drop

to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > 0.9)]
print("\nHighly correlated features to drop:", to_drop)



reduced_data = data.drop(columns=to_drop)
print("\nReduced Dataset:")
print(reduced_data)


#444444444444444444444444444444444444444444444
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Create dataset
data = pd.DataFrame({
    'Age': [25, 30, 35, 40, 45, 50],
    'Balance': [20000, 30000, 40000, 10000, 12000, 50000],
    'Active_Member': [1, 0, 1, 0, 0, 1],
    'Churn': [0, 1, 0, 1, 1, 0]
})

# Split data
X = data[['Age', 'Balance', 'Active_Member']]
y = data['Churn']

# Train model
model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

# Create figure 
plt.figure(figsize=(12, 8))
plot_tree(model,
          feature_names=['Age', 'Balance', 'Active_Member'],
          class_names=['Not Churn', 'Churn'],
          filled=True,
          rounded=True,
          fontsize=10)

# Add title and layout
plt.title("Decision Tree Classifier for Customer Churn", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
