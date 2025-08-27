ime = input("Unesite svoje ime: ")

def standardna(ime):
    return "Pozdrav " + ime + "!"

lambdaf = lambda ime: "Dobrodošao " + ime + "!"

def treca(funkcija):
    print(funkcija(ime))

treca(standardna)
