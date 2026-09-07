import random

# Kleuren
kleuren = ('oranje', 'blauw', 'groen', 'bruin')

# Vraag om het aantal M&M's in zak
aantal = int(input("Hoeveel M&M's wil je aan de zak toevoegen? "))

# Een lege lijst voor de zak met M&M's
zak_met_mms = []

# Vul de zak metkleuren
for _ in range(aantal):
    kleur = random.choice(kleuren)
    zak_met_mms.append(kleur)

# Inhoud van zak
print("Inhoud van de zak met M&M's:", zak_met_mms)