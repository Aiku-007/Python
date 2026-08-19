# ============================================================
# PYTHON MASTER PRACTICE
# DevOps Server Management Program
# ============================================================


# ------------------------------------------------------------
# 1. VARIABLES + DATA TYPES
# ------------------------------------------------------------

name = "Aiko"
age = 21
is_devops_student = True
experience = 0.5

print("Name:", name)
print("Age:", age)
print("DevOps Student:", is_devops_student)
print("Experience:", experience)


# ------------------------------------------------------------
# 2. INPUT + TYPE CONVERSION
# ------------------------------------------------------------

user_name = input("\nEnter your name: ")
user_age = int(input("Enter your age: "))

print(f"Hello {user_name}, you are {user_age} years old.")


# ------------------------------------------------------------
# 3. STRINGS
# ------------------------------------------------------------

server_name = "production-server"

print("\nServer:", server_name)

# Indexing
print("First character:", server_name[0])
print("Last character:", server_name[-1])

# Slicing
print("First 6 characters:", server_name[:6])
print("Characters 2 to 8:", server_name[2:9])
print("Last 6 characters:", server_name[-6:])

# Reverse
print("Reversed:", server_name[::-1])

# String methods
print(server_name.upper())
print(server_name.lower())
print(server_name.title())

# String immutability
new_server_name = server_name.upper()

print("Original:", server_name)
print("New:", new_server_name)


# ------------------------------------------------------------
# 4. OPERATORS
# ------------------------------------------------------------

cpu_usage = 75
memory_usage = 60

print("\nCPU:", cpu_usage)
print("Memory:", memory_usage)

print("CPU + Memory:", cpu_usage + memory_usage)
print("CPU - Memory:", cpu_usage - memory_usage)
print("CPU * 2:", cpu_usage * 2)
print("CPU / 2:", cpu_usage / 2)
print("CPU // 2:", cpu_usage // 2)
print("CPU % 10:", cpu_usage % 10)
print("CPU ** 2:", cpu_usage ** 2)


# ------------------------------------------------------------
# 5. COMPARISON + LOGICAL OPERATORS
# ------------------------------------------------------------

print("\nCPU > 80:", cpu_usage > 80)
print("CPU == 75:", cpu_usage == 75)
print("CPU != 50:", cpu_usage != 50)

print(
    "Server overloaded:",
    cpu_usage > 80 and memory_usage > 80
)

print(
    "Server needs attention:",
    cpu_usage > 80 or memory_usage > 80
)

print(
    "Server is NOT overloaded:",
    not (cpu_usage > 80)
)


# ------------------------------------------------------------
# 6. IF / ELIF / ELSE
# ------------------------------------------------------------

if cpu_usage >= 90:
    status = "Critical"
elif cpu_usage >= 70:
    status = "Warning"
else:
    status = "Healthy"

print("\nServer status:", status)


# ------------------------------------------------------------
# 7. LISTS
# ------------------------------------------------------------

servers = [
    "web-01",
    "web-02",
    "web-03",
    "db-01",
    "db-02",
    "cache-01"
]

print("\nServers:")
print(servers)

# Indexing
print("First server:", servers[0])
print("Last server:", servers[-1])

# Slicing
print("First three servers:", servers[:3])
print("Last two servers:", servers[-2:])

# List methods
servers.append("backup-01")
servers.insert(1, "web-04")

print("After adding servers:", servers)

servers.remove("web-04")

print("After removing web-04:", servers)

print("Number of servers:", len(servers))


# ------------------------------------------------------------
# 8. FOR LOOP
# ------------------------------------------------------------

print("\nAll servers:")

for server in servers:
    print(server)


# ------------------------------------------------------------
# 9. RANGE()
# ------------------------------------------------------------

print("\nServer numbers:")

for number in range(len(servers)):
    print(number, servers[number])


# ------------------------------------------------------------
# 10. CONDITIONALS INSIDE A LOOP
# ------------------------------------------------------------

print("\nServer types:")

for server in servers:

    if server.startswith("web"):
        print(f"{server} is a web server")

    elif server.startswith("db"):
        print(f"{server} is a database server")

    elif server.startswith("cache"):
        print(f"{server} is a cache server")

    else:
        print(f"{server} is another type of server")


# ------------------------------------------------------------
# 11. LINEAR SEARCH
# ------------------------------------------------------------

search_server = input("\nEnter a server to search for: ")

found = False

for server in servers:

    if server == search_server:
        found = True
        print(f"{search_server} was found!")
        break

if not found:
    print(f"{search_server} was not found.")


# ------------------------------------------------------------
# 12. STRING NORMALIZATION
# ------------------------------------------------------------

search_server = input("\nSearch for a server again: ")

search_server = search_server.lower().strip()

found = False

for server in servers:

    if server.lower() == search_server:
        found = True
        print(f"Found: {server}")
        break

if not found:
    print("Server not found.")


# ------------------------------------------------------------
# 13. TWO-POINTER PRACTICE
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50, 60, 70]

