# ==========================================
#          TO-DO LIST APPLICATION
# ==========================================

tasks = []


# Function to add a task
def add_task():
    print("\n========== ADD TASK ==========")

    task = input("Enter task: ").strip()

    if task == "":
        print("Task cannot be empty!")
        return

    tasks.append({
        "task": task,
        "completed": False
    })

    print("Task added successfully!")


# Function to view all tasks
def view_tasks():
    print("\n========== YOUR TASKS ==========")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    for number, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f"{number}. {task['task']} - {status}")


# Function to mark a task as completed
def complete_task():
    print("\n========== COMPLETE TASK ==========")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    choice = input("\nEnter task number to complete: ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    task_number = int(choice)

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number!")
        return

    tasks[task_number - 1]["completed"] = True

    print("Task completed successfully!")


# Function to delete a task
def delete_task():
    print("\n========== DELETE TASK ==========")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    choice = input("\nEnter task number to delete: ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    task_number = int(choice)

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number!")
        return

    deleted_task = tasks.pop(task_number - 1)

    print("Task deleted successfully!")
    print("Deleted task:", deleted_task["task"])


# Main program
while True:

    print("\n==========================================")
    print("             TO-DO LIST")
    print("==========================================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("==========================================")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("\nThank you for using To-Do List!")
        break

    else:
        print("\nInvalid choice! Please enter a number from 1 to 5.")