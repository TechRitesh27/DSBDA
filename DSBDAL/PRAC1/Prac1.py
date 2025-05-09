import pandas as pd
import numpy as np

# Load dataset with correct encoding
df = pd.read_csv(r"C:\Users\Yash\Desktop\DSBDAL\PRAC1\Zomato_data.csv", encoding='latin1')

# Display first 5 rows
print("First 5 rows:\n", df.head())

# Basic info
print("\nShape:", df.shape)
print("\nColumns:", df.columns)
print("\nInfo:")
print(df.info())

# Missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Fill missing values with 0
df.fillna(0, inplace=True)

# Replace '?' with NaN
df.replace("?", np.nan, inplace=True)

# Ensure 'votes' is numeric
df['votes'] = pd.to_numeric(df['votes'], errors='coerce').fillna(0).astype(int)

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe(include='all'))

# Sort by votes descending
df.sort_values('votes', ascending=False, inplace=True)

# Filter restaurants with more than 500 votes
filtered_df = df[df['votes'] > 500]
print("\nRestaurants with votes > 500:\n", filtered_df)

# Grouping by 'listed_in' and finding average votes
if 'listed_in' in df.columns:
    grouped = df.groupby('listed_in')['votes'].mean()
    print("\nAverage Votes by Listing Type:\n", grouped)

# Reset index
df.reset_index(drop=True, inplace=True)
