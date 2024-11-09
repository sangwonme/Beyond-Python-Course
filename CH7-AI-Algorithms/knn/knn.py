import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from collections import Counter

# Step 1: Generate a synthetic dataset
X, y = make_blobs(n_samples=100, centers=3, random_state=42, cluster_std=1.5)

# Step 2: Plot the dataset
def plot_dataset(X, y):
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap="viridis", s=50, edgecolor="k")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("Dataset")
    plt.show()

plot_dataset(X, y)

# Step 3: Define a function to calculate the Euclidean distance
def euclidean_distance(point1, point2):
    # Implement the Euclidean distance formula
    return np.sqrt(np.sum((point1 - point2) ** 2))

# Step 4: Implement the KNN function
def knn(X_train, y_train, new_point, k=3):
    # 1. Calculate distances between new_point and each point in X_train
    distances = []
    for i in range(len(X_train)):
        # Calculate the distance from new_point to X_train[i]
        dist = euclidean_distance(new_point, X_train[i])
        distances.append((dist, y_train[i]))  # Save distance and label

    # 2. Sort distances (ascending) and select the top-k closest neighbors
    # Sort distances and take the first k neighbors
    distances.sort(key=lambda x: x[0])
    k_neighbors = distances[:k]

    # 3. Extract the labels of the k neighbors and find the most common label
    # Get the labels of the neighbors and find the most common one
    label_counts = Counter([label for _, label in k_neighbors])
    predicted_label = label_counts.most_common(1)[0][0]

    return predicted_label

# Step 5: Define a function to visualize the classification steps
def plot_knn_steps(X, y, k, new_point):
    plt.figure(figsize=(10, 6))

    # Plot the dataset
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap="viridis", s=50, edgecolor="k", label="Data points")
    
    # Plot the new point in red
    plt.scatter(new_point[0], new_point[1], c="red", s=100, label="New point", marker="x")

    # Find the k nearest neighbors using our KNN function
    distances = []
    for i in range(len(X)):
        dist = euclidean_distance(new_point, X[i])
        distances.append((dist, y[i]))
    distances.sort(key=lambda x: x[0])
    k_neighbors = distances[:k]

    # Plot lines connecting the new point to its nearest neighbors
    for dist, label in k_neighbors:
        neighbor_index = np.where((X == X[i]).all(axis=1))[0][0]
        plt.plot([new_point[0], X[i][0]], [new_point[1], X[i][1]], 'k--', linewidth=1)

    predicted_label = knn(X, y, new_point, k=k)
    
    plt.title(f"New point classified as class {predicted_label}")
    plt.legend()
    plt.show()

# Step 6: Test the KNN function with a new point
new_point = [0, -6]
plot_knn_steps
