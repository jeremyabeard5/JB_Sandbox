#! /usr/bin/python3
# 20210724 Mood Tracker - reading and writing to csv

#The following while loop confirms the first and last name of the user
userConfirmName = False
while userConfirmName == False:
    print('Enter your first name : ', end='')
    firstName = input()

    print('Enter your last name : ', end='')
    lastName = input()
    
    print('Name is ' + firstName + ' ' + lastName + '? (y/n) : ', end='')
    confirmation = input()
    if confirmation == ('y' or 'Y'):
        userConfirmName = True
    elif confirmation == ('n' or 'N'): 
        continue #this should bring it back to the beginning
    else:
        print('You suck at responding correctly. Try again. Quitting...') #need to figure out how to quit completely
        
import datetime
dowStrs = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
monStrs = ['January','February','March','April','May','June','July','August','September','October','November','December']

def submitTodaysMood():
    print('\nToday\'s Mood')
    Current_Date = str(datetime.datetime.today().strftime('%Y%m%d'))
    today_year = int(Current_Date[0:4])
    today_mon = int(Current_Date[4:6])
    today_monStr = monStrs[today_mon-1]
    today_day = int(Current_Date[6:8])
    today_dow = dowStrs[datetime.datetime.today().weekday()]
    print('Today is', today_dow, today_monStr, today_day, today_year)
    print('How was the day? (awful 1-10 amazing) : ', end='')
    todaySumm = input()
    
    
    
    
def submitDayMood():
    print('Other Day Mood')
        
#Once user name is confirmed, search for existing moods file with name
if userConfirmName == True:
    #Search for existing moods
    name = firstName.lower() + lastName.lower()
    print(name)
    
    import csv
    import os.path
    file_path = '/home/jeremy/Documents/GitStuff/JB_Sandbox/' + name + '_moods.csv'
    print('File Exists = ' + str(os.path.exists(file_path)))
    if os.path.exists(file_path): #if file exists, read in the data
        csvFile = open(file_path)
        csvReader = csv.reader(csvFile)
        csvData = list(csvReader)
        print(csvData)
#     with open(file_path, "a+") as f: #regardless, write this stuff
#         data = f.read()
#         print(data)
#         #f.seek(0)
#         newRow = '\nIt worked!, yay!, goteam!, woop woop, Good job.'
#         print(newRow)
#         f.write(newRow)
    
    #confirm user selection
    validUserChoice = False
    while validUserChoice == False:
        print('What do you want to do? \n(1) Submit mood for today \n(2) Submit mood for other day \n(3) Quit \nChoice: ', end='')
        userChoice = int(input())
        if userChoice == 1:
            validUserChoice = True
            #Submit mood for today
            print('Choice: Submit mood for today')
            submitTodaysMood()
        elif userChoice == 2:
            validUserChoice = True
            #Submit mood for other day
            print('Choice: Submit mood for other day')
            submitDayMood()
        elif userChoice == 3:
            validUserChoice = True
            #quit
            print('Quitting')
        else:
            print('Invalid selection, try again...')
            

    


    
    
    
    
    
    #If not, create a moods file

    # Ask if that want to set a mood for a custom date, set mood for today, search for a day's mood, or quit

    # IF CUSTOM DATE
    #Ask for year, month, day

    #Ask for scale of 1-10, Ask for specific adjectives prompt

    #If doesn't exist, return message

    #If exists, return mood (formatted)

    # IF SET MOOD FOR TODAY
    #Ask for Scale of 1-10, Ask for specific adjectives

    #Save to file (csv)

    # IF SEARCH FOR A DAY'S MOOD
    # Prompt for year, month, day

    #Search for existing mood

    # If doesn't exist, message

    # If exists, return mood







