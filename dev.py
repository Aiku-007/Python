
import shutil
import datetime

# Server disk to monitor
path = "/"

# Get disk usage information
total, used, free = shutil.disk_usage(path)

# Convert bytes to gigabytes
total_gb = total / (1024 ** 3)
used_gb = used / (1024 ** 3)
free_gb = free / (1024 ** 3)

# Calculate disk usage percentage
usage_percent = (used / total) * 100

# Display the report
print("===== SERVER HEALTH REPORT =====")
print("Time:", datetime.datetime.now())
print(f"Total disk space: {total_gb:.2f} GB")
print(f"Used disk space: {used_gb:.2f} GB")
print(f"Free disk space: {free_gb:.2f} GB")
print(f"Disk usage: {usage_percent:.2f}%")

# Alert if disk usage is too high
if usage_percent >= 80:
    print("WARNING: Disk usage is critically high!")
else:
    print("STATUS: Disk space is healthy.")
