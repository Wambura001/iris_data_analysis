import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('Iris.csv') 
df.drop('Id', axis = 1, inplace = True)
# df.drop_duplicates(inplace = True)

# print("First 5 row:\n", df.head()) 
# print("\nData Summary:\n", df.info())
# print("\nDescriptive Statistics:\n", df.describe())
# print("\nMissing Values:\n", df.isnull().sum())
# print("\nDuplicate Rows:\n", df.duplicated().sum())

# histogram
# df.hist(figsize=(10, 8))
# plt.suptitle("Histograms of Iris Features", fontsize=16)
# plt.tight_layout(rect=[0, 0.03, 1, 0.95])
# plt.show()

# Scatter plots
# sns.pairplot(df, hue='Species', diag_kind='kde')
# plt.suptitle("Pairplot of Iris Features", fontsize = 16)
# plt.tight_layout(rect=[0, 0.03, 1, 0.95])
# plt.show()

# Box plots 
# plt.figure(figsize=(10, 6))
# sns.boxplot(x='Species', y='SepalLengthCm', data=df)
# plt.title('Sepal Length by Species')
# plt.show()

# plt.figure(figsize=(10, 6))
# sns.boxplot(x='Species', y='SepalWidthCm', data=df)
# plt.title('Sepal Width by Species')
# plt.show()

# plt.figure(figsize=(10, 6))
# sns.boxplot(x='Species', y='PetalLengthCm', data=df)
# plt.title('Petal Length by Species')
# plt.show()

# plt.figure(figsize=(10, 6))
# sns.boxplot(x='Species', y='PetalWidthCm', data=df)
# plt.title('Petal Width by Species')
# plt.show()

print(df.groupby('Species').describe())