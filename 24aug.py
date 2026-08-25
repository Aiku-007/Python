def check_cpu(cpu_usage):
    if cpu_usage > 80:
        return "High CPU usage"
    else:
        return "CPU usage is normal"


def check_memory(memory_usage):
    if memory_usage > 80:
        return "High memory usage"
    else:
        return "Memory usage is normal"


def check_disk(disk_usage):
    if disk_usage > 90:
        return "Disk space is critically low"
    else:
        return "Disk space is okay"


def server_status(server_name, cpu, memory, disk):
    print(f"\nServer: {server_name}")
    print(check_cpu(cpu))
    print(check_memory(memory))
    print(check_disk(disk))


server_status("web-server-01", 75, 65, 80)
server_status("web-server-02", 92, 70, 95)