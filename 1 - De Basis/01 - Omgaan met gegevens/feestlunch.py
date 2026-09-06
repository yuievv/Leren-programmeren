"""
Feestlunch.py

Bereken de kosten van een feestlunch met de volgende producten:
- 17 croissantjes van elk 0,39 euro
- 2 stokbroden van elk 2,78 euro
- 3 kortingsbonnen van elk 0,50 euro
"""

from termcolor import colored

# aantal van producten en prijzen
aantal_croissants = 17
prijs_croissant = 0.39          # euro

aantal_stokbroden = 2
prijs_stokbrood = 2.78          # euro

aantal_kortingsbonnen = 3
waarde_kortingsbon = 0.50       # euro

# berekening
totaal_croissants = aantal_croissants * prijs_croissant
totaal_stokbroden = aantal_stokbroden * prijs_stokbrood
totaal_korting = aantal_kortingsbonnen * waarde_kortingsbon

subtotaal = totaal_croissants + totaal_stokbroden
te_betalen = subtotaal - totaal_korting

# resultaat tonen
print(". ݁₊ ⊹ . ݁ ⟡ ݁ Feestlunch ݁ ⟡ ݁ . ⊹ ₊ ݁.")
print(f"{colored(str(aantal_croissants), 'light_magenta')} croissantjes    : € {colored(f'{totaal_croissants:.2f}', 'red')}")
print(f"{colored(str(aantal_stokbroden), 'blue')} stokbroden       : € {colored(f'{totaal_stokbroden:.2f}', 'red')}")
print(f"Subtotaal          : € {colored(f'{subtotaal:.2f}', 'red')}")
print(f"Korting ({colored(str(aantal_kortingsbonnen), 'green')} bonnen) : - € {colored(f'{totaal_korting:.2f}', 'red')}")
print("—————————————————————————————————")
print(f"Te betalen         : € {colored(f'{te_betalen:.2f}', 'red')}")

print()
print(f"De feestlunch kost je bij de bakker {colored(f'{te_betalen:.2f}', 'red')} euro voor de "
      f"{colored(str(aantal_croissants), 'light_magenta')} croissantjes en de {colored(str(aantal_stokbroden), 'blue')} stokbroden "
      f"als de {colored(str(aantal_kortingsbonnen), 'green')} kortingsbonnen nog geldig zijn!")