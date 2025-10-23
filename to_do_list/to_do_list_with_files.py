# This project is a file I/O based To-do list
# Here you can add/view/delete tasks

# The file to store our tasks
TASK_FILE = "todo_list.txt"

# --- New File I/O Functions ---
def load_tasks():
    """Reads tasks from the file and returns a list."""
    try:
        with open(TASK_FILE, 'r') as f:
            # strip() removes the newline character at the end of each line
            tasks = [line.strip() for line in f.readlines()]
        return tasks
    except FileNotFoundError:
        # If the file doesn't exist yet, return an empty list
        return []

def save_tasks(tasks):
    """Writes the current list of tasks to the file."""
    with open(TASK_FILE, 'w') as f:
        # Write each task followed by a newline character
        for task in tasks:
            f.write(task + '\n')
    print("Tasks saved successfully!")

# --- Core Task Functions (Improved) ---

# Function for creating task
def create_task():
    task = input("Enter the task : ")
    return task

# function for viewing tasks
def view_task(tasks):
    # Improved UX: check if list is empty and display indexed tasks
    if not tasks:
        print("\nYour To-Do list is currently empty!")
        return
    print("\n--- Current To-Do List ---")
    # enumerate starts the index (i) at 1 for user-friendly display
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print("--------------------------\n")

# function for deleting tasks (Now takes 'tasks' list as an argument)
def delete_task(tasks, index):
    tasks.pop(index - 1)
    return tasks

# --- Program Starts Here (Revised Logic) ---

# Load existing tasks immediately, ignoring your old 'query' input
tasks = load_tasks()
print(f"Loaded {len(tasks)} existing tasks from file.")

# loop to 'add/view/delete' tasks
while True: # Using an infinite loop and 'break' for cleaner exit
    print("\n--- Menu ---")
    query2 = input("Want to add/view/delete/quit? : ")

    if query2.lower() == 'add':
        tasks.append(create_task())
        save_tasks(tasks) # Save immediately after adding

    elif query2.lower() == 'view':
        view_task(tasks)

    elif query2.lower() == 'delete':
        # Added try/except for robust error handling
        view_task(tasks)
        try:
            index = int(input("Enter the # of the task you want to delete: "))
            # Input validation to prevent crashing on index out of range
            if 1 <= index <= len(tasks):
                delete_task(tasks, index)
                save_tasks(tasks) # Save immediately after deleting
            else:
                print("Error: That number is not on the list.")
        except ValueError:
            print("Error: Please enter a valid number.")

    elif query2.lower() == 'quit':
        # A clear, single exit point is cleaner than the "Wanna play again" logic
        break 

    else:
        print("Invalid input. Please choose add, view, delete, or quit.")

print("Thank you for using the To-Do List. Goodbye!")