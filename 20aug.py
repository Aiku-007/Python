# ============================================================
#              SERVER HEALTH & INCIDENT MONITOR
# ============================================================

print("=" * 60)
print("        🖥️  SERVER HEALTH & INCIDENT MONITOR")
print("=" * 60)

# ------------------------------------------------------------
# SERVER DATA
# ------------------------------------------------------------

servers = [
    ["web-01", "web", 35, 42, 51],
    ["web-02", "web", 82, 67, 74],
    ["db-01", "database", 91, 88, 92],
    ["db-02", "database", 45, 52, 48],
    ["api-01", "api", 73, 69, 61],
    ["api-02", "api", 28, 35, 40]
]

incidents = []


# ------------------------------------------------------------
# FUNCTION: DETERMINE SERVER STATUS
# ------------------------------------------------------------

def check_health(cpu, memory, disk):

    if cpu >= 90 or memory >= 90 or disk >= 90:
        return "CRITICAL"

    elif cpu >= 75 or memory >= 75 or disk >= 75:
        return "WARNING"

    else:
        return "OK"


# ------------------------------------------------------------
# FUNCTION: DISPLAY SERVER
# ------------------------------------------------------------

def display_server(server):

    name = server[0]
    server_type = server[1]
    cpu = server[2]
    memory = server[3]
    disk = server[4]

    status = check_health(cpu, memory, disk)

    print("\n" + "-" * 50)
    print(f"Server Name : {name}")
    print(f"Type        : {server_type}")
    print(f"CPU Usage   : {cpu}%")
    print(f"Memory      : {memory}%")
    print(f"Disk Usage  : {disk}%")
    print(f"Status      : {status}")
    print("-" * 50)


# ------------------------------------------------------------
# FUNCTION: CHECK ALL SERVERS
# ------------------------------------------------------------

def check_all_servers():

    print("\n🔍 CHECKING ALL SERVERS...\n")

    healthy = 0
    warning = 0
    critical = 0

    for server in servers:

        name = server[0]
        cpu = server[2]
        memory = server[3]
        disk = server[4]

        status = check_health(cpu, memory, disk)

        print(f"{name:10} → {status}")

        if status == "OK":
            healthy += 1

        elif status == "WARNING":
            warning += 1

        elif status == "CRITICAL":
            critical += 1

    print("\n" + "=" * 40)
    print("HEALTH SUMMARY")
    print("=" * 40)

    print(f"Healthy servers  : {healthy}")
    print(f"Warning servers  : {warning}")
    print(f"Critical servers : {critical}")


# ------------------------------------------------------------
# FUNCTION: SEARCH SERVER
# ------------------------------------------------------------

def search_server():

    search = input("\nEnter server name: ").lower()

    found = False

    for server in servers:

        if server[0].lower() == search:

            display_server(server)
            found = True
            break

    if not found:
        print("\n❌ Server not found.")


# ------------------------------------------------------------
# FUNCTION: GENERATE INCIDENTS
# ------------------------------------------------------------

def generate_incidents():

    print("\n🚨 SCANNING FOR INCIDENTS...\n")

    incidents.clear()

    for server in servers:

        name = server[0]
        cpu = server[2]
        memory = server[3]
        disk = server[4]

        status = check_health(cpu, memory, disk)

        if status != "OK":

            if status == "CRITICAL":
                message = f"{name} requires immediate attention."

            else:
                message = f"{name} should be investigated."

            incidents.append([name, status, message])

    if len(incidents) == 0:

        print("✅ No incidents detected.")

    else:

        for incident in incidents:

            print(f"🚨 {incident[0]} | {incident[1]}")
            print(f"   {incident[2]}")


# ------------------------------------------------------------
# FUNCTION: SAVE REPORT
# ------------------------------------------------------------

def save_report():

    file = open("server_report.txt", "w")

    file.write("=" * 50 + "\n")
    file.write("SERVER HEALTH REPORT\n")
    file.write("=" * 50 + "\n\n")

    for server in servers:

        name = server[0]
        server_type = server[1]
        cpu = server[2]
        memory = server[3]
        disk = server[4]

        status = check_health(cpu, memory, disk)

        file.write(f"Server: {name}\n")
        file.write(f"Type: {server_type}\n")
        file.write(f"CPU: {cpu}%\n")
        file.write(f"Memory: {memory}%\n")
        file.write(f"Disk: {disk}%\n")
        file.write(f"Status: {status}\n")
        file.write("-" * 40 + "\n")

    file.write("\nINCIDENTS\n")
    file.write("=" * 50 + "\n")

    for incident in incidents:

        file.write(
            f"{incident[0]} | {incident[1]} | {incident[2]}\n"
        )

    file.close()

    print("\n📄 Report saved as server_report.txt")


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

while True:

    print("\n")
    print("=" * 60)
    print("                 MAIN MENU")
    print("=" * 60)

    print("1. View all servers")
    print("2. Check server health")
    print("3. Search for a server")
    print("4. Generate incidents")
    print("5. Save report")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        for server in servers:
            display_server(server)

    elif choice == "2":

        check_all_servers()

    elif choice == "3":

        search_server()

    elif choice == "4":

        generate_incidents()

    elif choice == "5":

        save_report()

    elif choice == "6":

        print("\n👋 Monitoring system shutting down...")
        break

    else:

        print("\n❌ Invalid option. Try again.")