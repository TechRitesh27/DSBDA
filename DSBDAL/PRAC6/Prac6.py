# Step 1: Import libraries and create aliases
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 2 & 3: Load and initialize the data frame
df = pd.read_csv(r'C:\Users\Yash\Desktop\DSBDAL\PRAC6\Social_Network_Ads.csv')
print("First 5 rows of dataset:")
print(df.head())

# Step 4: Data Preprocessing

# Convert categorical to numerical if needed (Gender column)
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])  # Male=1, Female=0

# Check for null values
print("\nChecking for null values:")
print(df.isnull().sum())

# Divide the dataset into independent (X) and dependent (Y) variables
# We'll use 'Gender', 'Age', and 'EstimatedSalary' to predict 'Purchased'
X = df[['Gender', 'Age', 'EstimatedSalary']]
Y = df['Purchased']

# Split the dataset into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# Feature scaling (important for salary/age range differences)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 5: Train the model using Naive Bayes
from sklearn.naive_bayes import GaussianNB

gaussian = GaussianNB()
gaussian.fit(X_train, y_train)

# Step 6: Predict values for the test set
Y_pred = gaussian.predict(X_test)

# Step 7: Evaluate model performance
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

accuracy = accuracy_score(y_test, Y_pred)
precision = precision_score(y_test, Y_pred, average='micro')
recall = recall_score(y_test, Y_pred, average='micro')

print("\nModel Evaluation:")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

# Step 8: Confusion Matrix
cm = confusion_matrix(y_test, Y_pred)
print("\nConfusion Matrix:")
print(cm)

# Optional: Visualize the confusion matrix
import seaborn as sns

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