left = 0
right = len(numbers) - 1

print("\nTwo-pointer traversal:")

while left <= right:

    print(numbers[left])

    if left != right:
        print(numbers[right])

    left += 1
    right -= 1


# ------------------------------------------------------------
# 14. DICTIONARY
# ------------------------------------------------------------

server_status = {
    "web-01": "healthy",
    "web-02": "warning",
    "web-03": "healthy",
    "db-01": "healthy",
    "db-02": "down",
    "cache-01": "warning",
    "backup-01": "healthy"
}

print("\nServer status dictionary:")

for server, status in server_status.items():
    print(f"{server}: {status}")


# ------------------------------------------------------------
# 15. DICTIONARY LOOKUP
# ------------------------------------------------------------

lookup = input("\nEnter a server to check its status: ").lower().strip()

if lookup in server_status:
    print(f"{lookup}: {server_status[lookup]}")
else:
    print("Server does not exist.")


# ------------------------------------------------------------
# 16. COUNTING WITH A LOOP
# ------------------------------------------------------------

healthy = 0
warning = 0
down = 0

for status in server_status.values():

    if status == "healthy":
        healthy += 1

    elif status == "warning":
        warning += 1

    elif status == "down":
        down += 1


print("\nServer Summary")
print("Healthy:", healthy)
print("Warning:", warning)
print("Down:", down)


# ------------------------------------------------------------
# 17. TUPLE
# ------------------------------------------------------------

server_location = ("Canada", "Ontario", "Toronto")

print("\nServer location:")
print(server_location)

print("Country:", server_location[0])
print("Province:", server_location[1])
print("City:", server_location[2])


# ------------------------------------------------------------
# 18. SET
# ------------------------------------------------------------

server_tags = {
    "production",
    "linux",
    "aws",
    "docker",
    "linux"
}

print("\nServer tags:")
print(server_tags)


# ------------------------------------------------------------
# 19. FUNCTIONS
# ------------------------------------------------------------

def check_server(server_name):
    server_name = server_name.lower().strip()

    if server_name in server_status:
        return server_status[server_name]

    return None


result = check_server("WEB-01")

if result:
    print("\nFunction result:", result)
else:
    print("\nServer not found.")


# ------------------------------------------------------------
# 20. FUNCTION WITH PARAMETERS
# ------------------------------------------------------------

def calculate_average(numbers):

    total = sum(numbers)
    count = len(numbers)

    return total / count


cpu_values = [50, 60, 70, 80, 90]

average_cpu = calculate_average(cpu_values)

print("\nAverage CPU:", average_cpu)


# ------------------------------------------------------------
# 21. WHILE LOOP
# ------------------------------------------------------------

counter = 1

print("\nCountdown:")

while counter <= 5:

    print(counter)

    counter += 1


# ------------------------------------------------------------
# 22. TRY / EXCEPT
# ------------------------------------------------------------

print("\nNumber conversion:")

try:

    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:

    print("Please enter a valid number.")


# ------------------------------------------------------------
# 23. MULTIPLE EXCEPTIONS
# ------------------------------------------------------------

try:

    number = int(input("\nEnter a number: "))

    result = 100 / number

    print("Result:", result)

except ValueError:

    print("You must enter a number.")

except ZeroDivisionError:

    print("You cannot divide by zero.")


# ------------------------------------------------------------
# 24. ELSE WITH TRY / EXCEPT
# ------------------------------------------------------------

try:

    number = int(input("\nEnter another number: "))

except ValueError:

    print("Invalid number.")

else:

    print("Successfully converted:", number)


# ------------------------------------------------------------
# 25. FILE HANDLING
# ------------------------------------------------------------

log_message = f"""
User: {user_name}
CPU Usage: {cpu_usage}
Memory Usage: {memory_usage}
Server Status: {status}
"""

with open("server_log.txt", "w") as file:
    file.write(log_message)

print("\nLog file created.")


# ------------------------------------------------------------
# 26. READ FILE
# ------------------------------------------------------------

try:

    with open("server_log.txt", "r") as file:

        content = file.read()

        print("\nLog file contents:")
        print(content)

except FileNotFoundError:

    print("Log file does not exist.")


# ------------------------------------------------------------
# 27. APPEND TO FILE
# ------------------------------------------------------------

with open("server_log.txt", "a") as file:

    file.write("Log updated successfully.\n")


# ------------------------------------------------------------
# 28. FINAL REPORT
# ------------------------------------------------------------

print("\n" + "=" * 40)
print("FINAL SERVER REPORT")
print("=" * 40)

print(f"Engineer: {user_name}")
print(f"Total servers: {len(server_status)}")
print(f"Healthy: {healthy}")
print(f"Warning: {warning}")
print(f"Down: {down}")
print(f"Average CPU: {average_cpu}")

print("=" * 40)
print("Program finished.")
print("=" * 40)