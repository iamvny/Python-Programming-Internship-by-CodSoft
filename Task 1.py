class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task index.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            to_do_list.add_task(task)
        elif choice == "2":
            to_do_list.display_tasks()
        elif choice == "3":
            index = int(input("Enter task index to remove: "))
            to_do_list.remove_task(index)
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
