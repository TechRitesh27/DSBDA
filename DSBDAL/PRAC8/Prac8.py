# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the Titanic dataset
dataset = sns.load_dataset('titanic')
print(dataset.head())

# -------------------------------
# Distplot (Replaced with histplot in latest Seaborn)
# -------------------------------
# Histogram of 'age' with KDE
sns.histplot(data=dataset, x='age', bins=10, kde=True)
plt.title("Histogram of Age with KDE")
plt.show()

# Histogram without KDE
sns.histplot(data=dataset, x='age', bins=10, kde=False)
plt.title("Histogram of Age without KDE")
plt.show()

# -------------------------------
# Jointplots: Scatter and Hex
# -------------------------------
sns.jointplot(data=dataset, x='age', y='fare', kind='scatter')
sns.jointplot(data=dataset, x='age', y='fare', kind='hex')

# -------------------------------
# Rugplot: Small bars for distribution
# -------------------------------
sns.rugplot(x='fare', data=dataset)
plt.title("Rugplot of Fare")
plt.show()

# -------------------------------
# Barplot and Countplot
# -------------------------------
sns.barplot(x='sex', y='age', data=dataset)
plt.title("Barplot of Age by Sex")
plt.show()

sns.barplot(x='sex', y='age', data=dataset, estimator=np.std)
plt.title("Barplot of Age (STD) by Sex")
plt.show()

sns.countplot(x='sex', data=dataset)
plt.title("Count of Passengers by Sex")
plt.show()

# -------------------------------
# Boxplot and Violinplot
# -------------------------------
sns.boxplot(x='sex', y='age', data=dataset)
plt.title("Boxplot of Age by Sex")
plt.show()

sns.boxplot(x='sex', y='age', data=dataset, hue="survived")
plt.title("Boxplot of Age by Sex and Survival")
plt.show()

sns.violinplot(x='sex', y='age', data=dataset)
plt.title("Violinplot of Age by Sex")
plt.show()

sns.violinplot(x='sex', y='age', data=dataset, hue='survived', split=True)
plt.title("Violinplot of Age by Sex and Survival")
plt.show()

# -------------------------------
# Stripplot and Swarmplot
# -------------------------------
sns.stripplot(x='sex', y='age', data=dataset, jitter=False)
plt.title("Stripplot (no jitter)")
plt.show()

sns.stripplot(x='sex', y='age', data=dataset, jitter=True)
plt.title("Stripplot with Jitter")
plt.show()

sns.stripplot(x='sex', y='age', data=dataset, jitter=True, hue='survived', dodge=True)
plt.title("Stripplot with Jitter and Hue")
plt.show()

sns.swarmplot(x='sex', y='age', data=dataset)
plt.title("Swarmplot of Age by Sex")
plt.show()

sns.swarmplot(x='sex', y='age', data=dataset, hue='survived', dodge=True)
plt.title("Swarmplot with Hue (Survived)")
plt.show()

# -------------------------------
# Correlation Matrix & Heatmap
# -------------------------------
corr = dataset.corr(numeric_only=True)

sns.heatmap(corr)
plt.title("Correlation Heatmap")
plt.show()

sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap with Annotations")
plt.show()

# -------------------------------
# Histogram for Fare
# -------------------------------
sns.histplot(dataset['fare'], kde=False, bins=10)
plt.title("Histogram of Fare")
plt.show()
