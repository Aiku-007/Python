
import json
import os
import random
from datetime import datetime

# ==========================================
# DEVOPS SERVER MONITORING SYSTEM
# ==========================================

DATA_FILE = "servers.json"
LOG_FILE = "server_logs.txt"


# ==========================================
# 1. INITIAL SERVER INVENTORY
# ==========================================

servers = [
    {
        "id": 1,
        "name": "web-server-01",
        "ip": "192.168.1.10",
        "os": "Ubuntu",
        "environment": "Production",
        "cpu": 35,
        "ram": 60,
        "disk": 45,
        "status": "Running"
    },
    {
        "id": 2,
        "name": "database-server-01",
        "ip": "192.168.1.20",
        "os": "Ubuntu",
        "environment": "Production",
        "cpu": 85,
        "ram": 90,
        "disk": 75,
        "status": "Running"
    },
    {
        "id": 3,
        "name": "testing-server-01",
        "ip": "192.168.1.30",
        "os": "CentOS",
        "environment": "Testing",
        "cpu": 20,
        "ram": 35,
        "disk": 30,
        "status": "Running"
    },
    {
        "id": 4,
        "name": "backup-server-01",
        "ip": "192.168.1.40",
        "os": "Ubuntu",
        "environment": "Development",
        "cpu": 15,
        "ram": 25,
        "disk": 95,
        "status": "Running"
    }
]


# ==========================================
# 2. SAVE SERVER DATA USING JSON
# ==========================================

def save_servers():

    try:
        with open(DATA_FILE, "w") as file:
            json.dump(servers, file, indent=4)

        print("Server data saved successfully!")

    except OSError as error:
        print(f"Error saving data: {error}")


# ==========================================
# 3. LOAD SERVER DATA
# ==========================================

def load_servers():

    global servers

    if os.path.exists(DATA_FILE):

        try:
            with open(DATA_FILE, "r") as file:
                servers = json.load(file)

            print("Server inventory loaded!")

        except (OSError, json.JSONDecodeError) as error:
            print(f"Could not load server data: {error}")


# ==========================================
# 4. LOGGING SYSTEM
# ==========================================

def write_log(message):

    current_time = datetime.now()

    timestamp = current_time.strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(LOG_FILE, "a") as file:

        file.write(
            f"[{timestamp}] {message}\n"
        )


# ==========================================
# 5. DISPLAY ALL SERVERS
# ==========================================

def display_servers():

    print("\n========== SERVER INVENTORY ==========")

    if len(servers) == 0:

        print("No servers available.")

        return

    for server in servers:

        print(f"\nServer ID: {server['id']}")
        print(f"Name: {server['name']}")
        print(f"IP: {server['ip']}")
        print(f"Operating System: {server['os']}")
        print(f"Environment: {server['environment']}")
        print(f"Status: {server['status']}")

    print("\n======================================")


# ==========================================
# 6. ADD A NEW SERVER
# ==========================================

def add_server():

    print("\n========== ADD NEW SERVER ==========")

    name = input("Enter server name: ").strip()

    ip = input("Enter server IP: ").strip()

    os_name = input("Enter operating system: ").strip()

    environment = input(
        "Enter environment (Production/Testing/Development): "
    ).strip()

    if not name or not ip or not os_name or not environment:

        print("All fields are required!")

        return

    for server in servers:

        if server["name"].lower() == name.lower():

            print("Server already exists!")

            return

    new_server = {

        "id": max(
            [server["id"] for server in servers],
            default=0
        ) + 1,

        "name": name,

        "ip": ip,

        "os": os_name,

        "environment": environment,

        "cpu": 0,

        "ram": 0,

        "disk": 0,

        "status": "Running"
    }

    servers.append(new_server)

    save_servers()

    write_log(f"New server added: {name}")

    print(f"Server {name} added successfully!")


# ==========================================
# 7. LINEAR SEARCH
# ==========================================

def search_server():

    search_name = input(
        "\nEnter server name to search: "
    ).strip().lower()

    found = False

    for server in servers:

        if server["name"].lower() == search_name:

            print("\nServer Found!")

            print(f"Name: {server['name']}")
            print(f"IP: {server['ip']}")
            print(f"CPU: {server['cpu']}%")
            print(f"RAM: {server['ram']}%")
            print(f"Disk: {server['disk']}%")

            found = True

            break

    if not found:

        print("Server not found!")


# ==========================================
# 8. DELETE A SERVER
# ==========================================

def delete_server():

    try:

        server_id = int(
            input("\nEnter server ID to delete: ")
        )

        for server in servers:

            if server["id"] == server_id:

                servers.remove(server)

                save_servers()

                write_log(
                    f"Server deleted: {server['name']}"
                )

                print("Server deleted successfully!")

                return

        print("Server ID not found!")

    except ValueError:

        print("Please enter a valid numeric ID!")


# ==========================================
# 9. SIMULATE SERVER MONITORING
# ==========================================

