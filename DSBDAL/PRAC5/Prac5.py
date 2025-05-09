# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Load the dataset
df = pd.read_csv(r"C:\Users\Yash\Desktop\DSBDAL\PRAC5\Social_Network_Ads.csv")

# Step 3: Initialize and inspect
print("First 5 rows of the dataset:\n", df.head())
print("\nGender Column:\n", df['Gender'])

# Step 4: Data Preprocessing
# Convert categorical to numerical
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})

# Check for null values
print("\nNull values:\n", df.isnull().sum())

# Data types
print("\nData types:\n", df.dtypes)

# Covariance Matrix (Optional step, just an idea)
print("\nCovariance Matrix:\n", df.cov(numeric_only=True))

# Step 4.1: Divide dataset into X and Y
x = df.drop(['Age'], axis=1)  # Independent features
y = df['Age']                 # Dependent variable

# Step 4.2: Split into train and test sets
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.25, random_state=0)

# Step 4.3: Feature Scaling
from sklearn.preprocessing import StandardScaler
st_x = StandardScaler()
xtrain = st_x.fit_transform(xtrain)
xtest = st_x.transform(xtest)

# Step 5: Train using Logistic Regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(xtrain, ytrain)

# Step 6: Prediction
y_pred = classifier.predict(xtest)
print("\nPredicted values:\n", y_pred)

# Step 7 & 8: Evaluation
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(ytest, y_pred)
acc = accuracy_score(ytest, y_pred)

print("\nConfusion Matrix:\n", cm)
print("\nAccuracy Score:", acc)
