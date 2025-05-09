# 1. Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from scipy import stats

# 2. Load dataset
df = pd.read_csv(r"C:\Users\Yash\Desktop\DSBDAL\PRAC2\acdemic_data.csv")

# 3. Display the data
print(df.head())

# 4. Checking for missing values
print("\nMissing values using isnull():\n", df.isnull())
print("\nMissing in each column:\n", df.isnull().sum())

# 5. Check not null values
print("\nNon-missing values using notnull():\n", df.notnull())

# 6. Filter rows with NaNs in a specific column (e.g., math score)
if "math score" in df.columns:
    nan_math = pd.isnull(df["math score"])
    print("\nRows with NaN in math score:\n", df[nan_math])

# 7. Label Encoding categorical column (e.g., gender)
if "gender" in df.columns:
    le = LabelEncoder()
    df["gender"] = le.fit_transform(df["gender"])

# 8. Replace specific values like "na" or "Na" with NaN
missing_values = ["Na", "na"]
df = pd.read_csv("acdemic_data.csv", na_values=missing_values)

# 9. Fill missing values
df.fillna(0, inplace=True)  # With 0
# Or fill with mean/median/std/min/max
if "math score" in df.columns:
    df["math score"].fillna(df["math score"].mean(), inplace=True)

# 10. Replace NaNs with a specific value
df.replace(to_replace=np.nan, value=-99, inplace=True)

# 11. Drop nulls
df.dropna()  # Drop rows with any NaNs
df.dropna(how='all')  # Drop rows if all values are NaN
df.dropna(axis=1)  # Drop columns with NaN

# 12. Detect outliers using Boxplot
cols = ['math score', 'reading score', 'writing score', 'placement score']
for col in cols:
    if col in df.columns:
        df.boxplot([col])
plt.show()

# 13. Detect outliers using Z-score
if "math score" in df.columns:
    z = np.abs(stats.zscore(df["math score"]))
    print("\nZ-scores:\n", z)
    threshold = 0.18
    outliers = np.where(z < threshold)
    print("\nSample Outliers (Z-Score < 0.18):\n", outliers)

# 14. Scatterplot for visual outlier detection
if "placement score" in df.columns and "placement offer count" in df.columns:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['placement score'], df['placement offer count'])
    plt.title("Scatterplot: Placement Score vs Offer Count")
    plt.xlabel("Placement Score")
    plt.ylabel("Placement Offer Count")
    plt.show()

# 15. Histogram of math score
if "math score" in df.columns:
    df['math score'].plot(kind='hist', title='Histogram of Math Score')
    plt.show()

    # Log transform and plot
    df['log_math'] = np.log10(df['math score'].replace(0, np.nan).dropna())
    df['log_math'].plot(kind='hist', title='Histogram of Log(Math Score)')
    plt.show()

# 16. Save final processed dataset
df.to_csv("processed_acdemic_data.csv", index=False)
