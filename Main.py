import csv


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
            subMenus()
            break
        else:
            print("Please choose a viable option: ")
    
        
        
        
def createCSV(taskName,status):
    try:
        with open('file.csv','r') as f :
            id = len(f.readlines())
    except FileNotFoundError as e:
        print(e)
    try:
        with open('file.csv','a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([id,taskName,status])
    except:
        id = 0
    
        
def addTaskMenu():
    while True:
        taskName = input("Enter the task Name (press e to exit): ").lower()
        status = input("Enter the status of this task (press e to exit): ").lower()
        
        if taskName == 'e' or status == 'e':
            MenuPage()
            break
        
        
        createCSV(taskName,status)
        
    

       
def taskListMenu():
    with open('file.csv','r') as f:
        reader = csv.reader(f)
        for row in reader:
            print("ID: " + row[0]+ " Task: " + row[1])
    
    while True:
        print("To view all task with status 'Done' Press 1: ")
        print("To view all tasks with status 'not done' Press 2: ")
        print("To view all tasks with status 'In-Progress' Press 3: ")
        print('To go back to the Main Menu press 4: ')
        
        userInput = input()
        
        if userInput == '1' or userInput == '2' or userInput == '3':
            subMenus(userInput)
            break
        elif userInput == '4':
            MenuPage()
            break
        
        subMenus(userInput)
            
    
def subMenus(userInput):
    statusMap = {'1' : 'done','2' : 'not done','3':'in-progress'}
    filterStatus = statusMap[userInput]
    with open('file.csv','r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2] == filterStatus:
                print(row)
        
        
            
MenuPage()
    

 







