juiste_wachtwoord = "programmeren123"
max_pogingen = 5
poging = 0

while poging < max_pogingen:
    invoer = input("Voer het wachtwoord in: ")
    poging += 1

    if invoer == juiste_wachtwoord:
        print(f"Gefeliciteerd! Je hebt het juiste wachtwoord ingevoerd na {poging} poging{'en' if poging > 1 else ''}.")
        break
    else:
        print(f"Fout wachtwoord. Poging {poging} van {max_pogingen}.")

else:
    print("Je hebt te veel foute pogingen gedaan. Je mag niet meer inloggen.")