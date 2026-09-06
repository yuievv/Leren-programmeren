"""
Feestlunch.py

Bereken de kosten van een feestlunch met de volgende producten:
- 17 croissantjes van elk 0,39 euro
- 2 stokbroden van elk 2,78 euro
- 3 kortingsbonnen van elk 0,50 euro
"""

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
print(f"{aantal_croissants} croissantjes    : € {totaal_croissants:.2f}")
print(f"{aantal_stokbroden} stokbroden       : € {totaal_stokbroden:.2f}")
print(f"Subtotaal          : € {subtotaal:.2f}")
print(f"Korting ({aantal_kortingsbonnen} bonnen) : - € {totaal_korting:.2f}")
print("—————————————————————————————————")
print(f"Te betalen         : € {te_betalen:.2f}")

print()
print(f"De feestlunch kost je bij de bakker {te_betalen:.2f} euro voor de "
      f"{aantal_croissants} croissantjes en de {aantal_stokbroden} stokbroden "
      f"als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn!")