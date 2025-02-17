tasks = []
"""add task"""
def add_task(task):
    tasks.append({'task': task, 'completed': False})  # Store as a dictionary
    print(f'Task "{task}" is added.')

"""view task"""
def view_task():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            if task ['completed']:
                status = 'completed'
            else:
                status = 'not completed'
            print(f'{index}. {task["task"]} [{status}]')
"""task complete"""
def task_complete()
    

while True:
    action = input("What would you like to do?\n-> add task\n-> view\n-> exit\n").strip().lower()
    if action == 'add':
        task = input("Enter the task you want to add:\n")
        add_task(task)
    elif action == 'view':
        view_task()
    elif action == 'exit':
        print("Exiting the To-Do List app.")
        break
    else:
        print("Invalid option. Please choose 'add', 'view', or 'exit'.")    