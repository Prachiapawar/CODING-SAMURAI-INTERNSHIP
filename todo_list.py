tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks.")
        else:
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

    elif choice == "3":
        number = int(input("Enter task number: "))
        if number <= len(tasks):
            tasks.pop(number - 1)
            print("Task deleted!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
