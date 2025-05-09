# Step 1: Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: Load the Iris dataset from Seaborn
dataset = sns.load_dataset('iris')

# Display the first 5 rows of the dataset
print(dataset.head())

# Step 3: Plot Histograms for different attributes
plt.figure(figsize=(16, 9))

# Histograms for 'sepal_length', 'sepal_width', 'petal_length', 'petal_width'
sns.histplot(dataset['sepal_length'])
plt.title("Histogram of Sepal Length")
plt.show()

sns.histplot(dataset['sepal_width'])
plt.title("Histogram of Sepal Width")
plt.show()

sns.histplot(dataset['petal_length'])
plt.title("Histogram of Petal Length")
plt.show()

sns.histplot(dataset['petal_width'])
plt.title("Histogram of Petal Width")
plt.show()

# Step 4: Plot Boxplots for each attribute grouped by species
plt.figure(figsize=(16, 9))

# Boxplot for 'petal_length' grouped by 'species'
sns.boxplot(x='species', y='petal_length', data=dataset)
plt.title("Boxplot of Petal Length by Species")
plt.show()

# Boxplot for 'petal_width' grouped by 'species'
sns.boxplot(x='species', y='petal_width', data=dataset)
plt.title("Boxplot of Petal Width by Species")
plt.show()

# Boxplot for 'sepal_length' grouped by 'species'
sns.boxplot(x='species', y='sepal_length', data=dataset)
plt.title("Boxplot of Sepal Length by Species")
plt.show()

# Boxplot for 'sepal_width' grouped by 'species'
sns.boxplot(x='species', y='sepal_width', data=dataset)
plt.title("Boxplot of Sepal Width by Species")
plt.show()


