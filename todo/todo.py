import os
import pickle


class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            print("Invalid task index.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Not Completed"
                print(f"{i + 1}. {task.description} - {status}")

    def save_to_file(self, filename="todolist.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.tasks, file)

    def load_from_file(self, filename="todolist.pkl"):
        if os.path.exists(filename):
            with open(filename, "rb") as file:
                self.tasks = pickle.load(file)


def main():
    todo_list = ToDoList()

    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Remove Task")
        print("4. Display Tasks")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.display_tasks()
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_task_as_completed(index)
        elif choice == "3":
            todo_list.display_tasks()
            index = int(input("Enter the index of the task to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            todo_list.save_to_file()
            print("To-Do List saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
