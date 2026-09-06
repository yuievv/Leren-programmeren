"""
Speelhal.py

Berekenen de kosten van een dagje speelhal met de volgende producten:
- Toegangstickets: € 7,45 per persoon, voor 5 personen
- VIP-VR GameSeat: € 0,37 per persoon per 5 minuten, voor 45 minuten
- Jij en 1 vriend trakteren, dus de kosten worden verdeeld over 2 personen
"""

from termcolor import colored

# gegevens 
aantal_personen = 5
prijs_toegangsticket = 7.45     # euro p.p

prijs_per_5min = 0.37           # euro p.p per 5 minuten
duur_minuten = 45
aantal_periodes = duur_minuten // 5     # aantal periodes van 5 minuten

aantal_trakteerders = 2         # jij en 1 vriend

# berekening
totaal_toegang = aantal_personen * prijs_toegangsticket
prijs_vip_per_persoon = aantal_periodes * prijs_per_5min
totaal_vip = aantal_personen * prijs_vip_per_persoon

totale_kosten = totaal_toegang + totaal_vip

# verdeling van de kosten over het aantal trakteerders
kosten_per_trakteerder = totale_kosten / aantal_trakteerders

# resultaat tonen
print(". ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ Speelhal Dag ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁..")
print(f"Toegang ({colored(str(aantal_personen), 'yellow')} personen)             : € {colored(f'{totaal_toegang:.2f}', 'light_blue')}")
print(f"VIP-VR GameSeat ({colored(str(aantal_personen), 'yellow')} personen)     : € {colored(f'{totaal_vip:.2f}', 'light_blue')}")
print(f"  ({colored(str(aantal_periodes), 'light_red')} x 5 min x € {colored(f'{prijs_per_5min:.2f}', 'light_blue')} p.p. = € {colored(f'{prijs_vip_per_persoon:.2f}', 'light_blue')} p.p.)")
print("──────────────────────♡──────────────────────")
print(f"Totale kosten                    : € {colored(f'{totale_kosten:.2f}', 'light_blue')}")
print("──────────────────────♡──────────────────────")
print(f"Te betalen per trakteerder ({colored(str(aantal_trakteerders), 'yellow')}x)  : € {colored(f'{kosten_per_trakteerder:.2f}', 'light_blue')}")

print()
print(f"Dit geweldige dagje-uit met {colored(str(aantal_personen), 'yellow')} mensen in de Speelhal "
      f"met {colored(str(duur_minuten), 'light_red')} minuten VR kost je maar {colored(f'{kosten_per_trakteerder:.2f}', 'light_blue')} "
      f"euro per persoon voor {colored(str(aantal_trakteerders), 'yellow')} mensen")