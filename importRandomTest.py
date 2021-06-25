# 20210624 testing the import of libraries

import random
print('How many random numbers do you want? :')
endNum = input()
endNum = int(endNum)
print('Random numbers between 1 andddd __? :')
rangeHi = input()
rangeHi = int(rangeHi)
for i in range(1,endNum+1):
    print(str(i) + ': ' + str(random.randint(1,rangeHi)))
print('Wow, this program is so random.')    