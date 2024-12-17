def menu():
    print("\nMy To-Do List")
    print("Add task")
    print("View tasks")
    print("Mark task as completed")
    print("Update task")
    print("Delete task")
    print("Exit")
def add_task(tasks):
    task = input("\nType in the task to add:")
    tasks.append(task)
    print("Your task has been added successfully")
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks have been added")
    else:
        print("\nTasks:")
        for i, tasks in enumerate(tasks, start=1):
            print(f"{i}.{tasks}")
def mark_task_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        print("\nNo tasks have been added")
        return
    try:
        index = int(input("\nEnter the task number you completed")) -1
        if 0<= index < len(tasks):
            tasks[index] += " - Completed" 
            print (f"Task '{tasks[index]} marked as completed")
        else:
         print("Invalid task number")
    except ValueError:
        print("Enter a number")
def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        print("\n No tasks have been added")
        return
    try:
        index = int(input("\nEnter the task number you want to update")) -1
        if 0<= index <= len(tasks):
            updated_tasks = input("Enter your update:")
            tasks[index] = updated_tasks
            print("\nTask added successfully")
        else:
            print('Invalid task number')
    except ValueError:
        print("Please enter a number")
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        print("\nNo tasks have been added")
        return
    try:
        index = int(input("\nEnter the task number you want to delete")) -1
        if 0<= index < len(tasks):
            deleted_task = tasks.pop(index)
            print (f"Task {deleted_task} has been deleted")
        else:
            print("Invalid task number")
    except ValueError:
        print("Enter a number")
def main():
    tasks = []
    while True:
        menu()
        choice = input("\nEnter your choice:")
        if choice == '1':
            add_task(tasks)
        elif choice =='2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice =='4':
            update_task(tasks)
        elif choice =='5':
            delete_task(tasks)
        elif choice =='6':
            break
        else:
            print ("Invalid choice")

if __name__ == "__main__":
    main()

            




