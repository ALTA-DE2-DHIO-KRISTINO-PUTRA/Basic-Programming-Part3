bilangan = int(input())
def faktor_bilangan(bilangan):
    faktor = []
    for i in range(1, bilangan + 1):
        if bilangan % i == 0:
            faktor.append(i)
    return faktor

input_bilangan = int(input("Masukkan bilangan: "))
faktor = faktor_bilangan(input_bilangan)
print("Faktor dari", input_bilangan, "adalah:", faktor)
