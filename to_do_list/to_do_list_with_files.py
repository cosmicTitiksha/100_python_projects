# This program is To-Do list, where tasks are saved in a file for long term storage

TASK_FILE = 'todo_list.txt'

# loading tasks stored in a file into a list
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as f:
            tasks = [lines.strip() for lines in f.readlines()]
        return tasks
    except FileNotFoundError:
        return []

# Create task
def create_task():
    task = input("Enter the task, you want to add : ")
    return task

# Save task
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        for task in tasks:
            f.write(task + '\n')
    print("Task saved successfully!!!!")

# Viewing tasks
def view_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Deleting tasks
def delete_task(tasks, index):
    tasks.pop(index-1)
    return tasks

# Program begins executing from here
tasks = load_tasks()

# Loop to keep the operation going...until exiting the loop
while True:
    # Asking the user, which oeration to perform
    query = input("What operation do you to perform, (add/view/delete/exit) tasks ? : ")
    # logic if user entered 'add'
    if query.lower() == 'add':
        tasks.append(create_task())
        save_tasks(tasks)
    
    # if user entered 'View'
    elif query.lower() == 'view':
        view_tasks(tasks)

    # if user entered 'delete'
    elif query.lower() == 'delete':
        try:
            index = int(input("Enter the # you want to delete : "))
            if 1 <= index <= len(tasks):
                tasks = delete_task(tasks, index)
                save_tasks(tasks)
        except ValueError:
            print("Please enter the valid literal")

    # if user entered 'exit'
    elif query.lower() == 'exit':
        print("✌️ Exiting.✌️")
        break

# part, outside the loop
print("Thanks for using To-Do list. GoodBye!!!!")
    