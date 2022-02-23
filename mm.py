import random

kleur = ['oranje', 'blauw', 'groen', 'bruin']

random.seed()
#"oranje": 0, "blauw": 0, "groen" : 0, "bruin" : 0
def vulKleuren(amount):
    zak = {}
    for i in range(amount):
        woord = kleur[random.randint(0,3)]
        try:
            zak[woord] += 1
        except:
            zak.update({woord : 1})
    return zak

amount = int(input("Hoeveel kleuren?\n"))
print(vulKleuren(amount))