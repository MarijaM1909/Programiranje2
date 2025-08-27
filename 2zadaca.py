import random

imena = ['Ivan', 'Antonio', 'Antonija', 'Anto', 'Marijan', 'Zvjezdan', 'Ivan', 'Mihaela', 'Ružica', 'Dorijan', 'Petra', 'Matej', 'Filip', 'Magdalena', 'Mate', 'Iva', 'Danis', 'Josip', 'Nebojša', 'Ante', 'Luka', 'Ante', 'Lorena', 'Ivan', 'Nikola', 'Ivan', 'Helena', 'Ivan', 'Gabrijela', 'Andrija', 'Regina', 'Petar', 'Dino', 'Marija', 'Semir', 'Gabriela', 'Borna', 'Filip', 'Krešimir', 'Ivana', 'Gabrijel', 'Vinko', 'Vinko', 'Romana', 'Viktorija', 'Mija', 'Matej', 'Vinko', 'Luka', 'Antea', 'Ivan', 'Ivan', 'Luka', 'Daniel', 'Nikola', 'Marko']

ocjene = {}

for ime in imena:
    ocjene[ime] = random.randint(1, 5)

brojevi = {}

for ocjena in ocjene.values():
    if ocjena in brojevi:
        brojevi[ocjena] += 1
    else:
        brojevi[ocjena] = 1

studenti = 0

for ocjena in ocjene.values():
    if ocjena > 1:
        studenti += 1

ukupno = len(ocjene)
postotak = (studenti / ukupno) * 100

print("Broj ocjena:", brojevi)
print("Prolaznost:", round(postotak, 2), "%")


