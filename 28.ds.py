from sklearn.cluster import KMeans
import numpy as np

# Sample customer dataset with shopping-related features (replace with your actual data)
customer_data = np.array([
    [2, 3],   # Customer 1
    [1, 2],   # Customer 2
    [6, 8],   # Customer 3
    [5, 7],   # Customer 4
    # ... add more customer data
])

# Input shopping-related features for the new customer
new_customer_features = [float(input(f"Enter feature {i+1} for the new customer: ")) for i in range(customer_data.shape[1])]

# Input the number of clusters (segments)
num_clusters = int(input("Enter the number of clusters (segments): "))

# Set n_init explicitly to suppress the warning
predicted_segment = KMeans(n_clusters=num_clusters, n_init=10).fit(customer_data).predict([new_customer_features])

print(f"The new customer belongs to segment {predicted_segment[0]}")
