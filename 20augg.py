# ============================================================
#              🚀 DEVOPS DEPLOYMENT CENTER
# ============================================================

print("=" * 65)
print("              🚀 DEVOPS DEPLOYMENT CENTER")
print("=" * 65)


# ------------------------------------------------------------
# SERVER DATABASE
# ------------------------------------------------------------

servers = [
    ["server-01", 25, 30, 20, "ONLINE"],
    ["server-02", 70, 55, 60, "ONLINE"],
    ["server-03", 45, 40, 35, "ONLINE"],
    ["server-04", 90, 85, 88, "ONLINE"],
    ["server-05", 15, 25, 30, "ONLINE"]
]


# ------------------------------------------------------------
# APPLICATION DATABASE
# ------------------------------------------------------------

applications = [
    ["website", "2.4.1", "LOW"],
    ["payment-api", "5.8.2", "HIGH"],
    ["user-service", "3.1.0", "MEDIUM"],
    ["inventory-api", "1.9.4", "MEDIUM"]
]


# ------------------------------------------------------------
# DEPLOYMENT HISTORY
# ------------------------------------------------------------

deployment_history = []


# ------------------------------------------------------------
# CHECK SERVER HEALTH
# ------------------------------------------------------------

def server_health(server):

    cpu = server[1]
    memory = server[2]
    disk = server[3]

    if cpu >= 90 or memory >= 90 or disk >= 90:
        return "CRITICAL"

    elif cpu >= 75 or memory >= 75 or disk >= 75:
        return "WARNING"

    else:
        return "HEALTHY"


# ------------------------------------------------------------
# CALCULATE SERVER LOAD
# ------------------------------------------------------------

def calculate_load(server):

    cpu = server[1]
    memory = server[2]
    disk = server[3]

    return (cpu + memory + disk) / 3


# ------------------------------------------------------------
# DISPLAY SERVERS
# ------------------------------------------------------------

def show_servers():

    print("\n" + "=" * 65)
    print("SERVER STATUS")
    print("=" * 65)

    for server in servers:

        name = server[0]
        cpu = server[1]
        memory = server[2]
        disk = server[3]
        status = server_health(server)
        load = calculate_load(server)

        print(f"\n{name}")
        print(f"CPU     : {cpu}%")
        print(f"Memory  : {memory}%")
        print(f"Disk    : {disk}%")
        print(f"Load    : {load:.1f}%")
        print(f"Status  : {status}")


# ------------------------------------------------------------
# SHOW APPLICATIONS
# ------------------------------------------------------------

def show_applications():

    print("\n" + "=" * 65)
    print("APPLICATIONS")
    print("=" * 65)

    for app in applications:

        name = app[0]
        version = app[1]
        risk = app[2]

        print(f"\nApplication : {name}")
        print(f"Version     : {version}")
        print(f"Risk        : {risk}")


# ------------------------------------------------------------
# FIND APPLICATION
# ------------------------------------------------------------

def find_application(name):

    for app in applications:

        if app[0].lower() == name.lower():
            return app

    return None


# ------------------------------------------------------------
# FIND BEST SERVER
# ------------------------------------------------------------

def find_best_server():

    best_server = None
    lowest_load = 101

    for server in servers:

        status = server_health(server)

        if status == "CRITICAL":
            continue

        load = calculate_load(server)

        if load < lowest_load:

            lowest_load = load
            best_server = server

    return best_server


# ------------------------------------------------------------
# CALCULATE DEPLOYMENT RISK
# ------------------------------------------------------------

def deployment_risk(app, server):

    app_risk = app[2]
    load = calculate_load(server)

    risk_score = 0

    # Application risk
    if app_risk == "LOW":
        risk_score += 10

    elif app_risk == "MEDIUM":
        risk_score += 30

    elif app_risk == "HIGH":
        risk_score += 50


    # Server load
    if load < 40:
        risk_score += 10

    elif load < 70:
        risk_score += 25

    else:
        risk_score += 45


    if risk_score >= 80:
        return "HIGH"

    elif risk_score >= 50:
        return "MEDIUM"

    else:
        return "LOW"


