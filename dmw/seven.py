
#Implement logistic regression method to make prediction based on the sample data set using python

# Step 1: Import libraries
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Step 2: Sample dataset
# X = study hours, Y = pass(1) or fail(0)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
Y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Step 3: Create the logistic regression model
model = LogisticRegression()

# Step 4: Train the model
model.fit(X, Y)

# Step 5: Predict if a student studying 3 hours will pass or fail_
test = [[3]]
prediction = model.predict(test)
print("Prediction for 3 hours of study:", "Pass" if prediction[0] == 1 else "Fail")

# Step 6: Plot the result
plt.scatter(X, Y, color='blue', label='Actual Data')
plt.plot(X, model.predict_proba(X)[:, 1], color='red', label='Probability Curve')
plt.xlabel("Study Hours")
plt.ylabel("Probability of Passing")
plt.title("Logistic Regression Example")
plt.legend()
plt.grid()
plt.show()
