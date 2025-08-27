def parni_brojevi(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def neparni_brojevi(n):
    for i in range(n):
        if i % 2 != 0:
            yield i

my_gen1 = parni_brojevi(10)
my_gen2 = neparni_brojevi(10)

print("parni: ")
for p in my_gen1:
    print(p)

print("neparni: ")
for nep in my_gen2:
    print(nep)
