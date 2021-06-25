# Practice with for loops, adding numbers
print('Lets add some numbers.')
print('We will start at 1. Where to end? :')
endNumInput = input()
endNum = int(endNumInput)
sum = 0
round = 1
print('Sum is currently ' + str(sum) + '.')
for i in range(endNum+1):
    sum = sum + i
    print('Round ' + str(round) + '. Added ' + str(i) + '. Now sum is ' + str(sum) + '.')
    round = round + 1
    
print('End. Final sum is ' + str(sum) + '.')