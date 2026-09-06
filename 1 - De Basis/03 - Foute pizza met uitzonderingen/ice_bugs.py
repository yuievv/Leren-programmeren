aantal1 = int(input('Hoeveel ijsjes van $1.25 wil je bestellen? '))
aantal2 = int(input('En hoeveel ijsjes van $2.10 wil je bestellen? '))

eindprijs = aantal1 * 1.25 + aantal2 * 2.10

print('Dat is dan {:.2f} totaal'.format(eindprijs))