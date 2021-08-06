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
    today_dow = datetime.datetime.today().weekday()
    today_dowStr = dowStrs[today_dow]
    print('Today is', today_dowStr, today_monStr, today_day, today_year)
    print('How was the mood today? (awful 1 - 5 amazing) : ', end='')
    todayMood = input()
    todayMood = int(todayMood) #need to implement checks
    print('Additional notes about mood today? : ', end='')
    todayMoodNotes = input()
    print('Thank you.')
    print('Did you get some exercise today? (1=yes, -1=no, 0=some movement) : ', end='')
    todayExer = input()
    todayExer = int(todayExer) #need to implement checks
    print('Additional notes about exercise? : ', end='')
    todayExerNotes = input()
    print('Thank you.')
    print('How was the quality of food you ate today? (shitty 1 - 5 perfect) : ', end='')
    todayFood = input()
    todayFood = int(todayFood) #need to implement checks
    print('Additional notes about food? : ', end='')
    todayFoodNotes = input()
    print('Thank you.')
    print('How was the quality of sleep last night? (shitty 1 - 5 amazing) : ', end='')
    todaySlp = input()
    todaySlp = int(todaySlp) #need to implement checks
    print('Number of hours of sleep? : ', end='')
    todaySlpHrs = input()
    todaySlpHrs = float(todaySlpHrs) #need to implement checks
    print('Thank you.')
    print('Any other notes about today? : ', end='')
    todayMiscNotes = input()
    todayRow = [today_year, today_mon, today_monStr, today_day, today_dow, today_dowStr, todayMood, todayMoodNotes, todayExer, todayExerNotes, todayFood, todayFoodNotes, todaySlp, todaySlpHrs, todayMiscNotes]
    with open(file_path, "a+") as f: #regardless, write this stuff
        data = f.read()
        print(data)
        f.seek(0)
        print(todayRow)
        todayRowStr = '\n' + str(todayRow)[1:-1]
        f.write(todayRowStr)
    
    
    
def submitDayMood():
    print('\nOther Day\'s Mood')
    print('Enter year (####) : ', end='')
    day_yearInput = input()
    day_year = int(day_yearInput)
    print('Enter month (##) : ', end='')
    day_monInput = input()
    day_mon = int(day_monInput)
    day_monStr = monStrs[day_mon-1]
    print('Enter day (##) : ', end='')
    day_dayInput = input()
    day_day = int(day_dayInput)
    day_dow = datetime.datetime(day_year, day_mon, day_day).weekday()
    day_dowStr = dowStrs[day_dow]
    
    print('Selected Day is', day_dowStr, day_monStr, day_day, day_year)
    print('How was the mood that day? (awful 1 - 5 amazing) : ', end='')
    dayMood = input()
    dayMood = int(dayMood) #need to implement checks
    print('Additional notes about mood that day? : ', end='')
    dayMoodNotes = input()
    print('Thank you.')
    print('Did you get some exercise that day? (1=yes, -1=no, 0=some movement) : ', end='')
    dayExer = input()
    dayExer = int(dayExer) #need to implement checks
    print('Additional notes about exercise? : ', end='')
    dayExerNotes = input()
    print('Thank you.')
    print('How was the quality of food you ate that day? (shitty 1 - 5 perfect) : ', end='')
    dayFood = input()
    dayFood = int(dayFood) #need to implement checks
    print('Additional notes about food? : ', end='')
    dayFoodNotes = input()
    print('Thank you.')
    print('How was the quality of sleep the night before? (shitty 1 - 5 amazing) : ', end='')
    daySlp = input()
    daySlp = int(daySlp) #need to implement checks
    print('Number of hours of sleep? : ', end='')
    daySlpHrs = input()
    daySlpHrs = float(daySlpHrs) #need to implement checks
    print('Thank you.')
    print('Any other notes about that day? : ', end='')
    dayMiscNotes = input()
    dayRow = [day_year, day_mon, day_monStr, day_day, day_dow, day_dowStr, dayMood, dayMoodNotes, dayExer, dayExerNotes, dayFood, dayFoodNotes, daySlp, daySlpHrs, dayMiscNotes]
    with open(file_path, "a+") as f: #regardless, write this stuff
        data = f.read()
        print(data)
        f.seek(0)
        print(dayRow)
        dayRowStr = '\n' + str(dayRow)[1:-1]
        f.write(dayRowStr)
        
        
        
#Once user name is confirmed, search for existing moods file with name
if userConfirmName == True:
    #Search for existing moods
    name = firstName.lower() + lastName.lower()
    print(name)
    
    import csv
    import os.path
    file_path = '/home/jeremy/Documents/GitStuff/JB_Sandbox/' + 'moods_' + name + '.csv'
    print('File Exists = ' + str(os.path.exists(file_path)))
    if os.path.exists(file_path): #if file exists, read in the data
        csvFile = open(file_path)
        csvReader = csv.reader(csvFile)
        csvData = list(csvReader)
        print(csvData)
    else: #file doesn't exist yet
        with open(file_path, "a+") as f: #write initial row
            data = f.read()
            print(data)
            f.seek(0)
            firstRow = ['Year', 'Month', 'Month Name', 'Day', 'Day of Week', 'Day of Week Name', 'Mood (1-5)', 'Mood Notes', 'Exercise (-1-1)', 'Exercise Notes', 'Food (1-5)', 'Food Notes', 'Sleep (1-5)', 'Sleep Hours', 'Misc Notes']
            print(firstRow)
            f.write(str(firstRow)[1:-1])

    
    #user selection
    while True:
        print('What do you want to do? \n(1) Submit mood for today \n(2) Submit mood for other day \n(3) Quit \nChoice: ', end='')
        userChoice = int(input())
        if userChoice == 1:
            #Submit mood for today
            print('Choice: Submit mood for today')
            submitTodaysMood()
        elif userChoice == 2:
            #Submit mood for other day
            print('Choice: Submit mood for other day')
            submitDayMood()
        elif userChoice == 3:            
            print('Quitting...')
            break
        else:
            print('Invalid selection, try again...\n')
            

    







