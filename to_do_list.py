#Create a simple To Do list app

#Create an empty list where you will save the To-Dos and their status
to_dos = []

while True:
    print("\n===== To-Do List =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

    choice = input("Enter your choice from the list above: ")

    if choice == '1':
        print()
        
        try:
            nr_tasks = int(input("How may To Dos you want to add: "))            
            for i in range(nr_tasks):
                task = input("Enter the task: ")
                to_dos.append({"task": task, "done": False})
                print("Task added!")
        except ValueError:
            print("Please enter a valid number!")

    elif choice == '2':
        print("\nTasks:")
        for index, task in enumerate(to_dos):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index + 1}. {task['task']} - Status: {status}")

    elif choice == '3':
        task_index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_index < len(to_dos):
            to_dos[task_index]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")

    elif choice == '4':
        print("Thank you for using our To-Do List. Have a great day!")
        break

    else:
        print("Invalid choice. Please try again.")

