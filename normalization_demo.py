import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

data = {
    'Age': [20, 32, 47, 58, 69],
    'Salary': [40000, 52000, 78000, 91000, 120000],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR']
}
df = pd.DataFrame(data)
print("Original Data:\n",df)

scaler = MinMaxScaler()
df['Salary_Normalized'] = scaler.fit_transform(df[['Salary']])

scaler_std = StandardScaler()
df['Age_Standardized'] = scaler_std.fit_transform(df[['Age']])

encoder = LabelEncoder()
df['Department_Encoded'] = encoder.fit_transform(df['Department'])

bins = [0,20, 35, 57, 70]
labels = ['kids','Young', 'Middle-aged', 'Senior']
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

df['Log_Salary'] = np.log(df['Salary'])
print(df)

