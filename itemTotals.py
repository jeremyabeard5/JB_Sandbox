# 20210625 Testing out nested dictionaries
nest = {'Juan': {'steaks': 5, 'cheese': 3},
        'Mike': {'steaks': 2, 'veggies': 4, 'veggies': 6},
        'Taylor': {'cheese': 2, 'wine': 1, 'veggies': 2}
        }

def totalBrought(guests, item):
    numBrought = 0
    for i, j in guests.items():
        numBrought = numBrought + j.get(item, 0)
    return numBrought

print('Number of things being brought:')
print('  - Steaks  ' + str(totalBrought(nest, 'steaks')))
print('  - Cheeses ' + str(totalBrought(nest, 'cheese')))
print('  - Veggies ' + str(totalBrought(nest, 'veggies')))
print('  - Wine    ' + str(totalBrought(nest, 'wine')))
