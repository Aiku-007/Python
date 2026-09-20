import shutil

total, used, free = shutil.disk_usage("/")

usage = used / total * 100

print(f"Disk usage: {usage:.1f}%")

if usage > 80:
    print("⚠️ WARNING: Disk space is running low!")
else:
    print("✅ Disk space is OK")