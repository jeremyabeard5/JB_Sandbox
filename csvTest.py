#! /usr/bin/python3
# 20210628 Practice with pyperclip

import pandas as pd #not really using Pandas, don't need
from pandas import Series, DataFrame #don't need

print('Fuck')
csvFile = pd.read_csv('Webbings.csv')
#print(csvFile)

import csv
csvFile2 = open('Webbings.csv')
csvReader = csv.reader(csvFile2)
csvData = list(csvReader)
#print(csvData)

OG_Manufacturers=[]
OG_Webbings=[]
OG_Materials=[]
OG_MBS=[]
OG_Weight=[]
OG_Stretch6kN=[]
OG_Stretch10kN=[]
OG_Width=[]
OG_Cost=[]
OG_Link=[]

numSheetRows = len(csvData)
for i in range(len(csvData)):
#                print(i)
                OG_Manufacturers = OG_Manufacturers + [csvData[i][0]]
                OG_Webbings = OG_Webbings + [csvData[i][1]]
                OG_Materials = OG_Materials + [csvData[i][2]]
                OG_MBS = OG_MBS + [csvData[i][3]]
                OG_Weight = OG_Weight + [csvData[i][4]]
                OG_Stretch6kN = OG_Stretch6kN + [csvData[i][5]]
                OG_Stretch10kN = OG_Stretch10kN + [csvData[i][6]]
                OG_Width = OG_Width + [csvData[i][7]]
                OG_Cost = OG_Cost + [csvData[i][8]]
                OG_Link = OG_Link + [csvData[i][9]]






OG_Manufacturers = OG_Manufacturers[2:]
#print(Manufacturers)
OG_Webbings = OG_Webbings[2:]
OG_Materials = OG_Materials[2:]
OG_MBS = OG_MBS[2:]
for i in range(len(OG_MBS)):
    OG_MBS[i] = float(OG_MBS[i])

OG_Weight = OG_Weight[2:]
for i in range(len(OG_Weight)):
    OG_Weight[i] = float(OG_Weight[i])

OG_Stretch6kN = OG_Stretch6kN[2:]
for i in range(len(OG_Stretch6kN)):
    OG_Stretch6kN[i] = float(OG_Stretch6kN[i])

OG_Stretch10kN = OG_Stretch10kN[2:]
for i in range(len(OG_Stretch10kN)):
    OG_Stretch10kN[i] = float(OG_Stretch10kN[i])

OG_Width = OG_Width[2:]
for i in range(len(OG_Width)):
    OG_Width[i] = float(OG_Width[i])
    
OG_Cost = OG_Cost[2:]
for i in range(len(OG_Cost)):
    OG_Cost[i] = float(OG_Cost[i])
OG_Link = OG_Link[2:]

maxWebChars = 0
for i in range(len(OG_Webbings)):
    if len(OG_Webbings[i]) > maxWebChars:
        maxWebChars = len(OG_Webbings[i])
print(maxWebChars)

spacedOGWebbings = []
for i in range(len(OG_Webbings)):
    addThisManySpaces = maxWebChars - len(OG_Webbings[i])
    spacedOGWebbings = spacedOGWebbings + [OG_Webbings[i] + addThisManySpaces*' ' + '  ']
#for i in range(len(spacedOGWebbings)):
#    print(spacedOGWebbings[i])
# Strength/Weight
# Strength/Weight/Cost
# Strength/Cost

OG_StrIWeight = []
OG_StrIWeightICost = []
OG_StrICost = []
OG_IWeightICost = []

numRows = len(OG_Manufacturers)
for i in range(numRows):
#    print(i)
    OG_StrIWeight = OG_StrIWeight + [OG_MBS[i]/OG_Weight[i]]
    OG_StrIWeightICost = OG_StrIWeightICost + [OG_MBS[i]/OG_Weight[i]/OG_Cost[i]]
    OG_StrICost = OG_StrICost + [OG_MBS[i]/OG_Cost[i]]
    OG_IWeightICost = OG_IWeightICost + [1/OG_Weight[i]/OG_Cost[i]]

