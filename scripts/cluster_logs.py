import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load repair logs from sample file
with open("repair_logs_sample.txt", "r") as file:
    repair_logs = [log.strip() for log in file.read().split("\n\n") if log.strip()]

# Vectorize the logs using TF-IDF (offline embedding alternative)
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(repair_logs)

# Define number of clusters (e.g., 2 or 3 for simplicity)
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

clusters = {i: [] for i in range(num_clusters)}

# Assign logs to clusters
for idx, label in enumerate(kmeans.labels_):
    clusters[label].append(repair_logs[idx])

# Save clustered logs to files
output_dir = "clustered_logs"
os.makedirs(output_dir, exist_ok=True)

for cluster_id, logs in clusters.items():
    filename = os.path.join(output_dir, f"cluster_{cluster_id + 1}.txt")
    with open(filename, "w") as f:
        for log in logs:
            f.write(log + "\n\n")

    print(f"Saved cluster {cluster_id + 1} with {len(logs)} logs to {filename}")
