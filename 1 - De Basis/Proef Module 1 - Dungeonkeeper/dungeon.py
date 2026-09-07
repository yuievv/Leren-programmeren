import time, math, random

# Speler statistieken
player_attack = 1
player_defense = 0
player_health = 3
player_rupees = 0
has_key = False
item = None

# === [Herbruikbare gevechtsfunctie] === #
def combat(enemy_name, enemy_attack, enemy_defense, enemy_health):
    global player_health
    
    print(f'Je loopt tegen een {enemy_name} aan.')
    enemy_hit_damage = (enemy_attack - player_defense)
    
    if enemy_hit_damage <= 0:
        print(f'Jij hebt een te goede verdediging voor de {enemy_name}, hij kan je geen schade doen.')
        return player_health
    else:
        enemy_attack_amount = math.ceil(player_health / enemy_hit_damage)
        player_hit_damage = (player_attack - enemy_defense)
        player_attack_amount = math.ceil(enemy_health / player_hit_damage)

        if player_attack_amount < enemy_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de {enemy_name}.')
            player_health = player_health - (player_attack_amount * enemy_hit_damage)
            print(f'Je health is nu {player_health}.')
            return player_health
        else:
            print(f'Helaas is de {enemy_name} te sterk voor je.')
            print('Game over.')
            exit()

# === [Kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [Kamer 7] === #
print('Je loopt door de volgende deur en komt in een kleine kamer.')
# Wizard betovering: 1 op 10 kans dat er geen rupee ligt
if random.randint(1, 10) == 1:
    print('De kamer is betoverd door een wizard. Er ligt geen rupee!')
else:
    print('Op de grond zie je iets glinsteren. Het is een rupee!')
    player_rupees += 1
    print(f'Je pakt de rupee op. Je hebt nu {player_rupees} rupee(s).')

print('Voor je zie je twee deuren:')
print('1. Ga naar het standbeeld (Kamer 2)')
print('2. Ga direct naar de gokmachine (Kamer 8)')
keuze7 = input('Welke deur kies je? (typ 1 of 2): ')
print('')
time.sleep(1)

# === [Vertakking uit Kamer 7] === #
if keuze7 == '1':
    # === [Kamer 2] === #
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een munt vast.')
    print('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')

    # Genereer een willekeurige som
    num1 = random.randint(10, 25)
    num2 = random.randint(-5, 75)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:  # operator == '*'
        correct_answer = num1 * num2

    print(f'Daarboven zie je een som staan {num1}{operator}{num2}=?')
    antwoord = int(input('Wat toets je in?'))

    if antwoord == correct_answer:
        print('Het standbeeld laat de munt vallen en je pakt hem op.')
        player_rupees += 1
        print(f'Je hebt nu {player_rupees} rupee(s).')
    else:
        print('Er gebeurt niets....')

    print('Je ziet achter het standbeeld twee deuren.')
    print('Aan de linkerkant zie je een donkere deur (kamer 6).')
    print('Recht vooruit zie je een deur naar de gokmachine (kamer 8).')
    keuze2 = input('Welke kamer kies je? (typ 6 of 8): ')
    print('')
    time.sleep(1)

    # === [Kamer 6] === #
    if keuze2 == '6':
        print('Je duwt de deur open en stapt een nieuwe, muffe kamer binnen.')
        # De zombie in kamer 6
        combat("zombie", 1, 0, 2)
        print('Achter de zombie zie je een deur en je gaat erdoorheen.')
        print('')
        time.sleep(1)
        # Na kamer 6 ga je automatisch door naar kamer 3 (de winkel)
        # (De code voor kamer 3 staat onderaan)
    else:
        # Als speler voor 8 kiest in kamer 2, ga je naar kamer 8
        # We vallen direct door naar de code van kamer 8 (later in het script)
        pass

# === [Kamer 8 - Gokmachine] === #
# Deze code wordt bereikt als:
# - Speler koos '2' in kamer 7
# - OF speler koos '8' in kamer 2
print('Je komt in een kamer met een mysterieuze gokmachine.')
print('De machine heeft twee dobbelstenen en een scherm met "GOKKEN" erop.')
gok_keuze = input('Wil je de gokmachine gebruiken? (ja/nee): ').lower()

