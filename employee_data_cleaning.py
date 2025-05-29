import pandas as pd

df = pd.read_csv("Extended_Employee_Performance_and_Productivity_Data.csv")
df['Hire_Date'] = pd.to_datetime(df['Hire_Date'], errors='coerce')
df['Gender'] = df['Gender'].str.strip().str.title()
df['Department'] = df['Department'].str.strip().str.title()
df['Education_Level'] = df['Education_Level'].str.strip().str.title()
df['Job_Title'] = df['Job_Title'].str.strip().str.title()
df = df.dropna()
df['Tenure_Category'] = pd.cut(
    df['Years_At_Company'],
    bins=[-1, 2, 5, 10, 20],
    labels=['<2 Years', '2-5 Years', '6-10 Years', '10+ Years']
)
categorical_cols = ['Gender', 'Department', 'Education_Level', 'Tenure_Category', 'Job_Title']
for col in categorical_cols:
    df[col] = df[col].astype('category')
df.to_csv("Cleaned_Employee_Productivity.csv", index=False)
print("Data cleaned and saved as 'Cleaned_Employee_Productivity.csv'")
