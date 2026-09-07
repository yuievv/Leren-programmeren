totale_som = 0
huidig_getal = 50
iteratie = 1

while totale_som <= 1000:
    totale_som += huidig_getal
    print(f"{iteratie}. {' + '.join(map(str, range(50, huidig_getal + 1)))} = {totale_som}")
    huidig_getal += 1
    iteratie += 1
