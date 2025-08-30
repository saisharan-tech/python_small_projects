def to_do_list():
    tasks = []

    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            print(f"Task '{task}' added successfully.")
        
        elif choice == "2":
            task = input("Enter task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' removed successfully.")
            else:
                print("Task not found.")
        
        elif choice == "3":
            if tasks:
                print("Tasks: ")
                for task in tasks:
                    print("- " + task)
            else:
                print("No tasks available.")
        
        elif choice == "4":
            print("Exiting the to-do list...")
            break
        else:
            print("Invalid choice. Please try again.")

to_do_list()
