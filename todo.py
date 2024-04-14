import json
import os
from datetime import datetime

# File path for storing tasks
TASKS_FILE = "tasks.json"

# Function to load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    else:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

# Function to add a new task
def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high/medium/low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({"name": task_name, "priority": priority, "due_date": due_date, "completed": False})
    save_tasks(tasks)
    print("Task added successfully.")

# Function to remove a task
def remove_task(tasks):
    print("Select the task to remove:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['name']} - Priority: {task['priority']} - Due Date: {task['due_date']}")
    choice = int(input("Enter task number to remove: ")) - 1
    del tasks[choice]
    save_tasks(tasks)
    print("Task removed successfully.")

# Function to mark a task as completed
def complete_task(tasks):
    print("Select the task to mark as completed:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['name']} - Priority: {task['priority']} - Due Date: {task['due_date']}")
    choice = int(input("Enter task number to mark as completed: ")) - 1
    tasks[choice]["completed"] = True
    save_tasks(tasks)
    print("Task marked as completed.")

# Function to display tasks
def display_tasks(tasks):
    print("Tasks:")
    for task in tasks:
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"- {task['name']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status}")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\nTO-DO List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
