servers = [
    "web01",
    "web02",
    "db01",
    "cache01",
    "backup01"
]
for server in servers:

    if server == "db01":
        print(f"Connecting to {server}")
        print("Server Busy!")
    else:
        print(f"Connecting to {server}")
        print("Connection Successful!")
    