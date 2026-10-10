
import psutil
from datetime import datetime

# Set resource usage thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80


def check_server_health():
    print("=" * 40)
    print("       SERVER HEALTH MONITOR")
    print("=" * 40)

    print(f"Time: {datetime.now()}")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")

    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")

    disk = psutil.disk_usage("/")
    print(f"Disk Usage: {disk.percent}%")

    # Check CPU
    if psutil.cpu_percent() > CPU_THRESHOLD:
        print("WARNING: High CPU usage!")

    # Check memory
    if memory.percent > MEMORY_THRESHOLD:
        print("WARNING: High memory usage!")

    # Check disk
    if disk.percent > DISK_THRESHOLD:
        print("WARNING: Disk space is running low!")

    print("=" * 40)


if __name__ == "__main__":
    check_server_health()
