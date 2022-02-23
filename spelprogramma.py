import random

random.seed()

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def spelProgramma(spelList, minimum, maximum):
    newList = []
    for i in range(random.randint(minimum, maximum)):
        newList.append(spelList[random.randint(0, 6)])
    return newList

print(spelProgramma(spelList, 1, 5))