#print(Webbings, StrIWeight)
#print(StrIWeightICost)
#print(StrICost)


# sortSpec sorts a given list and another list along with it
def sortSpec(globSpec, globWebs):
    spec = globSpec
    webs = globWebs
    i=1
    while i < len(webs):
        j = 1
        while j < len(webs):
            if spec[j] > spec[j-1]:
                tmp = spec[j]
                spec[j] = spec[j-1]
                spec[j-1] = tmp
                tmp = webs[j]
                webs[j] = webs[j-1]
                webs[j-1] = tmp
            j+=1
        i+=1
    i = 0
    while i < len(webs):
        print('{} {:.3f}'.format(webs[i], spec[i]))
        i+=1
    #print(webs)
    
# import pylab as pl
import matplotlib.pyplot as plt
def plotSpec(x,y,ttl):
     x1 = []
     for i in range(len(x)):
         x1 = x1 + [i]
     xTicks = x
     plt.figure()
     plt.xticks(x1, xTicks)
     plt.xticks(range(len(x1)), xTicks, rotation=90)
     plt.plot(x,y,'*')
     plt.subplots_adjust(left=0.11, bottom=0.27, right=0.9, top=0.88, hspace=0.2, wspace=0.2)
     plt.title(ttl)
#     plt.ion()
#     pl.pause(0.001)
     plt.show()
     
#     plt.ioff()
#     plt.show()
#import matplotlib.pyplot as plt    
    
    
import copy
print("\nCost")
sortedCost = copy.copy(OG_Cost)
webbings01 = copy.copy(spacedOGWebbings)
sortSpec(sortedCost, webbings01)    

print("\nMBS")
sortedMBS = copy.copy(OG_MBS)
webbings02 = copy.copy(spacedOGWebbings)
sortSpec(sortedMBS, webbings02)

print("\nWeight")
sortedWeight = copy.copy(OG_Weight)
webbings03 = copy.copy(spacedOGWebbings)
sortSpec(sortedWeight, webbings03)

print("\nStr / Weight")
sortedStrIWeight = copy.copy(OG_StrIWeight)
webbings04 = copy.copy(spacedOGWebbings)
sortSpec(sortedStrIWeight, webbings04)

print("\nStr / Weight / Cost")
sortedStrIWeightICost = copy.copy(OG_StrIWeightICost)
webbings05 = copy.copy(spacedOGWebbings)
sortSpec(sortedStrIWeightICost, webbings05)

print("\nStr / Cost")
sortedStrICost = copy.copy(OG_StrICost)
webbings06 = copy.copy(spacedOGWebbings)
sortSpec(sortedStrICost, webbings06)

print("\n1 / Weight / Cost")
sortedIWeightICost = copy.copy(OG_IWeightICost)
webbings07 = copy.copy(spacedOGWebbings)
sortSpec(sortedIWeightICost, webbings07)

print("\nStretch at 6kN")
sortedStretch6kN = copy.copy(OG_Stretch6kN)
webbings08 = copy.copy(spacedOGWebbings)
sortSpec(sortedStretch6kN, webbings08)

x1 = []
for i in range(len(OG_Webbings)):
    x1 = x1 + [i]
#xTicks = x
fig1 = plt.figure()
sp1 = fig1.add_subplot(2,4,1)
plt.grid(True)
xTicks = webbings01
plt.title('Cost')
plt.xticks(x1, xTicks)
plt.xticks(range(len(x1)), xTicks, rotation=90)
plt.plot(webbings01, sortedCost, '*')
plt.subplots_adjust(left=0.11, bottom=0.27, right=0.9, top=0.88, hspace=0.52, wspace=0.2)

