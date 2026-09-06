"""
Speelhal.py

Berekent de kosten van een dagje speelhal. De gebruiker voert zelf de
aantallen en prijzen in. Prijzen worden in euro's ingevoerd, maar direct
omgezet naar centen zodat er met hele getallen wordt gerekend
in plaats van met floats.
"""

from termcolor import colored

# gebruiker invoer
aantal_personen = int(input("Met hoeveel personen gaan jullie? "))
prijs_toegangsticket_euro = float(input("Wat kost 1 toegangsticket in euro's? "))
prijs_toegangsticket_cent = round(prijs_toegangsticket_euro * 100)

prijs_per_5min_euro = float(input("Wat kost de VIP-VR GameSeat per 5 minuten in euro's? "))
prijs_per_5min_cent = round(prijs_per_5min_euro * 100)
duur_minuten = int(input("Hoeveel minuten willen jullie in de VIP-VR GameSeat? "))
aantal_periodes = duur_minuten // 5     # aantal periodes van 5 minuten

aantal_trakteerders = int(input("Met hoeveel personen trakteren jullie samen? "))

# berekening in centen 
totaal_toegang_cent = aantal_personen * prijs_toegangsticket_cent
prijs_vip_per_persoon_cent = aantal_periodes * prijs_per_5min_cent
totaal_vip_cent = aantal_personen * prijs_vip_per_persoon_cent

totale_kosten_cent = totaal_toegang_cent + totaal_vip_cent

# verdeling van de kosten over het aantal trakteerders
kosten_per_trakteerder_cent = round(totale_kosten_cent / aantal_trakteerders)

# resultaat tonen
print(". ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ Speelhal Dag ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁..")
print(f"Toegang ({colored(str(aantal_personen), 'yellow')} personen)             : € {colored(f'{totaal_toegang_cent / 100:.2f}', 'light_blue')}")
print(f"VIP-VR GameSeat ({colored(str(aantal_personen), 'yellow')} personen)     : € {colored(f'{totaal_vip_cent / 100:.2f}', 'light_blue')}")
print(f"  ({colored(str(aantal_periodes), 'light_red')} x 5 min x € {colored(f'{prijs_per_5min_cent / 100:.2f}', 'light_blue')} p.p. = € {colored(f'{prijs_vip_per_persoon_cent / 100:.2f}', 'light_blue')} p.p.)")
print("──────────────────────♡──────────────────────")
print(f"Totale kosten                    : € {colored(f'{totale_kosten_cent / 100:.2f}', 'light_blue')}")
print("──────────────────────♡──────────────────────")
print(f"Te betalen per trakteerder ({colored(str(aantal_trakteerders), 'yellow')}x)  : € {colored(f'{kosten_per_trakteerder_cent / 100:.2f}', 'light_blue')}")

print()
print(f"Dit geweldige dagje-uit met {colored(str(aantal_personen), 'yellow')} mensen in de Speelhal "
      f"met {colored(str(duur_minuten), 'light_red')} minuten VR kost je maar {colored(f'{kosten_per_trakteerder_cent / 100:.2f}', 'light_blue')} "
      f"euro per persoon voor {colored(str(aantal_trakteerders), 'yellow')} mensen")