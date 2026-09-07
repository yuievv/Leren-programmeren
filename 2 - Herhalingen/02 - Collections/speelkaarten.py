import random

# Deck met kaarten
kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']
waarden = [str(i) for i in range(2, 11)] + ['boer', 'vrouw', 'heer', 'aas']
deck = [f"{kleur} {waarde}" for kleur in kleuren for waarde in waarden] + ['joker', 'joker']
random.shuffle(deck)

# Haal de bovenste 7 kaarten van het deck
bovenste_kaarten = deck[:7]
overige_kaarten = deck[7:]

# Toon de bovenste 7 kaarten
for i, kaart in enumerate(bovenste_kaarten, 1):
    print(f"kaart {i}: {kaart}")

# Toon de resterende kaarten
print(f"\ndeck ({len(overige_kaarten)} kaarten): {overige_kaarten}")