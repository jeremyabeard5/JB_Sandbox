# 20210624 Magic 8 Ball, testing functions
import random

def GetAnswer(n):
    if n == 1:
        return 'It is decidedly so.'
    elif n == 2:
        return 'It is certain.'
    elif n == 3:
        return 'Yes.'
    elif n == 4:
        return 'Reply uncertain, ask again.'
    elif n == 5:
        return 'Hmm, not sure about that one.'
    elif n == 6:
        return 'Ask again later.'
    elif n == 7:
        return 'Concentrate and ask again.'
    elif n == 8:
        return 'My reply is no.'
    elif n == 9:
        return 'The outlook is not looking good.'
    elif n == 10:
        return 'Hmm, very doubtful.'
    
#randNum = random.randint(1,10)
#fortune = GetAnswer(randNum)
#print(fortune)
print(GetAnswer(random.randint(1,10)))