cpu = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu}%")

if cpu > CPU_THRESHOLD:
    print("WARNING: High CPU usage!")