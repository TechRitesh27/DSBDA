# Step 1: Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Step 2: Define the independent variable (x) and dependent variable (y)
x = np.array([95, 85, 80, 70, 60])
y = np.array([85, 95, 70, 65, 70])

# Step 3: Create a Linear Regression model using np.polyfit
model = np.polyfit(x, y, 1)  # 1 indicates linear
print("Model Coefficients (slope, intercept):", model)

# Step 4: Predict y for a single value (e.g., x = 65)
predict = np.poly1d(model)
predicted_y = predict(65)
print("\nPredicted y for x = 65:", predicted_y)

# Step 5: Predict y for all values in x
y_pred = predict(x)
print("\nPredicted y values for all x:", y_pred)

# Step 6: Evaluate the model using R² score
r2 = r2_score(y, y_pred)
print("\nR² Score:", r2)

# Step 7: Plotting the regression line and data points
y_line = model[1] + model[0] * x

plt.figure(figsize=(8, 5))
plt.plot(x, y_line, color='red', label='Regression Line')  # Regression line
plt.scatter(x, y_pred, label='Predicted Points')           # Predicted points
plt.scatter(x, y, color='red', label='Actual Points')      # Actual points
plt.title("Linear Regression Model")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.grid(True)
plt.show()
