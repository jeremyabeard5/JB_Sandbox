# 20210624 Testing out lists by creating cat names
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' or enter nothing to cancel: ', end='')
    newName = input()
    if newName == '':
        break
    catNames = catNames + [newName]
    
print('Your cats names are:')
for name in catNames:
    print('  ' + name)