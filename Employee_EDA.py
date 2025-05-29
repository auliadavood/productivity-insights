import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📦 Set plot styles
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

df = pd.read_csv("Cleaned_Employee_Productivity.csv")

print("📌 Data Info:")
print(df.info())
print("\n📌 Summary Statistics:")
print(df.describe(include='all'))
print("\n📌 Categorical Column Unique Counts:")
print(df.select_dtypes(include=['object', 'category']).nunique())

sns.countplot(x='Performance_Score', data=df, palette='viridis')
plt.title("Performance Score Distribution")
plt.xlabel("Performance Score")
plt.ylabel("Number of Employees")
plt.show()

sns.histplot(df['Monthly_Salary'], kde=True, color='skyblue')
plt.title("Monthly Salary Distribution")
plt.xlabel("Monthly Salary")
plt.ylabel("Frequency")
plt.show()

sns.countplot(x='Gender', data=df, palette='Set2')
plt.title("Gender Distribution")
plt.show()

sns.boxplot(x='Department', y='Monthly_Salary', data=df)
plt.xticks(rotation=45)
plt.title("Monthly Salary by Department")
plt.show()

sns.boxplot(x='Education_Level', y='Performance_Score', data=df, palette='cool')
plt.title("Education Level vs Performance Score")
plt.show()

resign_rate = df.groupby('Tenure_Category')['Resigned'].mean().reset_index()
sns.barplot(x='Tenure_Category', y='Resigned', data=resign_rate, palette='magma')
plt.title("Resignation Rate by Tenure Category")
plt.ylabel("Proportion Resigned")
plt.show()

numeric_cols = df.select_dtypes(include=['number'])
correlation = numeric_cols.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

sns.scatterplot(x='Employee_Satisfaction_Score', y='Performance_Score', hue='Resigned', data=df)
plt.title("Satisfaction vs Performance Score (colored by Resigned)")
plt.show()

sns.countplot(y='Department', data=df, order=df['Department'].value_counts().index)
plt.title("Employees per Department")
plt.show()

sns.countplot(y='Job_Title', data=df, order=df['Job_Title'].value_counts().head(10).index)
plt.title("Top 10 Job Titles")
plt.show()

correlation.to_csv("correlation_matrix.csv")
print("✅ Correlation matrix saved as 'correlation_matrix.csv'")
