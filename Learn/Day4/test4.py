"""
To-Do List (Python Lists, Python Loops)

Topics tested:
Python Lists: Managing a list of tasks (adding, removing).
Python Loops: Implementing a loop to continuously prompt the user for actions.

Create a simple to-do list program where users can add, remove, and view tasks.
Use a list to store the tasks, and implement a loop to continuously prompt the user for actions until they choose to exit the program.
"""

tasks = []

def addTask():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to your list.")

def viewTasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Here are the Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task {index+1}. {task}")

def removeTask():
    viewTasks()
    try:
        taskToRemove = int(input("Select task number to remove: "))
        if taskToRemove >= 0 and taskToRemove < len(tasks):
            tasks.pop(taskToRemove)
            print(f"Task {taskToRemove} has been removed")
        else:
            print(f"Task number{taskToRemove} was not found")

    except:
        print("Invalid input.")

if __name__ == "__main__":

    print("Welcome to To Do list app: :)")
    while True:
        print("\n")
        print("Please one of the options")
        print("1. Add a new task")
        print("2. Remove a task")
        print("3. View tasks")
        print("4. Exit")

        selection = input("Enter your choice: ")

        if(selection == "1"):
            addTask()

        elif(selection == "2"):
            removeTask()

        elif(selection == "3"):
            viewTasks()

        elif(selection== "4"):
            break

        else:
            print("Invalid input, try again.")

    print("Thankyou, Goodbye!")