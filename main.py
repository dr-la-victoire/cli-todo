"""This is command line tool to manage tasks and to do.
With this, you can perform the following activities:
You can view your tasks
You can add a new task
You can mark it as either completed or pending."""

import json

# The dictionary to store the tasks
tasks = {}


# The loop
# Intro text
while True:
    print(
        "Welcome to the CLI Todo App. What do you want to do?\n1. View tasks\n2. Add a new task\n3. Delete a task\n4. Change the details of a task\n5. Exit\m"
    )
    answer = input("Enter a number: ")

    # Conditions for the various events
    if answer == "1":
        # reading the file to get the tasks
        with open("task.json", "r") as file:
            tasks = json.load(file)
        # looping through the dictionary to make it more readable
        print("Here are your tasks: ")
        for task_id, details in tasks.items():
            print(f"Task ID: {task_id}")
            print(f"Description: {details['description']}")
            print(f"Status: {details['status']}")
            print(f"Due Date: {details['due date']}")
            print("*" * 30)
        break

    elif answer == "2":
        # reading the file to get the number of tasks
        with open("task.json", "r") as file:
            tasks = json.load(file)

        # finding the length of the items in the file to give a unique id to each task
        if len(tasks) == 0:
            new_task_id = "task1"
        else:
            the_id = len(tasks) + 1
            new_task_id = "task" + str(the_id)

        # getting user input for the details of the todo
        description = input("What is the task?: ")
        status = input("What is the status (pending or completed)?: ")
        due_date = input("When is it due (format: day-month-year)?: ")

        # appending to the dictionary
        tasks[new_task_id] = {
            "description": description,
            "status": status,
            "due date": due_date,
        }

        # open the file for writing
        with open("task.json", "w") as file:
            json.dump(tasks, file, indent=4)
            print("The task has been successfully added!")
        break

    elif answer == "3":
        with open("task.json", "r") as file:
            tasks = json.load(file)

        task_id = input("Please provide the task id of the task to be deleted: ")
        # error validation to be sure the task id exists
        if task_id in tasks:
            del tasks[task_id]
            with open("task.json", "w") as file:
                json.dump(tasks, file, indent=4)
            print("The task has been successfully deleted.")
            break
        else:
            print("There's no task with this ID")

    elif answer == "4":
        with open("task.json", "r") as file:
            tasks = json.load(file)

        task_id = input(
            "Please provide the task id of the task you want to make changes to: "
        )
        if task_id in tasks:
            item = input("What do you want to change (description/status/due date)?: ")
            item_value = input("What do you want to change it to?: ")

            tasks[task_id][item] = item_value
            with open("task.json", "w") as file:
                json.dump(tasks, file, indent=4)
            print("The status of the task has been successfully changed.")
            break
        else:
            print("There's no task with this ID")
    elif answer == "5":
        print("Goodbye!")
        break
    else:
        print("Please select a number that corresponds with the menu you see.")
