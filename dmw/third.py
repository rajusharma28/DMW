# Build a decision tree classifier using python’s scikit learn library to predict customer churn based on historical data.


import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Create dataset
data = pd.DataFrame({
    'Age': [25, 30, 35, 40, 45, 50],
    'Balance': [20000, 30000, 400000, 120000, 50000, 60000],
    'Active_Member': [1, 0, 1, 0, 0, 1],
    'Churn': [0, 1, 0, 1, 1, 0]
})

# Split data
X = data[['Age', 'Balance', 'Active_Member']]
Y = data['Churn']

# Train model
model = DecisionTreeClassifier(random_state=0)
model.fit(X, Y)

# Create figure
plt.figure(figsize=(10, 7))
plot_tree(
    model,
    feature_names=['Age', 'Balance', 'Active_Member'],
    class_names=['Not Churn', 'Churn'],
    filled=True,
    rounded=True,
    fontsize=10
)

plt.title("Decision Tree Classifier for Customer Churn", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
