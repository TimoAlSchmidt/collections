import random

kleur = ['oranje', 'blauw', 'groen', 'bruin']

random.seed()

def vulKleurenList(amount):
    zak = []
    for i in range(amount):
        zak.append(kleur[random.randint(0,3)])

    return zak

def vulKleurenDict(amount):
    zak = {}
    for i in range(amount):
        woord = kleur[random.randint(0,3)]
        try:
            zak[woord] += 1
        except:
            zak.update({woord : 1})
    return zak

def sorteerder(zak):
    if type(zak) == list:
        zak.sort()

    # HOW DO YOU SORT A DICTIONARY?!?
    return zak

amount = int(input("Hoeveel kleuren?\n"))
print(sorteerder(vulKleurenList(amount)))


amount = int(input("Hoeveel kleuren?\n"))
print(sorteerder(vulKleurenDict(amount)))