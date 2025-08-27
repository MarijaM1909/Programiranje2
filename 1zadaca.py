import random

redovi = 7
stupci = 7
matrica = []

for i in range(redovi):
    red = []
    for j in range(stupci):
        broj = random.randint(1, 9)
        red.append(broj)
    matrica.append(red)

for i in range(redovi):
    for j in range(stupci):
        print(matrica[i][j], end=" ")
    print()

suma = 0
for i in range(redovi):
    for j in range(stupci):
        if i == 0 or i == redovi - 1 or j == 0 or j == stupci - 1:
            suma += matrica[i][j]

print("Zbroj elemenata na rubovima matrice je:", suma)
