service_status = "failed"  # Could be 'running', 'inactive', 'failed'

if service_status == "running":
    print("Service is healthy. No action needed.")
elif service_status in ["inactive", "failed"]:
    print("Attempting to restart service...")
    # os.system("systemctl restart my-service")
else:
    print("Unknown service status.")
