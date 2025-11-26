X = features.select_dtypes(include=['float64','int64']).fillna(0)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
features["cluster"] = clusters

cluster_to_label = {
    0: "bot",
    1: "script_kiddie",
    2: "skilled"
}
features["label"] = features["cluster"].map(cluster_to_label)

print(features["label"].value_counts())

cluster_summary = features.groupby("cluster").mean()
print(cluster_summary.T)


