# This project is a CLI based To-Do List
# Here you can add/view/delete tasks

# Function for creating task
def create_task():
    task = input("Enter the task : ")
    return task

# function for viewing tasks
def view_task(tasks):
    for i in tasks:
        print(i)

# function for deleting tasks
def delete_task(index):
    tasks.pop(index-1)
    return tasks

# program starts from here!
query = int(input("How many tasks you want to enter ? : "))
# empty 'tasks' list
tasks = []

for i in range(query):
    tasks.append(create_task())

# loop to 'add/view/delete' tasks
x = True
while x:

    query2 = input("Want to add/delete/view tasks :  ")
    if query2.lower() == 'add':
        tasks.append(create_task())
    elif query2.lower() == 'view':
        view_task(tasks)
    elif query2.lower() == 'delete':
        index = int(input("Enter the position (1/2/3...) you want to delete : "))
        delete_task(index)
    else:
        print("Invalid input")
    # 'any more operations to perform' section to continue with the loop or break the loop and exit the program
    entry = input("Any more operations to perform (y/n) ? :")
    if entry.lower() == 'y':
        x = True
    elif entry.lower() == 'n':
        x = False
    else:
        print("Invalid Entry")
        x = False