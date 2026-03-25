import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Income": [15, 16, 17, 18, 19, 60, 62, 64, 65, 67],
    "Spending": [39, 81, 6, 77, 40, 76, 6, 94, 3, 72]
}

df = pd.DataFrame(data)

# K-Means model
model = KMeans(n_clusters=3)
df["Cluster"] = model.fit_predict(df)

print(df)

# Plotting clusters
plt.scatter(df["Income"], df["Spending"], c=df["Cluster"])
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("Customer Segments")
plt.show()