# This program contains To-Do list where list of tasks would be stored in a file for permanent storage and not delete with every sync
TASK_FILE = 'todo_list.txt'

def load_tasks():
    try:
        with open(TASK_FILE, 'r') as f:
            tasks = [line.strip() for line in f.readlines()]
        return tasks
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        for task in tasks:
            f.write(task + '\n')
    print("Task saved successfully!")

def create_task():
    task = input("Enter the task : ")
    return task

def view_task(tasks):
    if not tasks:
        print("\nYour To-Do list is empty.")
        return
    print("\n----------Current To Do List---------------")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print("-----------------------------------------------------------")

def delete_task(index, tasks):
    tasks.pop(index-1)
    return tasks

tasks = load_tasks()
while True:
    query = input("What operation do you want to perform (add/delete/view/exit) tasks : ")
    if query.lower() == 'add':
        tasks.append(create_task())
        save_tasks(tasks)
    
    elif query.lower() == 'view':
        view_task(tasks)

    elif query.lower() == 'delete':
        view_task(tasks)
        try:
            index = int(input("Enter the # of the task, you want to delete : "))
            if 1 <= index <= len(tasks):
                delete_task(index, tasks)
                save_tasks(tasks)
            else:
                print("Error: The number is not in the list")
        except ValueError:
            print("Error: Please enter a valid number.")
    
    elif query.lower() == 'exit':
        break

    else:
        print("Invalid operation...please enter a valid query.")

print("Thanks for using the To-Do list. GoodBye!")
