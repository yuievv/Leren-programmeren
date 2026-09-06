small_prijs = 6.99
medium_prijs = 8.25
large_prijs = 10.89

def vraag_aantal_pizza(afmeting):
    while True:
        try:
            aantal = int(input(f"Hoeveel {afmeting} pizza's wilt u? "))
            if aantal < 0:
                print("Aantal moet een positief getal zijn.")
            else:
                return aantal
        except ValueError:
            print("Dit is geen heel nummer!")

def bereken_prijs(aantal, prijs):
    return aantal * prijs

def print_bon(small_aantal, medium_aantal, large_aantal):
    print(". ݁₊ ⊹ . ݁ ⟡ ݁ Kassabon ݁ ⟡ ݁ . ⊹ ₊ ݁.")
    
    if small_aantal > 0:
        print(f"Pizza's small: {small_aantal} x {small_prijs:.2f} =  {bereken_prijs(small_aantal, small_prijs):.2f}")
    if medium_aantal > 0:
        print(f"Pizza's medium: {medium_aantal} x {medium_prijs:.2f} = {bereken_prijs(medium_aantal, medium_prijs):.2f}")
    if large_aantal > 0:
        print(f"Pizza's large: {large_aantal} x {large_prijs:.2f} = {bereken_prijs(large_aantal, large_prijs):.2f}")
    
    print("—————————————————————————————————")
    totaal = bereken_prijs(small_aantal, small_prijs) + bereken_prijs(medium_aantal, medium_prijs) + bereken_prijs(large_aantal, large_prijs)
    print(f"Totaalprijs:               {totaal:.2f}")

def main():
    small_aantal = vraag_aantal_pizza("small")
    medium_aantal = vraag_aantal_pizza("medium")
    large_aantal = vraag_aantal_pizza("large")
    print_bon(small_aantal, medium_aantal, large_aantal)

main()