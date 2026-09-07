import time

while True:
    # Rood licht (20 seconden)
    for _ in range(20):
        print("Rood")
        time.sleep(1)
    
    # Groen licht (30 seconden)
    for _ in range(30):
        print("Groen")
        time.sleep(1)
    
    # Oranje licht (10 seconden)
    for _ in range(10):
        print("Oranje")
        time.sleep(1)
