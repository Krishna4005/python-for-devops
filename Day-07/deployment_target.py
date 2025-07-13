env = "stage"  # Could be 'dev', 'prod', 'stage'

if env == "dev":
    target = "AWS EC2"
elif env == "stage":
    target = "Kubernetes Cluster (staging)"
elif env == "prod":
    target = "Kubernetes Cluster (production)"
else:
    target = "Unknown"

print(f"Deploying to: {target}")
