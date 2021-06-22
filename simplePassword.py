passwordFile = open('SecretPasswordFile.txt')
readSecretPassword = passwordFile.read()
secretPassword = readSecretPassword[:-1]
print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
	print('Access granted')
	if typedPassword == '12345':
		print('Idiotic password.')
else:
	print('Access Denied')
