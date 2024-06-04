"""
To-Do List (Python Lists, Python Loops)

Topics tested:
Python Lists: Managing a list of tasks (adding, removing).
Python Loops: Implementing a loop to continuously prompt the user for actions.

Create a simple to-do list program where users can add, remove, and view tasks.
Use a list to store the tasks, and implement a loop to continuously prompt the user for actions until they choose to exit the program.
"""

shoppingLists = []

def addShoppingList():
    shoppingList = input("Enter a shoppingList: ")
    shoppingLists.append(shoppingList)
    print(f"shoppingList '{shoppingList}' has been added to your list.")

def viewShoppingLists():
    if not shoppingLists:
        print("No shoppingLists found.")
    else:
        print("Here are the shoppingLists:")
        for index, shoppingList in enumerate(shoppingLists):
            print(f"{index+1}. {shoppingList}")

def removeShoppingLists():
    viewShoppingLists()
    try:
        shoppingListToRemove = int(input("Select shoppingList number to remove: "))
        if shoppingListToRemove >= 0 and shoppingListToRemove < len(shoppingLists):
            shoppingLists.pop(shoppingListToRemove)
            print(f"shoppingList {shoppingListToRemove} has been removed")
        else:
            print(f"shoppingList number{shoppingListToRemove} was not found")

    except:
        print("Invalid input.")

if __name__ == "__main__":

    print("Welcome to To Do list app: :)")
    while True:
        print("\n")
        print("Please one of the options")
        print("1. Add a new shoppingList")
        print("2. Remove a shoppingList")
        print("3. View shoppingList")
        print("4. Exit")

        selection = input("Enter your choice: ")

        if(selection == "1"):
            addShoppingList()

        elif(selection == "2"):
            removeShoppingLists()

        elif(selection == "3"):
            viewShoppingLists()

        elif(selection== "4"):
            break

        else:
            print("Invalid input, try again.")

    print("Thankyou, Goodbye!")