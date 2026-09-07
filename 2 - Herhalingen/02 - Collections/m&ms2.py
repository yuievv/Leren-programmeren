import random

# Kleuren
kleuren = ['rood', 'blauw', 'groen', 'geel', 'bruin']

# Aantal m&ms in de zak
aantal_mnms = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? "))

# Lege lijst
zak_met_mnms = {}

# M&ms toevoegen
for _ in range(aantal_mnms):
    # Kleur kiezen
    kleur = random.choice(kleuren)
    # M&M van deze kleur toevoegen of verhoog het aantal als die er al in zit
    if kleur in zak_met_mnms:
        zak_met_mnms[kleur] += 1
    else:
        zak_met_mnms[kleur] = 1

# Inhoud van de zak
print("Zak met M&M's:")
print(zak_met_mnms)
