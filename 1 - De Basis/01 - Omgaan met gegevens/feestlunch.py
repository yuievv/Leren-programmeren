"""
Feestlunch.py

Bereken de kosten van een feestlunch. De gebruiker voert zelf de aantallen
en prijzen in. Prijzen worden in euro's ingevoerd, maar direct omgezet naar
centen zodat er met hele getallen wordt gerekend in plaats van
met floats.
"""

from termcolor import colored

# gebruiker invoer
aantal_croissants = int(input("Hoeveel croissantjes wil je kopen? "))
prijs_croissant_euro = float(input("Wat kost 1 croissantje in euro's? "))
prijs_croissant_cent = round(prijs_croissant_euro * 100)

aantal_stokbroden = int(input("Hoeveel stokbroden wil je kopen? "))
prijs_stokbrood_euro = float(input("Wat kost 1 stokbrood in euro's? "))
prijs_stokbrood_cent = round(prijs_stokbrood_euro * 100)

aantal_kortingsbonnen = int(input("Hoeveel kortingsbonnen heb je? "))
waarde_kortingsbon_euro = float(input("Wat is 1 kortingsbon waard in euro's? "))
waarde_kortingsbon_cent = round(waarde_kortingsbon_euro * 100)

# berekening in centen
totaal_croissants_cent = aantal_croissants * prijs_croissant_cent
totaal_stokbroden_cent = aantal_stokbroden * prijs_stokbrood_cent
totaal_korting_cent = aantal_kortingsbonnen * waarde_kortingsbon_cent

subtotaal_cent = totaal_croissants_cent + totaal_stokbroden_cent
te_betalen_cent = subtotaal_cent - totaal_korting_cent

# omzetten naar euro's, alleen voor de weergave
te_betalen_euro = te_betalen_cent / 100

# resultaat tonen
print("")
print(". ݁₊ ⊹ . ݁ ⟡ ݁ Feestlunch ݁ ⟡ ݁ . ⊹ ₊ ݁.")
print(f"{colored(str(aantal_croissants), 'light_magenta')} croissantjes    : € {colored(f'{totaal_croissants_cent / 100:.2f}', 'red')}")
print(f"{colored(str(aantal_stokbroden), 'blue')} stokbroden       : € {colored(f'{totaal_stokbroden_cent / 100:.2f}', 'red')}")
print(f"Subtotaal          : € {colored(f'{subtotaal_cent / 100:.2f}', 'red')}")
print(f"Korting ({colored(str(aantal_kortingsbonnen), 'green')} bonnen) : - € {colored(f'{totaal_korting_cent / 100:.2f}', 'red')}")
print("—————————————————————————————————")
print(f"Te betalen         : € {colored(f'{te_betalen_euro:.2f}', 'red')}")

print()
print(f"De feestlunch kost je bij de bakker {colored(f'{te_betalen_euro:.2f}', 'red')} euro voor de "
      f"{colored(str(aantal_croissants), 'light_magenta')} croissantjes en de {colored(str(aantal_stokbroden), 'blue')} stokbroden "
      f"als de {colored(str(aantal_kortingsbonnen), 'green')} kortingsbonnen nog geldig zijn!")