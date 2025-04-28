from task.simple import create_new_task, get_all_tasks, remove_a_task, Task

def main():
    print("Hello from test1!")

    while True:
        print_menu()

        choise = input("Enter choise: ")

        try:
            choise = int(choise)

            if choise == 1:
                create_task()
            elif choise == 2:
                display_tasks()
            elif choise == 3:
                remove_task()
            elif choise == 4:
                break

        except ValueError:
            print("Invalid choise!")

def print_menu():
    print("1. Create new task")
    print("2. Display all tasks")
    print("3. Remove a Task")
    print("4. Exit")

def create_task():

    task = input("Enter task name: ")

    if task:
        task = Task(
            name=task
        )

        new_task = create_new_task(task)

        print(f"New task: {new_task}", end="\n\n")

def display_tasks():
    tasks = get_all_tasks()

    for index, task in enumerate(tasks):
        print(f"{index+1}. {task.id}: {task.name}")

def remove_task():
    task_id = input("Enter task id: ")

    removed_task = remove_a_task(task_id)

    print(removed_task)

    if removed_task is None:
        print("Task not found!")

    print(f"Removed task: {removed_task}", end="\n\n")

if __name__ == "__main__":
    main()
