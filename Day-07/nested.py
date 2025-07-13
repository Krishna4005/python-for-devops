env = "prod"
region = "us-west-2"

if env == "prod":
    if region.startswith("us-"):
        print("Deploying to production (US region)")
    else:
        print("Production deployments are only allowed in US regions")
elif env == "dev":
    print("Deploying to development environment")
else:
    print("Unsupported environment")
