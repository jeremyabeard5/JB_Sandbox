#! /usr/bin/python3
# 20210806 practice with web scraping (lockheed tutorial)

import requests
import bs4

def print_list(list_data, list_type):
    print("\nHere is the listing of {}:".format(list_type))
    for item in list_data:
        print(item)


# download web page - get response object
resp = requests.get('https://www.gutenberg.org/catalog/')
try:
    resp.raise_for_status()
except Exception as exc:
    print('Seems there was a problem: %s' % (exc))
print("\nyou should see '200' for status code:")
print(resp.status_code)
input("\npress Enter to continue...\n")

# create a beatifulsoup object from the text attribute of the response object
gut_soup = bs4.BeautifulSoup(resp.text, "html.parser")

# pull all css elements named <input> that have a name attribute with any value
elems = gut_soup.select('input[name]')
print("\nthere are {} elements of type '<input>[name]'".format(len(elems)))
print("... and here they are:")
for item in elems:
    print(item)
input("\npress Enter to continue...\n")
print("\ncheck the 'class' of one of the elements:")
print(type(elems[2]))
print("\nexamine the elements' attributes:")
for item in elems:
    print(item.attrs)
input("\npress Enter to exit...\n")