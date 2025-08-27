rezultati = []

with open('rezultati.csv', 'r', encoding='utf-8') as file:
    for linija in file:
        podaci = linija.strip().split(',')
        if len(podaci) >= 3:
            ime = podaci[0]
            prezime = podaci[1]
            bodovi = int(podaci[2])
        rezultati.append((ime, prezime, bodovi))

print("Studenti koji su položili ispit:")
for ime, prezime, bodovi in rezultati:
    if bodovi > 49:
        print(ime, prezime, bodovi)

print()

def sortiraj_po_prezimenu(student):
    return student[1]

rezultati.sort(key=sortiraj_po_prezimenu)


ocjene = {
    "Nedovoljan": 0,
    "Dovoljan": 0,
    "Dobar": 0,
    "Vrlodobar": 0,
    "Izvrstan": 0
}

for ime, prezime, bodovi in rezultati:
    postotak = (bodovi / 100) * 100
    if postotak < 50:
        ocjene["Nedovoljan"] += 1
    elif postotak < 65:
        ocjene["Dovoljan"] += 1
    elif postotak < 80:
        ocjene["Dobar"] += 1
    elif postotak < 90:
        ocjene["Vrlodobar"] += 1
    else:
        ocjene["Izvrstan"] += 1

print("Broj studenata po ocjenama:")
for ocjena in ocjene:
    print(ocjena + ":", ocjene[ocjena])
