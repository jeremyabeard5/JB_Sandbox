# 20210624 Magic 8 Ball, testing functions
import random

answers = ['It is decidedly so.',
           'It is certain.',
           'Yes.',
           'Reply uncertain, ask again.',
           'Hmm, not sure about that one.',
           'Ask again later.',
           'Concentrate and ask again.',
           'My reply is no.',
           'The outlook is not looking good.',
           'Hmm, very doubtful.']

print(answers[random.randint(0,len(answers))])