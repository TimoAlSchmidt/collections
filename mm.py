import random

kleur = ['oranje', 'blauw', 'groen', 'bruin']

random.seed()

def vulKleuren(amount):
    zak = []
    for i in range(amount):
        zak.append(kleur[random.randint(0,3)])

    return zak


amount = int(input("Hoeveel kleuren?\n"))
print(vulKleuren(amount))