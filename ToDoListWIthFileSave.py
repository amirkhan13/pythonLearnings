import os 

FILENAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    
    tasks=[]
    with open(FILENAME,"r") as file:
        for line in file:
            task,status = line.strip().rsplit("|",1)
            tasks.append({
                "task":task,
                "completed" :status=="Done",
                
            })
        return tasks


def save_task(tasks):
    with open(FILENAME,"w") as file:
        for task in tasks:
            if task["completed"]:
                status ="Done"
            else:
                status="Not Done"
            
            file.write(f"{task['task']} | {status}\n")

def add_task(tasks):
    task_text   =  input("Enter the new task:").strip()

    if task_text =="":
        print("task cannot be empty!!")
        return
    tasks.append({
        "task":task_text,
        "completed":False

    })
    save_task(tasks)
    print("Task added Successfully!!")



def view_tasks(tasks):
    if not tasks:
        print("No tasks Available!!")
        return

    print("\n--Your Tasks--")
    for i, task in enumerate(tasks , start=1):
        status ="Done" if task["completed"] else "Not Done"
        print(f"{i}.{task['task']} | {status}")
      

def complete_task(tasks):
    task_id =int(input("Enter the task number to complete the task:"))

    if 1<=task_id <=len(tasks):
        tasks[task_id-1]["completed"]=True
        save_task(tasks)
        print("Task mark completed Successfully!!")
    else:
        print("Invalid task Number")


def delete_task(tasks):
    task_id =int(input("Enter the task number to delete the task:"))

    if 1<=task_id<=len(tasks):

        tasks.pop(task_id -1)
        save_task(tasks)
        print("Task Deleted Successfully!!")
    else:
        print("Invalid Task Number")

def main():

    tasks =load_tasks()

    while True:
        print("\n--- ToDo Menu ---")
        print("1.add Task")
        print("2.view Task")
        print("3.complete Task")
        print("4.Delete Task")
        print("5.Exit Task")

        choice = input("Enter your choice:")

        if choice == "1":
            add_task(tasks)
        elif choice =="2":
            view_tasks(tasks)
        elif choice =="3":
            complete_task(tasks)
        elif choice =="4":
            delete_task(tasks)
        elif choice =="5":
            print("Good Bye!!")
            break
        else:
            print("Invalid choice! Try again.")

main()


