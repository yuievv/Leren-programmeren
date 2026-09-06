"""
Question.py

Stelt de gebruiker een aantal vragen over zichzelf (naam, leeftijd,
lievelingseten en lievelingsdrankje) en toont daarna een samenvattende zin.
"""

naam = input("Hallo, wat is je naam? ")
leeftijd = int(input(f"Goedendag {naam}, hoe oud ben je? "))
lievelingseten = input(f"En als {leeftijd} jarige, wat eet je het liefst? ")
lievelingsdrankje = input(f"En wat drink je het liefst bij {lievelingseten}? ")

print("")
print(f"De {leeftijd} jarige {naam} drinkt het liefst {lievelingsdrankje} bij {lievelingseten}")