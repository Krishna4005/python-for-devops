namespaces = ["dev", "test", "stage", "prod"]

for ns in namespaces:
    print(f"Creating namespace: {ns}")
    # os.system(f"kubectl create namespace {ns}")