# ------------------------------------------------------------
# DEPLOY APPLICATION
# ------------------------------------------------------------

def deploy():

    app_name = input("\nEnter application name: ")

    app = find_application(app_name)

    if app is None:

        print("\n❌ Application not found.")
        return


    best_server = find_best_server()

    if best_server is None:

        print("\n❌ No suitable server available.")
        return


    print("\n🔍 Analyzing deployment...")

    risk = deployment_risk(app, best_server)

    print(f"\nApplication : {app[0]}")
    print(f"Version     : {app[1]}")
    print(f"Risk Level  : {risk}")
    print(f"Target      : {best_server[0]}")


    # --------------------------------------------------------
    # HIGH RISK DEPLOYMENT
    # --------------------------------------------------------

    if risk == "HIGH":

        print("\n⚠️ HIGH RISK DEPLOYMENT")

        confirmation = input(
            "Continue deployment? (yes/no): "
        ).lower()

        if confirmation != "yes":

            print("\n❌ Deployment cancelled.")
            return


    print("\n🚀 Deploying...")

    # Simulate deployment
    success = True

    if best_server[1] > 85:

        success = False


    if success:

        print("\n✅ DEPLOYMENT SUCCESSFUL")

        deployment_history.append(
            [app[0], app[1], best_server[0], "SUCCESS"]
        )

    else:

        print("\n💥 DEPLOYMENT FAILED")

        print("🔄 Starting rollback...")

        deployment_history.append(
            [app[0], app[1], best_server[0], "ROLLED BACK"]
        )

        print("✅ Rollback completed.")


# ------------------------------------------------------------
# DEPLOYMENT HISTORY
# ------------------------------------------------------------

def show_history():

    print("\n" + "=" * 65)
    print("DEPLOYMENT HISTORY")
    print("=" * 65)

    if len(deployment_history) == 0:

        print("\nNo deployments yet.")

        return


    for deployment in deployment_history:

        app = deployment[0]
        version = deployment[1]
        server = deployment[2]
        result = deployment[3]

        print(
            f"\n{app} "
            f"| v{version} "
            f"| {server} "
            f"| {result}"
        )


# ------------------------------------------------------------
# GENERATE REPORT
# ------------------------------------------------------------

def generate_report():

    file = open("deployment_report.txt", "w")

    file.write("=" * 60 + "\n")
    file.write("DEVOPS DEPLOYMENT REPORT\n")
    file.write("=" * 60 + "\n\n")


    file.write("SERVER STATUS\n")
    file.write("-" * 60 + "\n")

    for server in servers:

        name = server[0]
        load = calculate_load(server)
        status = server_health(server)

        file.write(
            f"{name} | "
            f"Load: {load:.1f}% | "
            f"Status: {status}\n"
        )


    file.write("\nDEPLOYMENT HISTORY\n")
    file.write("-" * 60 + "\n")

    for deployment in deployment_history:

        file.write(
            f"{deployment[0]} | "
            f"v{deployment[1]} | "
            f"{deployment[2]} | "
            f"{deployment[3]}\n"
        )


    file.close()

    print("\n📄 Report generated:")
    print("deployment_report.txt")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

while True:

    print("\n")
    print("=" * 65)
    print("                    MAIN MENU")
    print("=" * 65)

    print("1. View servers")
    print("2. View applications")
    print("3. Deploy application")
    print("4. View deployment history")
    print("5. Generate report")
    print("6. Exit")

    choice = input("\nChoose an option: ")


    if choice == "1":

        show_servers()


    elif choice == "2":

        show_applications()


    elif choice == "3":

        deploy()


    elif choice == "4":

        show_history()


    elif choice == "5":

        generate_report()


    elif choice == "6":

        print("\n🚀 DevOps Center shutting down...")
        break


    else:

        print("\n❌ Invalid option.")