import pandas as pd

# Creating a simple dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [40, 45, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

print("Student Study Dataset:")
print(df)

# Identifying feature and label
features = df["Study_Hours"]
labels = df["Marks"]

print("\nFeature (Input): Study Hours")
print("Label (Output): Marks")