if gok_keuze == 'ja':
    dobbel1 = random.randint(1, 6)
    dobbel2 = random.randint(1, 6)
    totaal = dobbel1 + dobbel2
    print(f'De dobbelstenen rollen: {dobbel1} en {dobbel2}. Totaal: {totaal}.')
    
    if totaal > 7:
        player_rupees *= 2
        print(f'Geluk! Je rupees worden verdubbeld. Je hebt nu {player_rupees} rupees.')
    elif totaal < 7:
        player_health -= 1
        print(f'Pech! Je verliest 1 health. Je hebt nu {player_health} health.')
        if player_health <= 0:
            print('Je health is 0. Je verliest het spel!')
            exit()
    else:  # totaal == 7
        player_rupees += 1
        player_health += 4
        print(f'Jackpot! Je krijgt 1 rupee en 4 health. Je hebt nu {player_rupees} rupees en {player_health} health.')
else:
    print('Je besluit de gokmachine links te laten liggen.')

print('Achter de gokmachine zie je een deur naar een betoverde kamer (kamer 9).')
print('Je loopt erdoorheen.')
print('')
time.sleep(1)

# === [Kamer 9 - Betovering] === #
print('Je stapt een vreemde kamer binnen. De lucht tintelt van magie.')
# Random betovering: +1 defence OF +2 health
betovering = random.choice(['defence', 'health'])
if betovering == 'defence':
    player_defense += 1
    print('Een magisch schild omhult je! Je verdediging is nu +1.')
else:
    player_health += 2
    print('Je voelt je energie stromen! Je health is nu +2.')

print('Je ziet een deur naar de winkel en je stapt erdoorheen.')
print('')
time.sleep(1)

# === [Kamer 3 - Winkel] === #
print('Je stapt de kamer binnen waar een handelaar (goblin) achter een toonbank staat.')
print(f'De goblin kijkt je aan en zegt: "Ik voel dat je {player_rupees} rupee(s) bij je hebt!"')
print('Hij verkoopt de volgende spullen voor 1 rupee per stuk:')
print('1. Schild (+1 verdediging)')
print('2. Zwaard (+2 aanval)')
print('3. Sleutel (opent de schatkist)')
print('4. Stoppen met kopen')

# Shop loop: blijf kopen zolang de speler wil en genoeg rupees heeft
while player_rupees > 0:
    keuze_shop = input('Wat wil je kopen? (typ 1, 2, 3 of 4): ')
    
    if keuze_shop == '1' and player_rupees >= 1:
        item = 'schild'
        player_defense += 1
        player_rupees -= 1
        print('Je koopt een schild en voelt je meteen veiliger.')
        print(f'Je hebt nu {player_rupees} rupee(s) over.')
    elif keuze_shop == '2' and player_rupees >= 1:
        item = 'zwaard'
        player_attack += 2
        player_rupees -= 1
        print('Je koopt een zwaard en voelt je een stuk sterker.')
        print(f'Je hebt nu {player_rupees} rupee(s) over.')
    elif keuze_shop == '3' and player_rupees >= 1:
        has_key = True
        player_rupees -= 1
        print('Je koopt een glimmende sleutel voor de schatkist!')
        print(f'Je hebt nu {player_rupees} rupee(s) over.')
    elif keuze_shop == '4':
        print('Je besluit te stoppen met kopen en loopt door.')
        break
    elif (keuze_shop == '1' or keuze_shop == '2' or keuze_shop == '3') and player_rupees < 1:
        print('Je hebt niet genoeg rupees om dit te kopen.')
        break
    else:
        print('Ongeldige keuze, probeer opnieuw.')

# Als de speler geen rupees meer heeft, is de shop automatisch voorbij
if player_rupees == 0:
    print('Je hebt geen rupees meer om te kopen.')

print('Op naar de volgende deur.')
print('')
time.sleep(1)

# === [Kamer 4] === #
if item:
    print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
else:
    print('Dapper, maar zonder wapens of pantser loop je de kamer binnen.')

# Nieuwe, sterkere vijand (attack: 2, defense: 0, health: 3)
combat("vijand", 2, 0, 3)
print('')
time.sleep(1)

# === [Kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een vijand tegenkomen.')
print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')

if has_key:
    print('Je gebruikt de sleutel om de schatkist te openen.')
    print('Gefeliciteerd! Je hebt de dungeon verslagen en de schat bemachtigd!')
else:
    print('Je probeert de schatkist te openen, maar je hebt geen sleutel.')
    print('De schatkist blijft op slot. Je verliest het spel.')
    print('Game over.')