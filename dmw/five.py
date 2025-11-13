

#Implement a linear regression method to make predictions based on the sample data set using python.
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Input and output data
x = np.array([[1], [2], [3], [4], [5]])  # study hours
y = np.array([20, 40, 60, 80, 100])      # marks

# Create and train model
model = LinearRegression()
model.fit(x, y)

# Predict for 6 hours
predicted = model.predict([[6]])
print("Predicted marks for 6 hours:", predicted[0])

# Plot
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, model.predict(x), color='red', label='Regression Line')
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Linear Regression Example")
plt.legend()
plt.show()
