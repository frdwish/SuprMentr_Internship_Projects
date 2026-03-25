import numpy as np
from sklearn.neighbors import NearestNeighbors

# Sample user preference dataset
# Rows represent users, columns represent movie ratings
data = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4],
    [0, 1, 5, 4]
])

# Create KNN model
model = NearestNeighbors(n_neighbors=2, metric='euclidean')
model.fit(data)

# New user preferences
new_user = np.array([[5, 2, 0, 1]])

# Find nearest neighbors
distances, indices = model.kneighbors(new_user)

print("Nearest Neighbors Index:", indices)
print("Distances:", distances)