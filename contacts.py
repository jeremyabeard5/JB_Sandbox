# 20210625 Testing dictionaries by making a contacts saving application
addresses = {'Mom': '6398 Old Forest Dr, Maineville, OH 45039',
             'Dad': '6398 Old Forest Dr, Maineville, OH 45039',
             'Mike': '145 S 32nd St, Boulder, CO 80305'}
birthdays = {'Mom': '9/26/1962', 'Dad': '1/14/1961', 'Josh': '12/29/1991',
             'Jacob': '3/11/1996', 'Dasha': '3/6/1997'}

strAdded = ''
while True:
    print('Enter a contact name.')
    print('OR, enter nothing to quit: ', end='')
    name = input()
    if name == '':
        print('Copy/Paste the following code to store added names from this session:')
        print(strAdded)
        print('Exiting...')
        break
    
    if name in birthdays:
        print(birthdays[name] + ' is ' + name + '\'s birthday.')
    else:
        print('No information for ' + name + '.')
        print('Enter birthday in MM/DD/YYYY format for ' + name + '. :', end='')
        bday = input()
        birthdays[name] = bday
        print('Thank you. Database updated.')
        #print('Copy/Paste the following line in the code to add to stored database:')
        strAdd = ', \'' + name + '\': \'' + bday + '\''
        strAdded = strAdded + strAdd
        #print(strAdd)
        