sp2 = fig1.add_subplot(2,4,2)
plt.grid(True)
xTicks = webbings02
plt.title('MBS')
plt.xticks(x1, xTicks)
plt.xticks(range(len(x1)), xTicks, rotation=90)
plt.plot(webbings02, sortedMBS, '*')
plt.subplots_adjust(left=0.11, bottom=0.27, right=0.9, top=0.88, hspace=0.52, wspace=0.2)


sp3 = fig1.add_subplot(2,4,3)
plt.grid(True)
xTicks = webbings03
plt.title('g/m')
plt.xticks(x1, xTicks)
plt.xticks(range(len(x1)), xTicks, rotation=90)
plt.plot(webbings03, sortedWeight, '*')
plt.subplots_adjust(left=0.11, bottom=0.27, right=0.9, top=0.88, hspace=0.52, wspace=0.2)

sp4 = fig1.add_subplot(2,4,8)
plt.grid(True)
xTicks = webbings04
plt.title('MBS/Wt')
plt.xticks(x1, xTicks)
plt.xticks(range(len(x1)), xTicks, rotation=90)
plt.plot(webbings04, sortedStrIWeight, '*')
plt.subplots_adjust(left=0.11, bottom=0.27, right=0.9, top=0.88, hspace=0.52, wspace=0.2)

sp5 = fig1.add_subplot(2,4,5)
plt.grid(True)
xTicks = webbings05
plt.title('MBS/Wt/$')
plt.xticks(x1, xTicks)
plt.xticks(range(len(x1)), xTicks, rotation=90)
plt.plot(webbings05, sortedStrIWeightICost, '*')
plt.subplots_adjust(left=0.11, bottom=0.27, right=0.9, top=0.88, hspace=0.52, wspace=0.2)

sp6 = fig1.add_subplot(2,4,6)
plt.grid(True)
xTicks = webbings06
plt.title('MBS/$')
plt.xticks(x1, xTicks)
plt.xticks(range(len(x1)), xTicks, rotation=90)
plt.plot(webbings06, sortedStrICost, '*')
plt.subplots_adjust(left=0.11, bottom=0.27, right=0.9, top=0.88, hspace=0.52, wspace=0.2)

sp7 = fig1.add_subplot(2,4,7)
plt.grid(True)
xTicks = webbings07
plt.title('1/Wt/$')
plt.xticks(x1, xTicks)
plt.xticks(range(len(x1)), xTicks, rotation=90)
plt.plot(webbings07, sortedIWeightICost, '*')
plt.subplots_adjust(left=0.11, bottom=0.27, right=0.9, top=0.88, hspace=0.52, wspace=0.2)

sp8 = fig1.add_subplot(2,4,4)
plt.grid(True)
xTicks = webbings08
plt.title('Stretch at 6kN')
plt.xticks(x1, xTicks)
plt.xticks(range(len(x1)), xTicks, rotation=90)
plt.plot(webbings08, sortedStretch6kN, '*')
plt.subplots_adjust(left=0.11, bottom=0.27, right=0.9, top=0.88, hspace=0.52, wspace=0.2)



#sp1.xticks(x1, xTicks1)
#sp1.xticks(range(len(x1)), xTicks1, rotation=90)
#sp1.plot(webbings01, sortedCost, '*')
#sp1.title('Cost')
#sp1.xticks(x1, webbings02)
#sp2.plot(webbings02, sortedMBS, '*')

# plt.plot(x,y,'*')

# plt.title(ttl)
plt.show()



# plotSpec(webbings01, sortedCost, 'Cost')
# plotSpec(webbings02, sortedMBS, 'MBS (kN)')
# plotSpec(webbings03, sortedWeight, 'g/m')
# plotSpec(webbings04, sortedStrIWeight, 'MBS/Wt')
# plotSpec(webbings05, sortedStrIWeightICost, 'MBS/Wt/$')
# plotSpec(webbings06, sortedStrICost, 'MBS/$')
# plotSpec(webbings06, sortedIWeightICost, '1/Wt/$')