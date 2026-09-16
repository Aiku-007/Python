from datetime import date


# ==========================================
# LIFE QUEUE
# ==========================================

tasks = []


# ------------------------------------------
# ADD A TASK
# ------------------------------------------

def add_task():
    print("\n--- Add Task ---")

    name = input("Task name: ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    importance = input("Importance (high/medium/low): ").lower()

    # Make sure importance is valid
    while importance not in ["high", "medium", "low"]:
        print("Please enter high, medium, or low.")
        importance = input("Importance: ").lower()

    task = {
        "name": name,
        "deadline": deadline,
        "importance": importance,
        "ignored_days": 0,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully!")


# ------------------------------------------
# CALCULATE TASK PRIORITY
# ------------------------------------------

def calculate_priority(task):
    deadline = date.fromisoformat(task["deadline"])
    today = date.today()

    days_left = (deadline - today).days

    score = 0

    # Importance
    if task["importance"] == "high":
        score += 3
    elif task["importance"] == "medium":
        score += 2
    else:
        score += 1

    # Deadline
    if days_left <= 0:
        score += 5
    elif days_left <= 2:
        score += 4
    elif days_left <= 5:
        score += 2

    # Being ignored increases priority
    score += task["ignored_days"]

    return score


# ------------------------------------------
# DECIDE WHICH BUCKET A TASK BELONGS TO
# ------------------------------------------

def get_bucket(task):
    score = calculate_priority(task)

    if score >= 7:
        return "MUST DO"

    elif score >= 4:
        return "SHOULD DO"

    else:
        return "CAN WAIT"


# ------------------------------------------
# DISPLAY ONE TASK
# ------------------------------------------

def display_task(task, number):
    deadline = date.fromisoformat(task["deadline"])
    today = date.today()

    days_left = (deadline - today).days
    priority = calculate_priority(task)
    bucket = get_bucket(task)

    print(f"\n{number}. {task['name']}")
    print(f"   Deadline: {task['deadline']}")

    if days_left < 0:
        print(f"   Status: {abs(days_left)} day(s) overdue")
    elif days_left == 0:
        print("   Status: Due today")
    elif days_left == 1:
        print("   Status: Due tomorrow")
    else:
        print(f"   Status: {days_left} day(s) left")

    print(f"   Importance: {task['importance']}")
    print(f"   Ignored days: {task['ignored_days']}")
    print(f"   Priority score: {priority}")
    print(f"   Bucket: {bucket}")


# ------------------------------------------
# VIEW ALL TASKS
# ------------------------------------------

def view_tasks():
    print("\n========== LIFE QUEUE ==========")

    if len(tasks) == 0:
        print("No tasks yet.")
        return

    buckets = {
        "MUST DO": [],
        "SHOULD DO": [],
        "CAN WAIT": []
    }

    # Put every task into its bucket
    for task in tasks:
        bucket = get_bucket(task)
        buckets[bucket].append(task)

    # Display MUST DO
    print("\n🔥 MUST DO")

    if len(buckets["MUST DO"]) == 0:
        print("   Nothing here.")

    else:
        number = 1
        for task in buckets["MUST DO"]:
            display_task(task, number)
            number += 1

    # Display SHOULD DO
    print("\n⚡ SHOULD DO")

    if len(buckets["SHOULD DO"]) == 0:
        print("   Nothing here.")

    else:
        number = 1
        for task in buckets["SHOULD DO"]:
            display_task(task, number)
            number += 1

    # Display CAN WAIT
    print("\n🌱 CAN WAIT")

    if len(buckets["CAN WAIT"]) == 0:
        print("   Nothing here.")

    else:
        number = 1
        for task in buckets["CAN WAIT"]:
            display_task(task, number)
            number += 1


# ------------------------------------------
# COMPLETE A TASK
# ------------------------------------------

def complete_task():
    print("\n--- Complete Task ---")

    if len(tasks) == 0:
        print("There are no tasks.")
        return

    for i in range(len(tasks)):
        if not tasks[i]["completed"]:
            print(f"{i + 1}. {tasks[i]['name']}")

    try:
        choice = int(input("Enter task number: "))

        if choice < 1 or choice > len(tasks):
            print("Invalid task number.")
            return

        task = tasks[choice - 1]

        if task["completed"]:
            print("That task is already completed.")
        else:
            task["completed"] = True
            print(f"Completed: {task['name']}")

    except ValueError:
        print("Please enter a number.")


# ------------------------------------------
# REMOVE COMPLETED TASKS
# ------------------------------------------

def remove_completed_tasks():
    print("\n--- Remove Completed Tasks ---")

    removed = 0

    for task in tasks[:]:
        if task["completed"]:
            tasks.remove(task)
            removed += 1

    print(f"Removed {removed} completed task(s).")


# ------------------------------------------
# SEARCH FOR A TASK
# ------------------------------------------

def search_task():
    print("\n--- Search Task ---")

    search = input("Search for: ").lower()

    found = False

    for task in tasks:
        if search in task["name"].lower():
            display_task(task, 1)
            found = True

    if not found:
        print("No matching task found.")


# ------------------------------------------
# DAILY UPDATE
# ------------------------------------------

def daily_update():
    print("\n--- Daily Update ---")

    if len(tasks) == 0:
        print("There are no tasks.")
        return

    for task in tasks:

        # Completed tasks don't get promoted
        if task["completed"]:
            continue

        # We assume the user ignored the task today
        task["ignored_days"] += 1

    print("Daily update completed.")
    print("Ignored tasks have become more urgent.")


# ------------------------------------------
# SHOW STATISTICS
# ------------------------------------------

def show_statistics():
    print("\n--- Statistics ---")

    total = len(tasks)
    completed = 0
    must_do = 0
    should_do = 0
    can_wait = 0

    for task in tasks:

        if task["completed"]:
            completed += 1

        bucket = get_bucket(task)

        if bucket == "MUST DO":
            must_do += 1

        elif bucket == "SHOULD DO":
            should_do += 1

        else:
            can_wait += 1

    print(f"Total tasks: {total}")
    print(f"Completed: {completed}")
    print(f"MUST DO: {must_do}")
    print(f"SHOULD DO: {should_do}")
    print(f"CAN WAIT: {can_wait}")


# ------------------------------------------
# MAIN MENU
# ------------------------------------------

def main():

    while True:

        print("\n")
        print("================================")
        print("          LIFE QUEUE")
        print("================================")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Remove completed tasks")
        print("5. Search task")
        print("6. Daily update")
        print("7. Statistics")
        print("8. Exit")
        print("================================")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            remove_completed_tasks()

        elif choice == "5":
            search_task()

        elif choice == "6":
            daily_update()

        elif choice == "7":
            show_statistics()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# ------------------------------------------
# START PROGRAM
# ------------------------------------------

main()