tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append([task, False])

    elif choice == "2":
        if not tasks:
            print("No tasks available")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task[1] else "Not Completed"
                print(f"{i}. {task[0]} - {status}")

    elif choice == "3":
        num = int(input("Enter task number: "))
        if 0 < num <= len(tasks):
            tasks[num - 1][1] = True
        else:
            print("Invalid task number")

    elif choice == "4":
        num = int(input("Enter task number: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
        else:
            print("Invalid task number")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
