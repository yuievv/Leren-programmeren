"""
Minmax.py

Vraagt twee gehele getallen op (a en b) en bepaalt met if/elif/else
welk getal het grootst en welk getal het kleinst is.
"""

a = int(input("Geef getal a: "))
b = int(input("Geef getal b: "))

if a > b:
    Max = a
    Min = b
    print("a is het grootste getal:", Max)
elif a < b:
    Min = a
    Max = b
    print("a is het kleinste getal:", Min)
else:
    Max = a
    Min = b
    print("a en b zijn even groot")

print("Het minimum is:", Min)
print("Het maximum is:", Max)