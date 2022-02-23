dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

for dag in dagen:
    print(dag)
print()

for dag in range(len(dagen)-2):
    print(dagen[dag])
print()

for dag in range(len(dagen)-5):
    print(dagen[dag+5])
print()

dagen.reverse()

for dag in dagen:
    print(dag)
print()

for dag in range(len(dagen)-2):
    print(dagen[dag+2])
print()

for dag in range(len(dagen)-5):
    print(dagen[dag])
print()