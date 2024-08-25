class ToDoList:

    def __init__(self):
        self.tasks = []

    def add_task(self):
        num_tasks = int(input("\nHow many tasks do you want to add? "))
        for i in range(num_tasks):
            task_name = input("Enter the task name: ").strip()
            self.tasks.append({"name": task_name, "status": "Pending"})
            print(f"Task '{task_name}' added.")
        print("")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks in the list.\n")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['name']}: [{task['status']}]")
            print("")

    def remove_task(self):

        if not self.tasks:
            print("\nNo tasks to update.\n")
            return
        
        self.view_tasks()

        num_tasks = int(input("\nHow many tasks do you want to remove? "))
        for i in range(num_tasks):
            task_num = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_num < len(self.tasks):
                removed_task = self.tasks.pop(task_num)
                print(f"Task '{removed_task['name']}' removed.")
            else:
                print("Invalid task number.")
        print("")

    def update_task_status(self):

        self.view_tasks()  # Show tasks before asking for updates
        if not self.tasks:
            print("\nNo tasks to update.\n")
            return

        num_tasks = int(input("\nHow many tasks do you want to update? "))
        for i in range(num_tasks):
            task_num = int(input("Enter the task number to update: ")) - 1
            if 0 <= task_num < len(self.tasks):
                status_input = input("Enter the new status ('y' for Completed / 'n' for Pending): ").strip()
                if status_input == 'y':
                    self.tasks[task_num]['status'] = "Completed"
                elif status_input == 'n':
                    self.tasks[task_num]['status'] = "Pending"
                else:
                    print("Invalid input! Please enter 'y' for Completed or 'n' for Pending.")
                    continue
                print(f"Task '{self.tasks[task_num]['name']}' status updated to '{self.tasks[task_num]['status']}'.")
            else:
                print("Invalid task number.")
        print("")

    def clear_all_tasks(self):
        confirmation = input("\nAre you sure you want to clear all tasks? (y/n): ").strip()
        if confirmation == 'y':
            self.tasks.clear()
            print("All tasks cleared.\n")
        else:
            print("Clear action canceled.\n")

todo = ToDoList()

while True:
    print("==============")
    print("To-Do List")
    print("==============")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Update task status")
    print("5. Clear all tasks")
    print("6. Exit")
    print("==============")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == '6':
        print("\nGoodbye!")
        break
    elif choice == '1':
        todo.add_task()
    elif choice == '2':
        todo.view_tasks()
    elif choice == '3':
        todo.remove_task()
    elif choice == '4':
        todo.update_task_status()
    elif choice == '5':
        todo.clear_all_tasks()
    else:
        print("Invalid choice! Please select a valid option.\n")
