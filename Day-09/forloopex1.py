services = ["nginx", "redis", "postgres"]

for service in services:
    print(f"Restarting {service}...")
    # os.system(f"systemctl restart {service}")
