"""
Starttheparty.py

Bepaalt met bepaalde condities of een feest kan beginnen, op basis van
de aanwezigheid van een gastheer, gasten, drank en chips.
"""

# naam van de gebruiker en van de SLB'er`
mijn_naam = "Klaudia"
slb_naam = "Rudi"

gastheer_naam = input("Wie is de gastheer? ")

# geen naam ingevuld betekent dat er geen gastheer is
gastheer = gastheer_naam != ""

gasten = int(input("Hoeveel gasten komen er? "))
# 0 gasten betekent dat er geen gasten zijn
gasten_aanwezig = gasten > 0

drank = True
chips = True

# bepaal of de gastheer de gebruiker zelf is, of de SLB'er
gastheer_is_ik = gastheer_naam == mijn_naam
gastheer_is_slb = gastheer_naam == slb_naam

# een feest kan beginnen als er een gastheer is, of als er gasten zijn
start_condition_1 = gastheer or gasten_aanwezig

# een feest kan beginnen als er een gastheer is, of als er gasten zijn en er zijn chips en drank
start_condition_2 = gastheer or (gasten_aanwezig and chips and drank)

# een feest kan beginnen als er geen chips zijn, of als er drank is
start_condition_3 = (not chips) or drank

# een feest kan beginnen als er geen gasten zijn, of als er chips of drank is
start_condition_4 = (not gasten_aanwezig) or chips or drank

# een feest kan beginnen als er geen gastheer is, of als er drank is
start_condition_5 = (not gastheer) or drank

# alleen chips zijn niet genoeg om een feest te beginnen, er moet ook een gastheer, gasten of drank aanwezig zijn
start_condition_6 = not (chips and not gastheer and not gasten_aanwezig and not drank)

# een feest met gasten kan pas beginnen als er minimaal 4 gasten zijn
start_condition_7 = (not gasten_aanwezig) or gasten >= 4

# een feest kan niet starten als er meer dan 20 aanwezigen zijn (gasten + gastheer)
aantal_aanwezigen = gasten + int(gastheer)
start_condition_8 = aantal_aanwezigen <= 20

if gastheer_is_ik or (not gastheer_is_slb
        and start_condition_1 and start_condition_2 and start_condition_3
        and start_condition_4 and start_condition_5 and start_condition_6
        and start_condition_7 and start_condition_8):
    print('Start the Party')
else:
    print('No Party')