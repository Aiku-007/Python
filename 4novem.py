# ============================================
# DevOps Server Monitoring - Loop Practice
# ============================================

servers = ["web-01", "web-02", "db-01", "cache-01"]

cpu_usage = [45, 87, 95, 30]

healthy = 0
warning = 0
critical = 0


# --------------------------------------------
# 1. FOR LOOP + RANGE()
# --------------------------------------------

print("=" * 40)
print("SERVER MONITORING")
print("=" * 40)

for i in range(len(servers)):

    server = servers[i]
    cpu = cpu_usage[i]

    print(f"\nChecking server: {server}")
    print(f"CPU Usage: {cpu}%")

    if cpu < 70:
        status = "Healthy"
        healthy += 1

    elif cpu < 90:
        status = "Warning"
        warning += 1

    else:
        status = "Critical"
        critical += 1

    print(f"Status: {status}")


# --------------------------------------------
# 2. LOOP WITH CONTINUE
# --------------------------------------------

print("\n" + "=" * 40)
print("HEALTHY SERVERS")
print("=" * 40)

for i in range(len(servers)):

    if cpu_usage[i] >= 70:
        continue

    print(f"{servers[i]} - {cpu_usage[i]}%")


# --------------------------------------------
# 3. LOOP WITH BREAK
# --------------------------------------------

print("\n" + "=" * 40)
print("SEARCHING FOR DATABASE SERVER")
print("=" * 40)

for i in range(len(servers)):

    print(f"Checking: {servers[i]}")

    if servers[i] == "db-01":
        print("Database server found!")
        break


# --------------------------------------------
# 4. WHILE LOOP
# --------------------------------------------

print("\n" + "=" * 40)
print("MONITORING COUNTDOWN")
print("=" * 40)

countdown = 5

while countdown > 0:

    print(countdown)

    countdown -= 1

print("Monitoring started!")


# --------------------------------------------
# 5. NESTED LOOPS
# --------------------------------------------

print("\n" + "=" * 40)
print("SERVER HEALTH CHECKS")
print("=" * 40)

for server in servers:

    print(f"\nServer: {server}")

    for check in range(1, 4):

        print(f"Check {check}")


# --------------------------------------------
# 6. SECOND WHILE LOOP
# --------------------------------------------

print("\n" + "=" * 40)
print("SERVER INDEXES")
print("=" * 40)

index = 0

while index < len(servers):

    print(f"Index {index}: {servers[index]}")

    index += 1


# --------------------------------------------
# 7. FINAL SUMMARY
# --------------------------------------------

print("\n" + "=" * 40)
print("MONITORING SUMMARY")
print("=" * 40)

print(f"Healthy servers: {healthy}")
print(f"Warning servers: {warning}")
print(f"Critical servers: {critical}")

print("=" * 40)