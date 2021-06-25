# 20210624 Testing use of dictionaries by counting characters in a message

message = 'Hey, I wonder how many times each character appears in this message'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
for i in count.items():
    print(i)
    