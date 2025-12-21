"""
 Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task  
2. View Tasks  
3. Mark Task as Completed  
4. Delete Task  
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""

import os
from datetime import datetime


def load_task(task_file):

    tasks = []
    if os.path.exists(task_file):

        with open(task_file , 'r' , encoding='utf-8') as f :
            prev = None 
            for line in f:
                if prev is not None:
                    task , status = line.strip().rsplit('||' , 1)
                    tasks.append({'task' : task , 'status' : status == 'done'})
                prev = line

    return tasks


def add_tasks(tasks , task_file):
    with open(task_file , 'w' , encoding='utf-8') as f :
            curr_time = datetime.now().strftime('%Y-%m-%d - %I:%M %p')
            f.write(f"{curr_time}\n")
            for line in tasks:
                task , status = line['task'] , 'done' if line['status'] else 'not_done'
                f.write(f"{task}||{status}\n")



def view_tasks(tasks):
    if len(tasks)==0:
        print('No Task Found')

    else:
        for idx , i in enumerate(tasks , 1):
            stat = '✅' if i['status'] else ' '
            print(f'{idx}. [{stat}] {i['task']} ')



def task_manager():

    task_file = 'tasks.txt'
    
    while True :
        tasks = load_task(task_file)
        decorate = "*" * 20
        print(f" {decorate}\nWelcome to Task List Manager\n {decorate}\n1. Add Task  \n2. View Tasks \n3. Mark Task as Completed  \n4. Delete Task \n5. Exit")

        choice = input("Please Select your option ( 1-5 ) : ")

        match choice:


            case "1" : #Add Task  
                task_item = input("Please Type your tasks: ").strip()

                if task_item:
                    item = {'task':task_item , 'status':False}
                    tasks.append(item)
                    add_tasks(tasks,task_file)
                else:
                    print('Empty Task is Invalid')



            case "2" :  # view_tasks 
                view_tasks(tasks)




            case "3" : # marks task completed 
                view_tasks(tasks)
                try:
                    task_no = int(input("Pleas give your input: "))
                    print(len(tasks))
                    if 1 <= task_no <= len(tasks) :
                        tasks[task_no-1]['status'] = True
                        add_tasks(tasks,task_file)
                        print('Asked Task is Marked as completed')
                    else:
                        print('Please Enter Valid number')
                except ValueError:
                    print('Please enter  Valid  Input')




            case "4" : # delete task 
                view_tasks(tasks)
                try:
                    task_no = int(input("Pleas give your input to delete task: "))
                    if 1 <= task_no <= len(tasks) :
                        tasks.pop(task_no-1)
                        add_tasks(tasks,task_file)
                        print('Asked Task is Removed')
                    else:
                        print('Please Enter Valid number')
                except  ValueError:
                    print('Please enter  Valid  Input')              



            case "5" :
                print(f"Exiting from Task List Manager !!!! Welcome back ")
                break




            case _:
                print("!!!!!!!!!!!!Please Select your option properly !!!!!!!!!!")

def main():

    task_manager()


if __name__ == '__main__':
    main()