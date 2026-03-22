import csv

from Tasks import *


def MenuPage():
    while True:
        print("Press 1 to add task: ")
        print("Press 2 to view all tasks: ")    
        print("Press 3 to edit Status")
        
        userInput = input("Enter: ")
        if userInput == '1':
            addTaskMenu()
            break
        elif userInput == '2':
            taskListMenu()
            break
        elif userInput == '3':
            statusMenu()
            break
        else:
            print("Please choose a viable option: ")
            
def addTaskMenu():
    taskName = ''
    while taskName != 'e':
        taskName = input("Enter the task Name (press e to exit): ").lower()
        if taskName == 'e':
            MenuPage()
            break
        status = input("Enter the status of this task: ").lower()
              
        createCSV(taskName,status)


def taskListMenu():
    rows = readCSV()
    for row in rows:
        print("ID: " + row[0]+ " Task: " + row[1])
    
    while True:
        print("To view all task with status 'Done' Press 1: ")
        print("To view all tasks with status 'not done' Press 2: ")
        print("To view all tasks with status 'In-Progress' Press 3: ")
        print('To go back to the Main Menu press 4: ')
        
        userInput = input()
        
        if userInput == '1' or userInput == '2' or userInput == '3':
            viewTasks(userInput)
            break
        elif userInput == '4':
            MenuPage()
            break

        
        


def statusMenu():
    id = input("Enter the task ID to edit: ")
    editTasks(id)