print('Welk seizoen vind jij het fijnst?', 
      "a) Lente", 
      "b) Zomer", 
      "c) Herfst", 
      "d) Winter")
gekozen_seizoen = input('? ').lower()

if gekozen_seizoen == 'a' or gekozen_seizoen == 'c':
    print('Dus jij vindt het tussenseizoen het fijnst...')
elif gekozen_seizoen == 'b':
    print('Dus jij houd van warm weer!')
elif gekozen_seizoen == 'd':
    print('Dus jij houd van koud weer!')