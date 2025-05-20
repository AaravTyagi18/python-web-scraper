import ssl
import certifi
import urllib.request

ssl_context = ssl.create_default_context(cafile=certifi.where())
response = urllib.request.urlopen('https://example.com', context=ssl_context)
print(response.read())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('titanic')

print("Shape:", df.shape)
print("Columns:", df.columns)
print("Info:")
print(df.info())
print("\nSummary:")
print(df.describe())

print("\nMissing values:\n", df.isnull().sum())

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='class', hue='survived')
plt.title("Survival Count by Class")
plt.show()
