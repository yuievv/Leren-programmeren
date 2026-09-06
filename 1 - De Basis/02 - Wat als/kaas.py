"""
kaas.py

Bepaalt welke kaas de gebruiker in gedachten heeft door een aantal vragen te stellen.
"""

is_geel = input("Is de kaas geel? (ja/nee) ").lower()

if is_geel == "ja":
    heeft_gaten = input("Zitten er gaten in? (ja/nee) ").lower()

    if heeft_gaten == "ja":
        is_duur = input("Is de kaas belachelijk duur? (ja/nee) ").lower()

        if is_duur == "ja":
            kaas = "Emmenthaler"
        else:
            kaas = "Leerdammer"

    else:
        is_hard = input("Is de kaas hard als steen? (ja/nee) ").lower()

        if is_hard == "ja":
            kaas = "Parmigiano Reggiano"
        else:
            kaas = "Goudse kaas"

else:
    heeft_schimmel = input("Heeft de kaas blauwe schimmel? (ja/nee) ").lower()

    if heeft_schimmel == "ja":
        heeft_korst = input("Heeft de kaas korst? (ja/nee) ").lower()

        if heeft_korst == "ja":
            kaas = "Blue de Rochbaron"
        else:
            kaas = "Foume d'ambert"

    else:
        heeft_korst = input("Heeft de kaas korst? (ja/nee) ").lower()

        if heeft_korst == "ja":
            kaas = "Camembert"
        else:
            kaas = "Mozzarella"

print("")
print(f"De kaas die je in gedachten hebt is: {kaas}")