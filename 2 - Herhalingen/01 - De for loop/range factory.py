aantal_lijstjes = int(input("Hoeveel lijstjes wilt u zien? "))

lijstjes = []

for i in range(aantal_lijstjes):
    lengte = int(input(f"Hoelang moet lijst {i+1} zijn? "))
    lijstje = list(range(i+1, lengte*(i+1)+1, i+1))
    
    lijstjes.append(lijstje)

print(lijstjes)