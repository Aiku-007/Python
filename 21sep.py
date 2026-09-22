import subprocess

servers = ["google.com", "github.com", "example.com"]

for server in servers:
    result = subprocess.run(
        ["ping", "-n", "1", server],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"✅ {server} is UP")
    else:
        print(f"❌ {server} is DOWN")