vertalingen = {
    "prinses": "koningin",
    "kasteel": "toren",
    "vijand": "vriend",
    "zwaard": "vleermuis",
    "spreuk": "liedje"
}

# Tekst invoeren
input_tekst = input("Voer een tekst in om te vertalen: ")

output_tekst = []
for woord in input_tekst.split():
    woord_zonder_punctuatie = woord.strip('.,!?')
    # Kijken of woord in de dictionary zit, anders vervangen of woord laten staan
    if woord_zonder_punctuatie in vertalingen:
        nieuw_woord = vertalingen[woord_zonder_punctuatie]
        # Eventuele leestekens toevoegen terug na vervanging
        nieuw_woord += woord[len(woord_zonder_punctuatie):]
        output_tekst.append(nieuw_woord)
    else:
        output_tekst.append(woord)

# Lijst met woorden combineren naar een string
output_tekst = " ".join(output_tekst)
 
# Resultaat
print("Vertaalde tekst:")
print(output_tekst)
