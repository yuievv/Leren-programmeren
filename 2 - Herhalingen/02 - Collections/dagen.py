# Dagen van de week
dagen_van_de_week = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

# Alle dagen van de week
print("Alle dagen van de week zijn:")
for dag in dagen_van_de_week:
    print(f"- {dag}")

# Weekenddagen
weekenddagen = dagen_van_de_week[5:]  # zaterdag en zondag
print("\nDe weekenddagen zijn:", " & ".join(weekenddagen))

# Werkdagen
werkdagen = dagen_van_de_week[:5]  # maandag t/m vrijdag
print("\nDe werkdagen zijn:", ", ".join(werkdagen))

# Alle dagen van de week in omgekeerde volgorde
omgekeerde_dagen = " -> ".join(dagen_van_de_week[::-1])
print("\nAlle dagen van de week in omgekeerde volgorde zijn:", omgekeerde_dagen)

# Werkdagen in omgekeerde volgorde
print("\nDe werkdagen in omgekeerde volgorde zijn:")
for dag in werkdagen[::-1]:
    print(f"- {dag}")

# Weekenddagen in omgekeerde volgorde
print("\nDe weekenddagen in omgekeerde volgorde zijn:", " + ".join(weekenddagen[::-1]))
