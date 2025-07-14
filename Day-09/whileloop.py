import time

connected = False
retries = 0

while not connected and retries < 3:
    print("Trying to connect to server...")
    # Simulate: connected = try_ssh_connection()
    connected = retries == 2  # simulate success on third try
    time.sleep(1)
    retries += 1

if connected:
    print("✅ Connected to server")
else:
    print("❌ Failed to connect after 3 attempts")
