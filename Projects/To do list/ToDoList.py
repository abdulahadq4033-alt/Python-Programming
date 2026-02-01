def to_do_list():
    tasks = []
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option : ")
        
        if choice == '1':
            task = input("Enter the task to add: ")
            tasks.append(task)
            print(f'Task "{task}" added.')
        
        elif choice == '2':
            if tasks:
                print("Your To-Do List:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("Your To-Do List is empty.")
        
        elif choice == '3':
            if tasks:
                print("Your To-Do List:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f'Task "{removed_task}" removed.')
                else:
                    print("Invalid task number.")
            else:
                print("Your To-Do List is empty.")
        
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")