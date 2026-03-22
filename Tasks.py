import csv


def createCSV(taskName,status):
    try:
        with open('file.csv','r') as f :
            id = len(f.readlines())
    except FileNotFoundError as e:
        id = 0
        print(e)
    try:
        with open('file.csv','a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([id,taskName,status])
    except:
        id = 0


def readCSV():
    with open('file.csv','r') as f:
        return list(csv.reader(f) )
    
def editTasks(id):

    rows = list(readCSV())

    
    for row in rows:
        if row[0] == str(id):
            row[2] = input("Enter status: ")
     
     
    with open('file.csv','w',newline='')as f:
        writer = csv.writer(f)
        writer.writerows(rows)
        
def viewTasks(userInput):
    statusMap = {'1' : 'done','2' : 'not done','3':'in-progress'}
    filterStatus = statusMap[userInput]
    rows = readCSV()
    for row in rows:
        if row[2] == filterStatus:
            print(row)