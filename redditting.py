#! /usr/bin/python3
# 20210806 practice with reddit api


#reads in client id and client secret from file
import csv
import os.path
file_path = '/home/jeremy/Documents/GitStuff/JB_Sandbox/' + 'reddit.jb'
print('File Exists = ' + str(os.path.exists(file_path)))
if os.path.exists(file_path):
    csvFile = open(file_path)
    csvReader = csv.reader(csvFile)
    csvData = list(csvReader)
else:
    print('Invalid file path. Modify code...')

import requests
import requests.auth
client_auth = requests.auth.HTTPBasicAuth(csvData[0][0], csvData[1][0])

# Continue from https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps
#Need similar file read in for username and password