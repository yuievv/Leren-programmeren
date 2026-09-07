# Loop door de uren van de dag
for i in range(2): 
    for uur in range(1, 13):  # Binnenste loop voor de uren van 1 tot 12
        if i == 0:
            print(f"{uur} AM")  # Ochtend
        else:
            print(f"{uur} PM")  # Middag