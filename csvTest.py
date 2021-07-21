#! /usr/bin/python3
# 20210628 Practice with pyperclip

import pandas as pd
from pandas import Series, DataFrame

print('Fuck')
csvFile = pd.read_csv('Webbings.csv')
print(csvFile)

import csv
csvFile2 = open('Webbings.csv')
csvReader = csv.reader(csvFile2)
csvData = list(csvReader)
print(csvData)

Manufacturers=[]
Webbings=[]
Materials=[]
MBS=[]
Weight=[]
Stretch6kN=[]
Stretch10kN=[]
Width=[]
Cost=[]
Link=[]

numSheetRows = len(csvData)
for i in range(len(csvData)):
                print(i)
                Manufacturers = Manufacturers + [csvData[i][0]]
                Webbings = Webbings + [csvData[i][1]]
                Materials = Materials + [csvData[i][2]]
                MBS = MBS + [csvData[i][3]]
                Weight = Weight + [csvData[i][4]]
                Stretch6kN = Stretch6kN + [csvData[i][5]]
                Stretch10kN = Stretch10kN + [csvData[i][6]]
                Width = Width + [csvData[i][7]]
                Cost = Cost + [csvData[i][8]]
                Link = Link + [csvData[i][9]]




print(Manufacturers)
Manufacturers = Manufacturers[2:]
Webbings = Webbings[2:]
Materials = Materials[2:]
MBS = MBS[2:]
for i in range(len(MBS)):
    MBS[i] = float(MBS[i])

Weight = Weight[2:]
for i in range(len(Weight)):
    Weight[i] = float(Weight[i])

Stretch6kN = Stretch6kN[2:]
for i in range(len(Stretch6kN)):
    Stretch6kN[i] = float(Stretch6kN[i])

Stretch10kN = Stretch10kN[2:]
for i in range(len(Stretch10kN)):
    Stretch10kN[i] = float(Stretch10kN[i])

Width = Width[2:]
for i in range(len(Width)):
    Width[i] = float(Width[i])
    
Cost = Cost[2:]
for i in range(len(Cost)):
    Cost[i] = float(Cost[i])
Link = Link[2:]

# Strength/Weight
# Strength/Weight/Cost
# Strength/Cost

StrIWeight = []
StrIWeightICost = []
StrICost = []

numRows = len(Manufacturers)
for i in range(numRows):
    print(i)
    StrIWeight = StrIWeight + [MBS[i]/Weight[i]]
    StrIWeightICost = StrIWeightICost + [MBS[i]/Weight[i]/Cost[i]]
    StrICost = StrICost + [MBS[i]/Cost[i]]
    


