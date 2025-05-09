# 1. Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import preprocessing

# 2. Load the dataset
df = pd.read_csv(r"C:\Users\Yash\Desktop\DSBDAL\PRAC3\acdemic_data.csv")  # Update path if needed

# 3. Display the dataframe
print("Full Dataset:\n", df)

# -------------------------------
# 4. Statistical Operations
# -------------------------------

# MEAN
print("\n--- Mean ---")
print(df.mean(numeric_only=True))  # Mean of all numeric columns
print("\nMean of 'SPOS':", df['SPOS'].mean())  # Example: Mean of SPOS column
print("Row-wise Mean (first 4 rows):", df.mean(axis=1, numeric_only=True)[0:4])

# MEDIAN
print("\n--- Median ---")
print(df.median(numeric_only=True))  # Median of all numeric columns
print("Median of 'DSBDA':", df['DSBDA'].median())
print("Row-wise Median (first 4 rows):", df.median(axis=1, numeric_only=True)[0:4])

# MODE
print("\n--- Mode ---")
print(df.mode(numeric_only=True))  # Mode of all numeric columns
print("Mode of 'WT':", df['WT'].mode()[0])  # First mode value

# MINIMUM
print("\n--- Minimum ---")
print(df.min(numeric_only=True))
print("Min of 'SPOS':", df['SPOS'].min())

# MAXIMUM
print("\n--- Maximum ---")
print(df.max(numeric_only=True))
print("Max of 'DA':", df['DA'].max())

# STANDARD DEVIATION
print("\n--- Standard Deviation ---")
print(df.std(numeric_only=True))
print("Std deviation of 'WT':", df['WT'].std())

# GROUP BY
print("\n--- Group By: Average SPOS by Gender ---")
grouped = df.groupby(['Gender'])['SPOS'].mean()
print(grouped)

# -------------------------------
# 5. One-Hot Encoding
# -------------------------------

print("\n--- One Hot Encoding ---")
enc = preprocessing.OneHotEncoder()
encoded = enc.fit_transform(df[['Gender']]).toarray()

# Create DataFrame for encoded values
enc_df = pd.DataFrame(encoded, columns=enc.get_feature_names_out(['Gender']))

# Join with original dataframe
df_encoded = df.join(enc_df)
print("\nEncoded DataFrame:\n", df_encoded)

