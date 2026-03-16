# Program to Handle Missing Variables in a Dataset

import pandas as pd
import numpy as np

# Step 1: Create dataset with missing values
data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Aman", "Riya", "John", "Sara", "Raj"],
    "Age": [21, np.nan, 20, 22, np.nan],
    "Salary": [30000, 35000, np.nan, 40000, 38000]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Step 2: Check missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Step 3: Replace missing Age with mean value
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Step 4: Replace missing Salary with median value
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

print("\nDataset after Handling Missing Values:")
print(df)

# Step 5: Verify again
print("\nMissing Values After Treatment:")
print(df.isnull().sum())