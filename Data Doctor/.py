import pandas as pd

# Sample dataset
data = {
    "Name": ["Rahul", "Anita", "Rahul", "Vikas", None],
    "City": ["Delhi", "Mumbai", "Delhi", "mumbai", "Chennai"],
    "Score": [85, 90, 85, None, 78]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Handle missing values
df["Name"].fillna("Unknown", inplace=True)
df["Score"].fillna(df["Score"].mean(), inplace=True)

# Remove duplicate rows
df = df.drop_duplicates()

# Standardize text (make city names lowercase)
df["City"] = df["City"].str.lower()

print("\nCleaned Data:")
print(df)