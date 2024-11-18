import sys
import json
from datetime import datetime
from pathlib import Path

""" Create a Path object """
path = Path("tasks.json")

""" Try reading if the Path object exist """
if path.exists():
    contents = path.read_text()
    tasks = json.load(contents)
else:
    tasks = []

""" Setup datetime object """
now = datetime.now()


def main():
    """ Checking user command-line input """
    if len(sys.argv) < 2:
        sys.exit("Missing or invalid command-line argument")

    VALID_COMMAND = ["add", "update", "delete", "list", "mark-in-progress", "mark-done"]
    if sys.argv[1] not in VALID_COMMAND:
        sys.exit(f"Program only accepts the following command {VALID_COMMAND}")

    command = sys.argv[1]
    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Usage: task-cli add <task_description>")
            else:
                task_add(sys.argv[2])
        elif command == "update":
            if len(sys.argv) < 4:
                print("Usage: task-cli update <task_id> <new_description>")
            else:
                task_update(sys.argv[2], sys.argv[3])
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Usage: task-cli delete <task_id>")
            else:
                task_delete(sys.argv[2])
        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Usage: task-cli mark-in-progress <task_id>")
            else:
                task_mark_in_progress(sys.argv[2])
        elif command == "mark-done":
            if len(sys.argv) < 3:
                print("Usage: task-cli mark-done <task_id>")
            else:
                task_mark_done(sys.argv[2])
        elif command == "list":
            if len(sys.argv) > 2:
                task_list(sys.argv[2])
            else:
                task_list()
    except Exception:
        sys.exit("Missing or invalid command-line argument")


def task_save():
    """ Function to save all tasks data after making change """
    with path.open("w") as file:
        json.dump(tasks, file, indent=2)


def task_add(task_name):
    """ Function to create an ID and add the task to a json task list """
    task_id = len(tasks) + 1
    now = datetime.now()
    tasks.append({
        "id": task_id,
        "description": task_name,
        "status": "todo",
        "createdAt": now.strftime("%d/%b/%Y - %H:%M:%S"),
        "updatedAt": now.strftime("%d/%b/%Y - %H:%M:%S")
    })
    task_save()
    print(f"Task ID {task_id} added successfully")


def task_update(id, new_description):
    """ Update existing task id with new description """
    try:
        task_id = int(id)
    except ValueError:
        print("Invalid id number")
    else:
        for task in tasks:
            if task["id"] == task_id:
                task["description"] = new_description
                task["updatedAt"] = now.strftime("%d/%b/%Y - %H:%M:%S")
                task_save()
                print(f"Task ID {id} has been updated sucessfully")
                break
        else:
            print(f"Task ID {id} cannot be found")


def task_delete(id):
    """ Delete existing task id """
    try:
        task_id = int(id)
    except ValueError:
        print("Invalid id number")
    else:
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                del tasks[i]
                task_save()
                print(f"Task ID {id} has been deleted sucessfully")
                break
        else:
            print(f"Task not found")


def task_mark_done(id):
    """ Mark existing task done """
    try:
        task_id = int(id)
    except ValueError:
        print("Invalid id number")
    else:
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "done"
                task["updatedAt"] = now.strftime("%d/%b/%Y - %H:%M:%S")
                task_save()
                print(f"Task ID {id} has been updated sucessfully")
                break
        else:
            print(f"Task not found")


def task_mark_in_progress(id):
    """ Mark existing task in-progress """
    try:
        task_id = int(id)
    except ValueError:
        print("Invalid id number")
    else:
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "in-progress"
                task["updatedAt"] = now.strftime("%d/%b/%Y - %H:%M:%S")
                task_save()
                print(f"Task ID {id} has been updated sucessfully")
                break
        else:
            print(f"Task not found")


def task_list(status=None):
    """ List all task with given status """
    if status:
        filtered_tasks = [task for task in tasks if task["status"] == status]
    else:
        filtered_tasks = tasks
    
    """ Print all the filtered tasks """
    if filtered_tasks:
        for task in filtered_tasks:
            print(f"Task ID {task["id"]:}: {task["description"]}, Status: {task["status"]} was created at {task["createdAt"]} and updated at {task["updatedAt"]}")
    else:
        print("Task not found")


if __name__ == "__main__":
    main()