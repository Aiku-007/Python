services = (
    ("nginx", "running"),
    ("docker", "running"),
    ("ssh", "stopped")
)
for service, status in services:
    print(service, status)

    for service, status in services:
        if status != "running":
            print(f"WARNING: {service} is down")