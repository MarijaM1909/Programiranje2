import re

ime = 'M'       
prezime = 'M'   

regex = '^' + ime + '.*[0-5].* .*' + prezime + '$'
unos = input("Unesi string: ")
if re.match(regex, unos):
    print("Podudara se")
else:
    print("Nije dobar unos")