def monitor_servers():

    print("\n========== SERVER MONITORING ==========")

    if not servers:

        print("No servers available to monitor.")

        return

    for server in servers:

        # Simulated resource usage
        server["cpu"] = random.randint(5, 100)

        server["ram"] = random.randint(10, 100)

        server["disk"] = random.randint(10, 100)

        print(f"\nMonitoring: {server['name']}")

        print(f"CPU Usage: {server['cpu']}%")

        print(f"RAM Usage: {server['ram']}%")

        print(f"Disk Usage: {server['disk']}%")

        if (
            server["cpu"] > 80
            or server["ram"] > 85
            or server["disk"] > 90
        ):

            print("WARNING: High resource usage!")

            write_log(
                f"WARNING: High resource usage on "
                f"{server['name']}"
            )

        else:

            print("Server health: NORMAL")

    save_servers()

    print("\nMonitoring completed!")

    print("========================================")


# ==========================================
# 10. GENERATE SERVER HEALTH REPORT
# ==========================================

def generate_report():

    print("\n========== SERVER HEALTH REPORT ==========")

    total_servers = len(servers)

    healthy_servers = 0

    critical_servers = 0

    total_cpu = 0

    total_ram = 0

    total_disk = 0

    for server in servers:

        total_cpu += server["cpu"]

        total_ram += server["ram"]

        total_disk += server["disk"]

        if (
            server["cpu"] > 80
            or server["ram"] > 85
            or server["disk"] > 90
        ):

            critical_servers += 1

        else:

            healthy_servers += 1

    if total_servers == 0:

        print("No server data available.")

        return

    average_cpu = total_cpu / total_servers

    average_ram = total_ram / total_servers

    average_disk = total_disk / total_servers

    print(f"Total Servers: {total_servers}")

    print(f"Healthy Servers: {healthy_servers}")

    print(f"Critical Servers: {critical_servers}")

    print(f"Average CPU Usage: {average_cpu:.2f}%")

    print(f"Average RAM Usage: {average_ram:.2f}%")

    print(f"Average Disk Usage: {average_disk:.2f}%")

    print("===========================================")


# ==========================================
# 11. FILTER PRODUCTION SERVERS
# ==========================================

def production_servers():

    print("\n========== PRODUCTION SERVERS ==========")

    found = False

    for server in servers:

        if server["environment"].lower() == "production":

            print(
                f"{server['name']} - {server['ip']}"
            )

            found = True

    if not found:

        print("No production servers found.")


# ==========================================
# 12. FIND SERVERS WITH HIGH CPU USAGE
# ==========================================

def high_cpu_servers():

    print("\n========== HIGH CPU SERVERS ==========")

    found = False

    for server in servers:

        if server["cpu"] > 80:

            print(
                f"{server['name']} "
                f"has CPU usage of {server['cpu']}%"
            )

            found = True

    if not found:

        print("No servers have critical CPU usage.")


# ==========================================
# 13. READ SERVER LOGS
# ==========================================

def read_logs():

    print("\n========== SERVER LOGS ==========")

    try:

        with open(LOG_FILE, "r") as file:

            logs = file.readlines()

            if not logs:

                print("Log file is empty.")

                return

            for log in logs:

                print(log.strip())

    except FileNotFoundError:

        print("No log file found yet.")


# ==========================================
# 14. SORT SERVERS BY CPU USAGE
# ==========================================

def sort_servers():

    sorted_servers = sorted(
        servers,
        key=lambda server: server["cpu"],
        reverse=True
    )

    print("\n========== SERVERS BY CPU USAGE ==========")

    for server in sorted_servers:

        print(
            f"{server['name']} : {server['cpu']}%"
        )


# ==========================================
# 15. MAIN MENU
# ==========================================

def main():

    load_servers()

    while True:

        print("\n")
        print("=" * 45)

        print("       DEVOPS SERVER MANAGEMENT")

        print("=" * 45)

        print("1. Display All Servers")

        print("2. Add New Server")

        print("3. Search Server")

        print("4. Delete Server")

        print("5. Monitor Servers")

        print("6. Generate Health Report")

        print("7. Show Production Servers")

        print("8. Show High CPU Servers")

        print("9. Read Server Logs")

        print("10. Sort Servers by CPU Usage")

        print("11. Exit")

        print("=" * 45)

        choice = input("Enter your choice (1-11): ").strip()

        if choice == "1":

            display_servers()

        elif choice == "2":

            add_server()

        elif choice == "3":

            search_server()

        elif choice == "4":

            delete_server()

        elif choice == "5":

            monitor_servers()

        elif choice == "6":

            generate_report()

        elif choice == "7":

            production_servers()

        elif choice == "8":

            high_cpu_servers()

        elif choice == "9":

            read_logs()

        elif choice == "10":

            sort_servers()

        elif choice == "11":

            save_servers()

            print("Exiting DevOps Management System!")

            write_log("Monitoring system stopped.")

            break

        else:

            print("Invalid choice! Try again.")


# ==========================================
# 16. PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":

    main()
